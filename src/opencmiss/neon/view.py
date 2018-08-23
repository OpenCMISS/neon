import json
import os

from atomicwrites import atomic_write
from os.path import expanduser
from importlib import import_module

from PySide2.QtCore import QSettings, QSize, QPoint
from PySide2.QtWidgets import QMainWindow, QUndoStack, QAction, QStackedWidget, QMenu, QFileDialog

from opencmiss.neon.extensions_dialog import ExtensionsDialog
from opencmiss.neon.model import Model
from opencmiss.neon.settings import application_name, organization_name
from opencmiss.neon import __version__ as project_version


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._start_directory = None
        self._handles = []

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

    def _init_extensions(self):
        self._model.load_extensions()
        discovered_extensions = self._model.get_discovered_extensions()
        for discovered_extension in discovered_extensions:
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

        menubar = self.menuBar()
        recent_menu = QMenu("Open Recent")
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(open_action)
        file_menu.addMenu(recent_menu)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        edit_menu = menubar.addMenu('&Edit')
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(delete_action)
        self._view_menu = menubar.addMenu('&View')
        tools_menu = menubar.addMenu('&Tools')
        tools_menu.addAction(extension_action)

        self._undo_action = undo_action
        self._redo_action = redo_action
        self._undo_action.setEnabled(self._undo_stack.canUndo())
        self._redo_action.setEnabled(self._undo_stack.canRedo())

        self._stacked_widget = QStackedWidget()
        self.setCentralWidget(self._stacked_widget)

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

    def _show_extensions(self):
        extension_manager = self._model.get_extension_manager()
        e_dlg = ExtensionsDialog(self)
        e_dlg.set_database(extension_manager.get_database())
        e_dlg.set_available_extensions(extension_manager.get_extensions())
        if e_dlg.exec_():
            extension_manager.set_database(e_dlg.get_database())

    def _instantiate_extension(self, extension_description_tuple):
        extension = extension_description_tuple[0]
        components = extension.split('.')
        components.insert(3, 'handlers')
        handler = '.'.join(components)
        module_name, class_name = handler.rsplit('.', 1)
        module = import_module(module_name)
        class_ = getattr(module, class_name)
        instance = class_()
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

    def _save_as(self):
        file_name, file_type = QFileDialog.getSaveFileName(self,
                                                           "Save Project", self._start_directory,
                                                           "Project Files (*.neon)")
        if file_name:
            self._file_name = file_name
            self._start_directory = os.path.dirname(file_name)
            self._save()

    def update_view_menu_ui(self):
        current_index = self._stacked_widget.currentIndex()
        [action.setEnabled(False if current_index == self._view_change_pairs[action] else True)
         for action in self._view_change_pairs]

    def register_view_change_pair(self, pair):
        self._view_change_pairs[pair[0]] = pair[1]

    def register_save_pair(self, pair):
        self._save_pairs[pair[0]] = pair[1]

    def register_open_pair(self, pair):
        self._open_pairs[pair[0]] = pair[1]

    def persist_extension(self, handle):
        self._handles.append(handle)

    def view_change_triggered(self):
        sender = self.sender()
        if sender in self._view_change_pairs:
            target_index = self._view_change_pairs[sender]
            if self._stacked_widget.currentIndex() != target_index:
                self._stacked_widget.setCurrentIndex(target_index)
                self.update_view_menu_ui()

    def get_zinc_context(self):
        return self._model.get_context()

    def get_stacked_widget(self):
        return self._stacked_widget

    def get_view_menu(self):
        return self._view_menu

    def closeEvent(self, event):
        self._model.save_extensions()
        self._write_settings()
        event.accept()
