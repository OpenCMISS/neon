
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication

from opencmiss.neon.settings import application_name, organization_name, organization_domain
from opencmiss.neon.view import MainWindow


def main():
    QApplication.setOrganizationName(organization_name)
    QApplication.setOrganizationDomain(organization_domain)
    QApplication.setApplicationName(application_name)
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
