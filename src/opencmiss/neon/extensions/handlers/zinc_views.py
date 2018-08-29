
from opencmiss.neon.extensions.handlers.base import BaseOpenGLHandler


class ZincView(BaseOpenGLHandler):

    @staticmethod
    def instantiate(main_view, cls, master_opengl_widget):
        widget = cls(main_view.get_zinc_context(), master_opengl_widget)
        main_view.register_view('Basic', widget,
                                'Zinc basic view', 'Set the current view to the Zinc basic view')


class ZincOrthographicPlusView(BaseOpenGLHandler):

    @staticmethod
    def instantiate(main_view, cls, master_opengl_widget):
        widget = cls(main_view.get_zinc_context(), master_opengl_widget)
        main_view.register_view('OrthographicPlus', widget,
                                   'Zinc Orthographic+ view',
                                   'Set the current view to the Zinc orthographic+ view')

