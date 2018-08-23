import os

from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QTreeWidgetItem, \
    QTreeWidgetItemIterator, QTreeWidget


class ExtensionsDialog(QDialog):

    def __init__(self, parent=None):
        super(ExtensionsDialog, self).__init__(parent)
        self._database_version = None

        loader = QUiLoader()
        ui_file = os.path.join(os.path.dirname(__file__), 'ui', 'extensions_widget.ui')
        self._widget = loader.load(ui_file)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._widget)
        self.setLayout(layout)

        self._make_connections()

    def _make_connections(self):
        button_box = self.findChild(QDialogButtonBox, '_buttonBox')
        button_box.rejected.connect(self.reject)
        button_box.accepted.connect(self.accept)

    def _database_to_tree_view(self, database):
        tree_widget = self.findChild(QTreeWidget, '_treeWidgetExtensions')
        # Transform database to a more convenient form.
        convenient_database = _convert_database(database)

        # Now keys in convenient database are tree branches, with a list of leaves that hold the state of the extension.
        tree_widget.setColumnCount(1)
        tree_widget.setHeaderHidden(True)
        for key in convenient_database:
            top_level_item = QTreeWidgetItem()
            top_level_item.setText(0, key)
            tree_widget.addTopLevelItem(top_level_item)
            for extension_tuple in convenient_database[key]:
                child_item = QTreeWidgetItem(top_level_item)
                child_item.setText(0, extension_tuple[0])
                child_item.setCheckState(0, Qt.Checked if extension_tuple[1] else Qt.Unchecked)

    def _tree_view_to_database(self):
        tree_widget = self.findChild(QTreeWidget, '_treeWidgetExtensions')
        database = {}
        it = QTreeWidgetItemIterator(tree_widget)
        while it.value():
            item = it.value()
            if item is not None and item.parent() is not None:
                module_name = '.'.join([item.parent().text(0), item.text(0)])
                database[module_name] = True if item.checkState(0) == Qt.Checked else False

            it += 1

        return database

    def set_database(self, database):
        self._database_to_tree_view(database)

    def get_database(self):
        return self._tree_view_to_database()

    def set_available_extensions(self, available_extensions):
        convenient_extensions = _convert_extensions(available_extensions)
        tree_widget = self.findChild(QTreeWidget, '_treeWidgetExtensions')
        it = QTreeWidgetItemIterator(tree_widget)
        while it.value():
            item = it.value()
            if item is not None and item.parent() is not None:
                if [item.parent().text(0), item.text(0)] not in convenient_extensions:
                    item.setCheckState(0, Qt.Unchecked)
                    item.setDisabled(True)

            it += 1

def _convert_database(database):
    """
    Transforms a Neon database into a more convenient form for putting into a tree widget.
    :param database: The Neon database to convert.
    :return: Convenient form of the database.
    """
    convenient_database = {}
    for key in database:
        p, m = key.rsplit('.', 1)
        if p in convenient_database:
            convenient_database[p].append((m, database[key]))
        else:
            convenient_database[p] = [(m, database[key])]

    return convenient_database

def _convert_extensions(extensions):
    converted_extensions = [extension[0].rsplit('.', 1) for extension in extensions]
    return converted_extensions