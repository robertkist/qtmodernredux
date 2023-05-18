import sys
import time
from ffpyplayer.player import MediaPlayer
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QImage, QPixmap, Qt
from qtmodernredux import QtModernRedux


"""
This example demonstrates an alternative media playback control (ffpyplayer) which can be used instead
of QMediaPlayer, which not only offers wider video format support, but also better compatibility with
QtModernRedux. 
"""


__author__ = "Robert Kist"


# https://stackoverflow.com/questions/59611075/how-would-i-go-about-playing-a-video-stream-with-ffpyplayer
# https://www.ffmpeg.org/ffmpeg-protocols.html

class MainWindow(QMainWindow):
    pass

    def __init__(self):
        super().__init__()
        self.player = None
        self.setWindowTitle("FFPyPlayer Test")

    def showEvent(self, e):
        self.timer_id = self.startTimer(1)
        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)

    def timerEvent(self, event) -> None:
        self.killTimer(self.timer_id)
        ff_opts = {'paused': False, 'autoexit': True}
        self.player = MediaPlayer('../example_data/sample.mp4', ff_opts=ff_opts, lib_opts={})
        # self.player = MediaPlayer('http://localhost:1441/sample_stream.mp4', ff_opts=ff_opts, lib_opts={})
        self.running = True
        while self.running:
            time.sleep(0.01)
            frame, val = self.player.get_frame()
            if val == 'eof':
                break
            if frame is None:
                time.sleep(0.01)
            else:
                img, t = frame
                data = img.to_bytearray()[0]
                width, height = img.get_size()
                # the technical name for the 'rgb24' default pixel format is RGB888,
                # which is QImage.Format_RGB888 in the QImage format enum
                qimage = QImage(data, width, height, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimage)
                pixmap = pixmap.scaled(self.lbl.width(), self.lbl.height(),
                                       Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.lbl.setPixmap(pixmap)
                time.sleep(val)
            QApplication.processEvents()

    def closeEvent(self, event) -> None:
        self.running = False
        if self.player is not None:
            self.player.set_pause(True)
            self.player.close_player()


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWindow(),
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.show()
    sys.exit(app.exec())


