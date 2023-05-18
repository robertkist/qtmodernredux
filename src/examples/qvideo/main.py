import sys
from PySide6.QtCore import QUrl, QFileInfo
from PySide6.QtWidgets import QMainWindow
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from qtmodernredux6 import QtModernRedux


"""
This example demonstates the feature to turn off window transparency.
By default, QtModernRedux tells Qt to create a transparent window, that supports anti-aliased rounded corners
and drop-shadow effects. On some platforms, such as Windows, this conflicts with the QMediaPlayer component.

In this case, it is possible to tell QtModernRedux to use an alternative method to draw the windows.
This window still has rounded corners, but they are not as nice, and the drop shadow is also not supported.
This is achieved via the 'transparent_window' parameter of the QtModernRedux.wrap() method.
"""


__author__ = "Robert Kist"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 400)
        self.media_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.setCentralWidget(self.video_widget)

    def showEvent(self, event) -> None:
        media_content = QUrl.fromLocalFile(QFileInfo('./../example_data/sample.mp4').absoluteFilePath())
        self.media_player.setSource(media_content)
        self.media_player.setVideoOutput(self.video_widget)
        self.video_widget.show()
        self.video_widget.update()
        self.media_player.setPosition(0)
        self.media_player.play()


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWindow(),
                            title_bar=True,
                            transparent_window=False,
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.show()
    sys.exit(app.exec())
