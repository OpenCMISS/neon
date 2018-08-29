import json
import os

from atomicwrites import atomic_write
from os.path import expanduser
from importlib import import_module

from PySide2 import QtOpenGL
from PySide2.QtCore import QSettings, QSize, QPoint
from PySide2.QtWidgets import QMainWindow, QUndoStack, QAction, QStackedWidget, QMenu, QFileDialog, QMessageBox

from opencmiss.neon.extensions.handlers.base import BaseOpenGLHandler
from opencmiss.neon.extensions_dialog import ExtensionsDialog
from opencmiss.neon.model import Model
from opencmiss.neon.settings import application_name, organization_name
from opencmiss.neon import __version__ as project_version


class RegisteredView(object):

    def __init__(self, index, action_text, action_tooltip):
        self._index = index
        self._action_text = action_text
        self._action_tooltip = action_tooltip

    def get_text(self):
        return self._action_text

    def get_tooltip(self):
        return self._action_tooltip

    def get_index(self):
        return self._index


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._start_directory = None
        self._handles = []
        self._registered_views = {}
        self._registered_graphics_initialized_callback = {}
        self._registered_view_labels = []

        self._read_settings()

        self._model = Model()

        self._undo_stack = QUndoStack()
        self._undo_action = None
        self._redo_action = None
        self._view_menu = None
        self._stacked_widget = None

        self._view_change_pairs = {}
        self._save_pairs = {}
        self._open_pairs = {}

        self._init_project()

        self._init_ui()

        self._init_extensions()

        self._make_connections()

    def _make_connections(self):
        for key in self._registered_graphics_initialized_callback:
            view = self._registered_views[key]
            view_widget = self._stacked_widget.widget(view.get_index())
            view_widget.graphics_initialized.connect(self._registered_graphics_initialized_callback[key])

    def _init_extensions(self):
        self._model.load_extensions()
        extension_manager = self._model.get_extension_manager()
        discovered_extensions = self._model.get_discovered_extensions()
        for discovered_extension in discovered_extensions:
            if extension_manager.is_extension_enabled(discovered_extension):
                self._instantiate_extension(discovered_extension)

    def _init_project(self):
        self._file_name = None

    def _init_ui(self):
        new_action = QAction('&New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Create new project')
        new_action.triggered.connect(self._new)

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self._save)

        save_as_action = QAction('&Save As ...', self)
        save_as_action.triggered.connect(self._save_as)

        open_action = QAction('&Open ...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open saved project')
        open_action.triggered.connect(self._open)

        exit_action = QAction('&Quit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        extension_action = QAction('&Extensions', self)
        extension_action.setStatusTip('Manage extensions')
        extension_action.triggered.connect(self._show_extensions)

        undo_action = QAction('&Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.setStatusTip('Undo')
        undo_action.triggered.connect(self._undo)

        redo_action = QAction('&Redo', self)
        redo_action.setShortcut('Ctrl+Shift+Z')
        redo_action.setStatusTip('Redo')
        redo_action.triggered.connect(self._redo)

        cut_action = QAction('&Cut', self)
        cut_action.setShortcut('Ctrl+X')
        cut_action.setStatusTip('Cut')
        cut_action.triggered.connect(self._cut)

        copy_action = QAction('&Copy', self)
        copy_action.setShortcut('Ctrl+C')
        copy_action.setStatusTip('Copy')
        copy_action.triggered.connect(self._copy)

        paste_action = QAction('&Paste', self)
        paste_action.setShortcut('Ctrl+V')
        paste_action.setStatusTip('Paste')
        paste_action.triggered.connect(self._paste)

        delete_action = QAction('&Delete', self)
        delete_action.setStatusTip('Delete')
        delete_action.triggered.connect(self._delete)

        self.statusBar()

        menu_bar = self.menuBar()
        recent_menu = QMenu("Open Recent")
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(open_action)
        file_menu.addMenu(recent_menu)
        self._file_pre_exit_action_separator_action = file_menu.addSeparator()
        file_menu.addAction(exit_action)
        self._file_menu = file_menu
        edit_menu = menu_bar.addMenu('&Edit')
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(delete_action)
        self._view_menu = menu_bar.addMenu('&View')
        self._setup_view_menu()
        self._view_menu.aboutToShow.connect(self._view_menu_about_to_show)
        tools_menu = menu_bar.addMenu('&Tools')
        tools_menu.addAction(extension_action)

        self._undo_action = undo_action
        self._redo_action = redo_action
        self._undo_action.setEnabled(self._undo_stack.canUndo())
        self._redo_action.setEnabled(self._undo_stack.canRedo())

        self._stacked_widget = QStackedWidget()
        self.setCentralWidget(self._stacked_widget)

        self._one_opengl_widget_to_rule_them_all = QtOpenGL.QGLWidget()

        self.setWindowTitle('Neon')

    def _write_settings(self):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, organization_name, application_name)
        settings.beginGroup("MainWindow")
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())
        settings.endGroup()
        settings.beginGroup("Project")
        settings.setValue("start_directory", self._start_directory)
        settings.endGroup()

    def _read_settings(self):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, organization_name, application_name)
        settings.beginGroup("MainWindow")
        self.resize(settings.value("size", QSize(400, 400)))
        self.move(settings.value("pos", QPoint(200, 200)))
        settings.endGroup()
        settings.beginGroup("Project")
        self._start_directory = settings.value("start_directory", expanduser("~"))
        settings.endGroup()

    # noinspection PyCallByClass
    def _show_extensions(self):
        extension_manager = self._model.get_extension_manager()
        e_dlg = ExtensionsDialog(self)
        prior_database = extension_manager.get_database()
        e_dlg.set_database(prior_database)
        e_dlg.set_available_extensions(extension_manager.get_extensions())
        if e_dlg.exec_():
            post_database = e_dlg.get_database()
            if post_database != prior_database:
                QMessageBox.information(self, "Extensions changed", "The configuration of extensions has changed, "
                                                                    "you will need to restart the application for "
                                                                    "these changes to take effect.")
                extension_manager.set_database(post_database)

    def _instantiate_extension(self, extension_description_tuple):
        extension = extension_description_tuple[0]
        components = extension.split('.')
        components.insert(3, 'handlers')
        handler = '.'.join(components)
        module_name, class_name = handler.rsplit('.', 1)
        module = import_module(module_name)
        class_ = getattr(module, class_name)
        instance = class_()
        if issubclass(class_, BaseOpenGLHandler):
            instance.instantiate(self, extension_description_tuple[3], self._one_opengl_widget_to_rule_them_all)
        else:
            instance.instantiate(self, extension_description_tuple[3])

    def _redo(self):
        pass

    def _undo(self):
        pass

    def _cut(self):
        pass

    def _copy(self):
        pass

    def _paste(self):
        pass

    def _delete(self):
        pass

    # noinspection PyCallByClass
    def _open(self):
        file_name, file_type = QFileDialog.getOpenFileName(self,
                                                           "Open Project", self._start_directory,
                                                           "Project Files (*.neon)")
        if file_name:
            self._file_name = file_name
            self._start_directory = os.path.dirname(file_name)
            with open(file_name) as f:
                project = f.read()
                json_form = json.loads(project)
                if "version" in json_form:
                    if json_form["version"] == project_version:
                        for key in json_form:
                            if key in self._open_pairs:
                                self._open_pairs[key](json_form[key])

    def _open_recent(self):
        pass

    def _new(self):
        pass

    def _save(self):
        if self._file_name is None:
            self._save_as()
        else:
            with atomic_write(self._file_name, overwrite=True) as f:
                try:
                    project = {'version': project_version}
                    for key in self._save_pairs:
                        project[key] = self._save_pairs[key]()
                    string_form = json.dumps(project, default=lambda o: o.__dict__, sort_keys=True, indent=4)
                    f.write(string_form)
                except Exception as e:
                    print('Saving project failed.')
                    print(e)

    # noinspection PyCallByClass
    def _save_as(self):
        file_name, file_type = QFileDialog.getSaveFileName(self,
                                                           "Save Project", self._start_directory,
                                                           "Project Files (*.neon)")
        if file_name:
            self._file_name = file_name
            self._start_directory = os.path.dirname(file_name)
            self._save()

    def _view_menu_about_to_show(self):
        self._setup_view_menu()
        current_index = self._stacked_widget.currentIndex()
        for label in self._registered_view_labels:
            registered_view = self._registered_views[label]
            action = QAction(registered_view.get_text(), self._view_menu)
            action.setToolTip(registered_view.get_tooltip())
            action.setData(label)
            action.triggered.connect(self._view_change_triggered)
            action.setCheckable(True)
            if current_index == registered_view.get_index():
                action.setChecked(True)

            self._view_menu.addAction(action)

    def _view_change_triggered(self):
        current_index = self._stacked_widget.currentIndex()
        label = self.sender().data()
        requested_index = self._registered_views[label].get_index()
        if requested_index != current_index:
            self._stacked_widget.setCurrentIndex(requested_index)

    def _setup_view_menu(self):
        self._view_menu.clear()
        action = QAction('Minimise', self._view_menu)
        # action.setShortcut('ctrl m')
        self._view_menu.addAction(action)
        self._view_menu.addSeparator()

    def register_view(self, label, widget, menu_text, menu_tooltip):
        widget_index = self._stacked_widget.count()
        self._stacked_widget.addWidget(widget)
        self._registered_views[label] = RegisteredView(widget_index, menu_text, menu_tooltip)
        self._registered_view_labels.append(label)

        # zinc_scene_action = QAction('&Zinc Orthographic+ view', self._view_menu)
        # zinc_scene_action.setStatusTip('Set the current view to the Zinc orthographic+ view')
        # zinc_scene_action.setData(label)
        # zinc_scene_action.triggered.connect(self._view_change_triggered)

    def register_graphics_initialized_callback(self, label, callee):
        self._registered_graphics_initialized_callback[label] = callee

    def get_view(self, label):
        return self._registered_views[label]

    def get_view_widget_at(self, index):
        return self._stacked_widget.widget(index)

    def register_save_pair(self, pair):
        self._save_pairs[pair[0]] = pair[1]

    def register_open_pair(self, pair):
        self._open_pairs[pair[0]] = pair[1]

    def persist_extension(self, handle):
        self._handles.append(handle)

    def get_zinc_context(self):
        return self._model.get_context()

    def get_stacked_widget(self):
        return self._stacked_widget

    def get_file_menu(self):
        return self._file_menu

    def add_import_action(self, import_action):
        file_actions = self._file_menu.actions()
        try:
            import_menu_action = [action for action in file_actions if action.text() == 'Import'][0]
        except IndexError:
            import_menu_action = None

        if import_menu_action is None:
            import_menu = QMenu('Import')
            self._file_menu.insertSeparator(self._file_pre_exit_action_separator_action)
            import_menu_action = self._file_menu.insertMenu(self._file_pre_exit_action_separator_action, import_menu)

        import_menu_action.menu().addAction(import_action)

    def get_start_directory(self):
        return self._start_directory

    def set_start_directory(self, start_directory):
        self._start_directory = start_directory

    def closeEvent(self, event):
        self._model.save_extensions()
        self._write_settings()
        event.accept()
