
from opencmiss.zinc.context import Context

from opencmiss.neon.extension_manager import ExtensionManager


class Model(object):

    def __init__(self):
        self._extension_manager = ExtensionManager()
        self._context = Context('neon')

    def load_extensions(self):
        """Load extensions found but only those that are enabled."""
        self._extension_manager.load()

    def save_extensions(self):
        self._extension_manager.save()

    def get_extension_manager(self):
        return self._extension_manager

    def get_discovered_extensions(self):
        return self._extension_manager.get_extensions()

    def get_context(self):
        return self._context
