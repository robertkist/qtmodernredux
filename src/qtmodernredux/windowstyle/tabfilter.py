from PySide2.QtWidgets import QWidget, QTabBar
from PySide2.QtCore import QObject, QEvent, QPoint


__author__ = "Robert Kist; Jean-Sébastien Gosselin"


class TabFilter(QObject):
    """
    This event filter prevents the right most tab in a QTabWidget to be moved.
    It also prevents other tabs from switching position with the last tab.
    Adapted from: https://stackoverflow.com/questions/31845768/pyside-qt4-qtabwidget-disable-drag-and-drop-of-a-single-q-tab-widget
    """

    def __init__(self, tab_bar: QTabBar) -> None:
        """Constructor"""
        super().__init__()
        self.tab_bar: QTabBar = tab_bar
        self.tab_bar.edge_offset = None

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        """Method which applies the event filter"""
        if event.type() == QEvent.Type.MouseMove and self.tab_bar.edge_offset is not None:
            if source.currentIndex() == self.tab_bar.count() - 1:  # Block MouseMove for last tab
                return True
            # For remaining tabs:
            # block MouseMove if the left edge of the moving tab goes
            # farther to the left than the right edge of first tab.
            moving_right_edge: int = event.pos().x() + self.tab_bar.edge_offset
            fixed_left_edge: int = self.tab_bar.tabRect(self.tab_bar.count() - 1).x()
            if moving_right_edge > fixed_left_edge:
                return True
        elif event.type() == QEvent.Type.MouseButtonPress:
            # Get mouse click horizontal position.
            xclick: QPoint = event.pos().x()
            # Get the left edge horizontal position of the targeted tab.
            xleft: int = self.tab_bar.tabRect(self.tab_bar.tabAt(event.pos())).x()
            # Compute and store offset between mouse click horizontal
            # position and the left edge of the targeted tab
            self.tab_bar.edge_offset = xclick - xleft
            self.tab_bar.edge_offset = self.tab_bar.tabRect(self.tab_bar.tabAt(event.pos())).width() - (xclick - xleft)
        return QWidget.eventFilter(self, source, event)
