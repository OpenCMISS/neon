import glob
import json
import os
import pkgutil
import inspect
from importlib import import_module

from atomicwrites import atomic_write

from PySide2.QtCore import QSettings

from opencmiss.neon.settings import organization_name, application_extensions_name
import opencmiss.neon.extensions as defined_extensions


def _get_subpackages(package_path):
    def is_package(d):
        d = os.path.join(package_path, d)
        return os.path.isdir(d) and glob.glob(os.path.join(d, '__init__.py*'))

    return filter(is_package, os.listdir(package_path))


def get_subpackages(module):
    """This does not return Python 3 style namespace packages!"""
    if hasattr(module, '__path__'):
        subpackages = []
        for module_path in module.__path__:
            subpackages += _get_subpackages(module_path)

        return subpackages

    return _get_subpackages(module.__file__)


def _all_subclasses(cls):
    return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                   for g in _all_subclasses(s)]


def _get_modules_classes(module):
    classes = []
    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)

    return classes


class ExtensionRegister(object):

    @staticmethod
    def _create_extension_entry(extension):
        classes = _get_modules_classes(extension)
        extension = {}
        for class_obj in classes:
            fq_class_name = '.'.join([class_obj.__module__, class_obj.__name__])
            extension[fq_class_name] = True

        return extension

    @staticmethod
    def load():
        extensions = {'version': defined_extensions.__version__, 'extensions': {}}

        package_path = os.path.dirname(defined_extensions.__file__)
        registered_extensions = [name for _, name, _ in pkgutil.iter_modules([package_path])]
        for registered_extension in registered_extensions:
            module_name = '.'.join([defined_extensions.__name__, registered_extension])
            registered_module = import_module(module_name)
            extensions['extensions'].update(ExtensionRegister._create_extension_entry(registered_module))

        return extensions


class ExtensionManager(object):

    def __init__(self):
        extension_settings = QSettings(QSettings.IniFormat, QSettings.UserScope, organization_name,
                                       application_extensions_name)
        self._file_name = extension_settings.fileName()
        self._extension_database = None
        self._discovered_extensions = None

        if not os.path.exists(self._file_name):
            extension_settings.beginGroup("Extensions")
            extension_settings.setValue('Empty', True)
            extension_settings.endGroup()

    def load(self):
        """Load settings for extensions from file."""
        self._update_extensions()
        self._discovered_extensions = self._discover_extensions()

    def _discover_extensions(self):
        discovered_extensions = []
        for extension in self._extension_database['extensions']:
            if self._extension_database['extensions'][extension]:
                oc_extensions_package = import_module('opencmiss.extensions')
                subpackages = get_subpackages(oc_extensions_package)
                for subpackage in subpackages:
                    imported_extension = import_module('.'.join(['opencmiss.extensions', subpackage]))
                    classes = _get_modules_classes(imported_extension)
                    for class_obj in classes:
                        mro_s = inspect.getmro(class_obj)
                        for mro in mro_s:
                            fq_class_name = '.'.join([mro.__module__, mro.__name__])
                            if fq_class_name == extension:
                                discovered_extensions.append((extension, class_obj.__module__,
                                                              class_obj.__name__, class_obj))
                                break

        return discovered_extensions

    def _update_extensions(self):
        # Read in registered extensions
        self._extension_database = ExtensionRegister.load()
        extension_settings = {}
        with open(self._file_name) as f:
            try:
                extension_settings = json.loads(f.read())
                if extension_settings is None:
                    extension_settings = {}
            except ValueError as e:
                print('Loading extension settings failed.')
                print(e)
        if 'version' in extension_settings and extension_settings['version'] == self._extension_database['version']:
            self._extension_database['extensions'].update(extension_settings['extensions'])

    def save(self):
        with atomic_write(self._file_name, overwrite=True) as f:
            try:
                string_form = json.dumps(self._extension_database, default=lambda o: o.__dict__, sort_keys=True, indent=4)
                f.write(string_form)
            except Exception as e:
                print('Storing extension settings failed.')
                print(e)

    def get_database(self):
        """Get the database of extensions that is part of the extensions structure."""
        return self._extension_database['extensions']

    def set_database(self, database):
        """Set the database of extensions that is part of the extensions structure."""
        self._extension_database['extensions'] = database

    def get_extensions(self):
        return self._discovered_extensions
