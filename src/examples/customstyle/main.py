import sys
from PySide2.QtWidgets import QMainWindow, QMessageBox
from qtmodernredux import QtModernRedux
from mainwindow_ui import Ui_MainWindow


"""
This example demonstates how user-defined custom styles can be used with QtModernRedux.
The new custom style lives entirely in the 'wow_style' sub-directory.
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
        retval = msg.exec_()
        print("value of pressed message box button:", retval)


if __name__ == "__main__":
    from wow_style import Style

    app = QtModernRedux.QApplication(sys.argv, style=Style)
    mw = QtModernRedux.wrap(MainWindow(),
                            titlebar_height=40,
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.show()
    sys.exit(app.exec_())
