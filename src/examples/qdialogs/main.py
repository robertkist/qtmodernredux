import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from qtmodernredux6 import QtModernRedux
from mainwindow_ui import Ui_MainWindow


"""
This example demonstates various styled QMessageBox dialogs, using enhanced notification icons,
suitable for HighDPI and Retina displays. 
This example also demonstrates setting an icon for the application.
"""


__author__ = "Robert Kist"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setWindowTitle('QDialog Test')
        self.__ui.msgWarning.clicked.connect(self.show_warning_msgbox)
        self.__ui.msgCritical.clicked.connect(self.show_critical_msgbox)
        self.__ui.msgQuestion.clicked.connect(self.show_question_msgbox)
        self.__ui.msgInformation.clicked.connect(self.show_information_msgbox)
        self.__ui.msgNoIcon.clicked.connect(self.show_regular_msgbox)

    def show_warning_msgbox(self):
        self.show_msg_box(QMessageBox.Warning)

    def show_critical_msgbox(self):
        self.show_msg_box(QMessageBox.Critical)

    def show_question_msgbox(self):
        self.show_msg_box(QMessageBox.Question)

    def show_information_msgbox(self):
        self.show_msg_box(QMessageBox.Information)

    def show_regular_msgbox(self):
        self.show_msg_box(QMessageBox.NoIcon)

    def show_msg_box(self, icon):
        msg = QtModernRedux.wrap(QMessageBox(self), parent=self, window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
        msg.setIcon(icon)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        retval = msg.exec()
        print("value of pressed message box button:", retval)


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWindow(),
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.setWindowIcon(QIcon("../example_data/sample.png"))
    mw.show()
    sys.exit(app.exec())
