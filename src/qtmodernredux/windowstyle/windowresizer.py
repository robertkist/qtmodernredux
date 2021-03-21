from typing import Optional, Any, Tuple, Dict
from PySide2.QtCore import Signal, QPoint, QRect
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import Qt, QMouseEvent, QCursor


__author__ = "Robert Kist"


DEBUG = False  # makes the resize handles opaque and colors them red and green


class Resizer(QLabel):
    """
    This class implements a Resize Handle. Resize handles can be placed at 8 cardinal dimensions
    of each Window.
    * at the sides: North, South, East, West
    * at the corners: North-East, South-East, South-West, North-West
    """
    LEFT = 'l'
    TOP = 't'
    RIGHT = 'r'
    BOTTOM = 'b'
    TOP_LEFT = 'tl'
    TOP_RIGHT = 'tr'
    BOTTOM_LEFT = 'bl'
    BOTTOM_RIGHT = 'br'
    move_signal = Signal(object)

    def __init__(self, parent: Any, type_: str, radius: int) -> None:
        """Constructor"""
        super().__init__(parent)
        self.__parent = parent
        self.setMouseTracking(True)
        self.__radius: int = radius
        if DEBUG:
            if type_ in [self.LEFT, self.RIGHT, self.TOP, self.BOTTOM]:
                self.setStyleSheet('background: #ff0000;')
            else:
                self.setStyleSheet('background: #00ff00;')
        self.__old_cursor: QCursor = self.cursor()
        self.__in: bool = False
        if not DEBUG:
            self.setAttribute(Qt.WA_TranslucentBackground)
        cursors: Dict[str, Any] = {
            self.LEFT: Qt.SizeHorCursor,
            self.TOP: Qt.SizeVerCursor,
            self.RIGHT: Qt.SizeHorCursor,
            self.BOTTOM: Qt.SizeVerCursor,
            self.TOP_LEFT: Qt.SizeFDiagCursor,
            self.TOP_RIGHT: Qt.SizeBDiagCursor,
            self.BOTTOM_LEFT: Qt.SizeBDiagCursor,
            self.BOTTOM_RIGHT: Qt.SizeFDiagCursor,
        }
        self.__type: str = type_
        self.setCursor(cursors[type_])
        self.__mouse_pressed: bool = False
        self.__mouse_pos: Optional[QPoint] = None
        self.__window_width: Optional[QPoint] = None
        self.__window_height: Optional[QPoint] = None
        self.__window_pos: Optional[QPoint] = None
        self.__window_geometry_x: int = 0
        self.__window_geometry_y: int = 0
        self.__window_pos_x: int = 0
        self.__window_pos_y: int = 0
        self.__window_geometry_width: int = 0
        self.__window_geometry_height: int = 0

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Qt Mouse-Press Event"""
        self.__mouse_pressed = True
        self.__mouse_pos = event.globalPos()
        if self.__type == self.TOP:
            self.__window_pos_y = self.__parent.pos().y()
            self.__window_geometry_x = self.__parent.geometry().x()
        elif self.__type in [self.BOTTOM, self.RIGHT, self.BOTTOM_RIGHT]:
            self.__window_geometry_x = self.__parent.geometry().x()
            self.__window_geometry_y = self.__parent.geometry().y()
        elif self.__type == self.LEFT:
            self.__window_pos_x = self.__parent.pos().x()
            self.__window_geometry_y = self.__parent.geometry().y()
        elif self.__type in [self.TOP_LEFT, self.TOP_RIGHT, self.BOTTOM_LEFT]:
            self.__window_pos_x = self.__parent.pos().x()
            self.__window_pos_y = self.__parent.pos().y()
        self.__window_geometry_width = self.__parent.geometry().width()
        self.__window_geometry_height = self.__parent.geometry().height()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Qt Mouse-Move Event"""

        def get_top_resize_values() -> Tuple[int, int]:
            """calculates vertial position and height"""
            py: int = (event.globalPos() - self.__mouse_pos).y()
            if self.__window_geometry_height - py < self.__parent.minimumSize().height():
                height: int = self.__parent.minimumSize().height()
                pos_y: int = self.__window_pos_y + self.__window_geometry_height - height
            else:
                height = self.__window_geometry_height - py
                pos_y = self.__window_pos_y + py
            return pos_y, height

        def get_left_resize_values() -> Tuple[int, int]:
            """calculates horizontal position and width"""
            px: int = (event.globalPos() - self.__mouse_pos).x()
            if self.__window_geometry_width - px < self.__parent.minimumSize().width():
                width: int = self.__parent.minimumSize().width()
                pos_x: int = self.__window_pos_x + self.__window_geometry_width - width
            else:
                width = self.__window_geometry_width - px
                pos_x = self.__window_pos_x + px
            return pos_x, width

        if self.__mouse_pressed:
            if self.__type == self.BOTTOM:
                py = (event.globalPos() - self.__mouse_pos).y()
                geometry = QRect(self.__window_geometry_x,
                                 self.__window_geometry_y,
                                 self.__window_geometry_width,
                                 self.__window_geometry_height + py)
            elif self.__type == self.RIGHT:
                px = (event.globalPos() - self.__mouse_pos).x()
                geometry = QRect(self.__window_geometry_x,
                                 self.__window_geometry_y,
                                 self.__window_geometry_width + px,
                                 self.__window_geometry_height)
            elif self.__type == self.TOP:
                pos_y, height = get_top_resize_values()
                geometry = QRect(self.__window_geometry_x, pos_y, self.__window_geometry_width, height)
            elif self.__type == self.LEFT:
                pos_x, width = get_left_resize_values()
                geometry = QRect(pos_x, self.__window_geometry_y, width, self.__window_geometry_height)
            elif self.__type == self.TOP_LEFT:
                pos_x, width = get_left_resize_values()
                pos_y, height = get_top_resize_values()
                geometry = QRect(pos_x, pos_y, width, height)
            elif self.__type == self.TOP_RIGHT:
                px = (event.globalPos() - self.__mouse_pos).x()
                pos_y, height = get_top_resize_values()
                geometry = QRect(self.__window_pos_x, pos_y, self.__window_geometry_width + px, height)
            elif self.__type == self.BOTTOM_LEFT:
                pos_x, width = get_left_resize_values()
                py = (event.globalPos() - self.__mouse_pos).y()
                geometry = QRect(pos_x, self.__window_pos_y, width, self.__window_geometry_height + py)
            elif self.__type == self.BOTTOM_RIGHT:
                px = (event.globalPos() - self.__mouse_pos).x()
                py = (event.globalPos() - self.__mouse_pos).y()
                geometry = QRect(self.__window_geometry_x,
                                 self.__window_geometry_y,
                                 self.__window_geometry_width + px,
                                 self.__window_geometry_height + py)
            if geometry.width() < self.__parent.minimumSize().width():
                geometry.setWidth(self.__parent.minimumSize().width())
            if geometry.height() < self.__parent.minimumSize().height():
                geometry.setHeight(self.__parent.minimumSize().height())
            self.__parent.setGeometry(geometry)
            self.adjust_resizers(geometry)

    def adjust_resizers(self, geometry: QRect) -> None:
        """Top, Left, Right, Bottom resizers are 4 px wide, corner resizers are 8x8 pixels"""
        radius: int = self.__radius if self.__parent.use_shadow and not self.__parent.maximized else 0
        cr = QRect(0 + radius,
                   0 + radius,
                   geometry.width() - radius * 2,
                   geometry.height() - radius * 2)
        r_width: int = 4  # resizer width/height
        c_width: int = 8  # corner width/height
        crx: int = cr.x()
        cry: int = cr.y()
        crw: int = cr.width()
        crw_sr: int = crw + radius - r_width
        crh: int = cr.height()
        crh_sr: int = crh + radius - r_width
        self.__parent.resizer_top.setGeometry(crx + c_width, cry, crw - c_width * 2, r_width)
        self.__parent.resizer_bot.setGeometry(crx + c_width, crh_sr, crw - c_width * 2, r_width)
        self.__parent.resizer_lef.setGeometry(crx, cry + c_width, r_width, crh - c_width * 2)
        self.__parent.resizer_rig.setGeometry(crw_sr, cry + c_width, r_width, crh - c_width * 2)
        self.__parent.resizer_tr.setGeometry(crw - c_width + radius, cry, c_width, c_width)
        self.__parent.resizer_br.setGeometry(crw - c_width + radius, crh - c_width + radius, c_width, c_width)
        self.__parent.resizer_bl.setGeometry(crx, crh - c_width + radius, c_width, c_width)
        self.__parent.resizer_tl.setGeometry(crx, cry, c_width, c_width)

    def mouseReleaseEvent(self, _: QMouseEvent) -> None:
        """Qt Mouse-Release Event"""
        self.__mouse_pressed = False
