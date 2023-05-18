import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QMovie, Qt
from qtmodernredux6 import QtModernRedux


"""
This example demonstates using a QMovie inside a QtModernRedux window.
"""


__author__ = "Robert Kist"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        lbl = QLabel(self)
        movie = QMovie('../example_data/sample.gif')
        lbl.setMovie(movie)
        lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        movie.start()
        self.setCentralWidget(lbl)


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWindow(),
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.show()
    sys.exit(app.exec())
