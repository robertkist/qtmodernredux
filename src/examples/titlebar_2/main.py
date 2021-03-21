import sys
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QColor
from qtmodernredux import QtModernRedux
from mainwindow_ui import Ui_MainWindow


"""
This example demonstrates a custom titlebar with multiple widgets.
Each widget that should appear in the titlebar must be placed into a container QWidget - in this example
this is 'self.__ui.title_widget'. QtModernRedux will then ensure that this widget and its children fit
properly into the titlebar. Be aware that you till have to specify the titlebar's height! Getting this right
may take a few tries. However, when using styled widgets, the titlebar will look the same on all supported
platforms.
"""


__author__ = "Robert Kist"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Constructor"""
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

    @property
    def title_widget(self):
        """Expose the titlebar widget so it can be styled"""
        return self.__ui.title_widget


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    main_window = MainWindow()
    modern_window = QtModernRedux.wrap(main_window,
                                       title_bar=False,  # disable standard titlebar
                                       titlebar_height=42,
                                       titlebar_color=QColor('#0076d2'),  # color when window is active
                                       titlebar_nofocus_color=QColor('#555555'),  # color when window is in-active
                                       titlebar_widget=main_window.title_widget,  # widget to put into the titlebar
                                       window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    modern_window.show()
    sys.exit(app.exec_())
