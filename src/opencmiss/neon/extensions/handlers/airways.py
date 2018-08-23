
class AirwayMask(object):

    @staticmethod
    def instantiate(main_view, cls):
        """Have a point to load some data and set up some graphics."""
        extension = cls(main_view)
        main_view.persist_extension(extension)
        main_view.register_save_pair(('airway_mask', extension.save))
        main_view.register_open_pair(('airway_mask', extension.open))
