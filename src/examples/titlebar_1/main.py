import sys
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QColor
from qtmodernredux import QtModernRedux
from mainwindow_ui import Ui_MainWindow


"""
This example demonstrates a custom titlebar with a tab bar, such as features in many popular web-browsers.
"""


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Constructor"""
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.tabWidget.setTabsClosable(True)
        self.__ui.tabWidget.setMovable(True)

    @property
    def tab_widget(self):
        """Expose the titlebar tab widget so it can be styled"""
        return self.__ui.tabWidget


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    main_window = MainWindow()
    modern_window = QtModernRedux.wrap(main_window,
                                       title_bar=False,
                                       titlebar_height=40,
                                       titlebar_color=QColor('#0076d2'),
                                       titlebar_nofocus_color=QColor('#ff0000'),
                                       titlebar_widget=main_window.tab_widget,
                                       window_buttons_position=QtModernRedux.WINDOW_BUTTONS_LEFT)
    modern_window.show()
    sys.exit(app.exec_())
