
from PySide2.QtWidgets import QMenu, QAction


class AirwaysMask(object):

    @staticmethod
    def instantiate(main_view, cls):
        """Have a point to load some data and set up some graphics."""
        extension = cls(main_view)
        main_view.persist_extension(extension)
        main_view.register_save_pair(('airways_mask', extension.save))
        main_view.register_open_pair(('airways_mask', extension.open))

        import_action = QAction('Airways Mask', main_view)
        main_view.add_import_action(import_action)
        import_action.triggered.connect(extension.import_airways_mask)
