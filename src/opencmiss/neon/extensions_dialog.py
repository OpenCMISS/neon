import os

from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QTreeView, QTreeWidgetItem, \
    QTreeWidgetItemIterator


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
        tree_widget = self.findChild(QTreeView, '_treeWidgetExtensions')
        # Transform database to a more convenient form.
        convenient_database = {}
        for key in database:
            p, m = key.rsplit('.', 1)
            if p in convenient_database:
                convenient_database[p].append((m, database[key]))
            else:
                convenient_database[p] = [(m, database[key])]

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
        tree_widget = self.findChild(QTreeView, '_treeWidgetExtensions')
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
