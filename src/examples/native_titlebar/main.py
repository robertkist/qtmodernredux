import sys
from PySide2.QtWidgets import QMainWindow
from qtmodernredux import QtModernRedux
from mainwindow_ui import Ui_MainWindow


"""
This example demonstrates all the styled widgets supported by QtModernRedux. 
"""


__author__ = "Robert Kist"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWindow(), native_window=True)  # enable native titlebar
    mw.show()
    sys.exit(app.exec_())
