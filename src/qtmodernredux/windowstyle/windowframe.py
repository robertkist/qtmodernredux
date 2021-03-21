from typing import Any
from PySide2.QtCore import QRect, Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import Qt, QColor, QPainter, QPen, QBrush, QPaintEvent, QMouseEvent


__author__ = "Robert Kist"


class WindowFrame(QWidget):
    """Implements a Qt 'windowFrame' widget"""
    double_clicked = Signal()

    def __init__(self,
                 titlebar_height: int,
                 titlebar_color: QColor,
                 background_color: QColor,
                 corner_radius: int,
                 parent: Any) -> None:
        """Constructor"""
        super().__init__(parent)
        self.__titlebar_height: int = titlebar_height
        self.__background_color: QColor = QColor(background_color)
        self.__titlebar_color: QColor = QColor(titlebar_color)
        self.__corner_radius: int = corner_radius

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        """Qt Mouse-Double-Click Event: Window dragging"""
        if event.pos().y() <= self.__titlebar_height + 1:
            self.double_clicked.emit()  # type: ignore

    def set_background_color(self, color: QColor) -> None:
        """Sets the titlebar's background color"""
        self.__titlebar_color = color

    def paintEvent(self, _: QPaintEvent) -> None:
        """Qt Paint Event"""
        w: int = self.width()
        h: int = self.__titlebar_height
        p: QPainter = QPainter(self)
        p.setPen(QPen(self.__background_color))
        p.setBrush(QBrush(self.__background_color))
        p.drawRoundedRect(QRect(0, 0, w, self.height()), self.__corner_radius, self.__corner_radius)
        p.setPen(QPen(Qt.transparent))
        p.setBrush(QBrush(self.__titlebar_color))
        p.drawRoundedRect(QRect(0, 0, w, h), self.__corner_radius, self.__corner_radius)
        p.drawRect(QRect(0, self.__corner_radius, w, h - self.__corner_radius))
