
from PySide2.QtWidgets import QAction

from opencmiss.neon.extensions.handlers.base import BaseOpenGLHandler


class ZincView(BaseOpenGLHandler):

    @staticmethod
    def instantiate(main_view, cls, master_opengl_widget):
        stacked_widget = main_view.get_stacked_widget()
        view_menu_index = stacked_widget.count()
        stacked_widget.addWidget(cls(main_view.get_zinc_context(), master_opengl_widget))
        view_menu = main_view.get_view_menu()

        zinc_scene_action = QAction('&Zinc basic view', main_view)
        zinc_scene_action.setStatusTip('Set the current view to the Zinc basic view')
        zinc_scene_action.triggered.connect(main_view.view_change_triggered)
        main_view.register_view_change_pair((zinc_scene_action, view_menu_index))

        view_menu.addAction(zinc_scene_action)

        main_view.update_view_menu_ui()


class ZincOrthographicPlusView(BaseOpenGLHandler):

    @staticmethod
    def instantiate(main_view, cls, master_opengl_widget):
        stacked_widget = main_view.get_stacked_widget()
        view_menu_index = stacked_widget.count()
        stacked_widget.addWidget(cls(main_view.get_zinc_context(), master_opengl_widget))
        view_menu = main_view.get_view_menu()

        zinc_scene_action = QAction('&Zinc Orthographic+ view', main_view)
        zinc_scene_action.setStatusTip('Set the current view to the Zinc orthographic+ view')
        zinc_scene_action.triggered.connect(main_view.view_change_triggered)
        main_view.register_view_change_pair((zinc_scene_action, view_menu_index))

        view_menu.addAction(zinc_scene_action)

        main_view.update_view_menu_ui()
