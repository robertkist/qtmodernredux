import sys
from typing import Any
from PySide2.QtCore import QRectF, QRect
from PySide2.QtWidgets import QMessageBox, QLabel
from PySide2.QtGui import Qt, QColor, QPainter, QPen, QPaintEvent, QFontMetrics, QBrush


__author__ = "Robert Kist"


QDIALOG_TYPES = (QMessageBox)
WINDOW_BUTTONS_RIGHT: str = 'window_buttons_right'
WIDTH_PADDING_PX = 3  # add 2 pixel padding to width of titlebar text
DEBUG = False


class WindowTitleLabel(QLabel):
    """Implements a label for window titles"""

    def __init__(self,
                 text: str,
                 height: int,
                 color: QColor,
                 parent: Any,
                 window_buttons_position: str,
                 button_bar_width: int,
                 minimum_width: int,
                 margin: int) -> None:
        """
        Constructor
        test: titlebar text
        height: titlebar height in pixels
        color: titlebar text color
        parent: parent widget
        window_buttons_position: WINDOW_BUTTONS_RIGHT or WINDOW_BUTTONS_RIGHT
        button_bar_width: combined width of all buttons in pixels
        minimum_width:
        right_margin:
        """
        super().__init__(parent)
        self.__original_text: str = text
        self.__ofs_y: float = height / 2.0
        self.__font_pen: QPen = QPen(color)
        self.__br_height: int = 0
        self.__window_buttons_position: str = window_buttons_position
        self.__margin: int = margin
        self.__button_bar_width: int = button_bar_width + margin
        self.setText(text)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setMinimumWidth(minimum_width)

    def paintEvent(self, _: QPaintEvent) -> None:
        """Qt Paint Event: ensures the title-bar text is elided properly and stays centered"""
        painter = QPainter()
        painter.begin(self)
        painter.setPen(self.__font_pen)

        # bold font for macOS window titles
        font = self.font()
        if sys.platform in ["darwin", "linux"]:
            font.setBold(True)
        font_metrics = QFontMetrics(font)

        # calculate text properties
        text_width: int = self.width() - self.__button_bar_width - self.__margin
        text: str = font_metrics.elidedText(self.__original_text, Qt.ElideRight, text_width)

        # calculate height
        br: QRect = font_metrics.boundingRect(text)
        if br.height() > 0:
            self.__br_height = br.height()
        py = self.__ofs_y - self.__br_height / 2.0
        br_width = br.width()

        # calculate width
        px = (self.width() - br_width - WIDTH_PADDING_PX) / 2.0
        if px < self.__button_bar_width:
            if self.__window_buttons_position == WINDOW_BUTTONS_RIGHT:
                if text != self.__original_text:
                    px = self.__margin
                else:
                    px = px - (self.__button_bar_width - px)
            else:
                px = self.__button_bar_width

        # draw title
        rect = QRectF(px, py, br_width + WIDTH_PADDING_PX, self.__br_height)
        painter.setFont(font)
        if DEBUG:
            painter.setBrush(QBrush(QColor('#ff0000')))
            painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignLeft, text)

    def setWindowTitle(self, title: str) -> None:
        """Sets the Window title string"""
        self.__original_text = title
        self.update()
