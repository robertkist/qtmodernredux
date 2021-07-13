import sys
from typing import Any, Optional, Union
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtCore import Slot, Signal, QEvent, QObject, QPoint, QRectF, QRect
from PySide2.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QToolButton, QGridLayout, QMessageBox, \
    QGraphicsDropShadowEffect, QDialog, QInputDialog, QApplication, QTabWidget, QTabBar, QLayout
from PySide2.QtGui import Qt, QCloseEvent, QRegion, QPainterPath, QMouseEvent, QColor, QResizeEvent, QPixmap, QPainter, \
    QShowEvent, QIcon, QKeyEvent
from qtmodernredux.windowstyle.windowresizer import Resizer
from qtmodernredux.windowstyle.windowtitlelabel import WindowTitleLabel
from qtmodernredux.windowstyle.windowframe import WindowFrame
from qtmodernredux.windowstyle.tabfilter import TabFilter


__author__ = "Robert Kist; Gerard Marull-Paretas (window maximize/minimize code)"


# list of supported dialogs, other than QDialog:
QDIALOG_TYPES = (QMessageBox, QInputDialog)
# when CENTER_MAINWINDOW is true, windows which have a position of 0/0 will be centered on the screen
CENTER_MAINWINDOW: bool = True
# centers child windows relative to their parent
ALIGN_CHILD_WINDOWS: bool = True


WINDOW_BUTTONS_RIGHT: str = 'window_buttons_right'
WINDOW_BUTTONS_LEFT: str = 'window_buttons_left'


class ModernWindow(QDialog):
    """
    Implements a modern window-frame.
    Notes:
        * Except for macOS, the OS will not add a shadow to the window. On Windows and Linux this
          class will add QGraphicsDropShadowEffect to the entire window.
    """
    __double_clicked = Signal()

    def __init__(self,
                 window: Any,
                 parent: Optional[Any],
                 style: Optional[Any],
                 title_bar: bool,
                 transparent_window: bool,
                 titlebar_height: Optional[int],
                 titlebar_color: Optional[QColor],
                 titlebar_nofocus_color: Optional[QColor],
                 titlebar_text_color: Optional[QColor],
                 titlebar_widget: Optional[Union[QWidget, QTabWidget]],
                 window_buttons_position: Optional[str]) -> None:
        """
        Constructor.
        Parameters:
         * window: Qt widget that should be wrapped
         * window_style: choose from one of the pre-defined styles, e.g. 'APL', 'WOW'
         * title_bar: display a traditional titlebar or not
         * titlebar_height: height of the titlebar in pixel
         * titlebar_color: override background color of the titlebar
         * titlebar_nofocus_color: override background color of the titlebar when the window is out of focus
         * titlebar_text_color: override color for the window title text
         * window_button_position: positions the window close/min/max buttons left (macOS) or right of the window title
           (Windows, Gnome, KDE, etc.)
         * transparent_window: turns off window transparency. This ensures compatibility with certain widgets and draw
           modes, such as QMediaWidget on Windows. Drawbacks: when transparent_window is False, window drop shadow
           effects will be disabled, except for operating systems that automatically add a drop shadow to all windows.
        """

        def expose_msgbox_methods() -> None:
            """ensure Qt methods of wrapped children are exposed"""
            assert self.__window is not None
            self.setText = self.__window.setText
            self.setInformativeText = self.__window.setInformativeText
            self.setDetailedText = self.__window.setDetailedText

        def add_window_buttons() -> None:
            """create window widget buttons"""
            button_size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            if not isinstance(self.__window, QDIALOG_TYPES):
                self._minimize_button = QToolButton(self)
                self._minimize_button.setObjectName('btnMinimize')
                self._minimize_button.setSizePolicy(button_size_policy)
                self._minimize_button.clicked.connect(self.__on_minimize_button_clicked)  # pylint: disable=no-member
                self._restore_button = QToolButton(self)
                self._restore_button.setObjectName('btnRestore')
                self._restore_button.setSizePolicy(button_size_policy)
                self._restore_button.clicked.connect(self.__on_restore_button_clicked)  # pylint: disable=no-member
                self._maximize_button = QToolButton(self)
                self._maximize_button.setObjectName('btnMaximize')
                self._maximize_button.setSizePolicy(button_size_policy)
                self._maximize_button.clicked.connect(self.__on_maximize_button_clicked)  # pylint: disable=no-member
            self._close_button = QToolButton(self)
            self._close_button.setObjectName('btnClose')
            self._close_button.setSizePolicy(button_size_policy)
            self._close_button.clicked.connect(self.__on_close_button_clicked)  # pylint: disable=no-member
            self.__move_window_buttons()  # place buttons

        def set_window_properties(titlebar_height: int) -> None:
            """Sets Qt Properties for the wrapper window"""
            assert self.__window is not None
            self.setStyleSheet(self.__style.get_window_stylesheet())
            self.setWindowFlags(Qt.Window |
                                Qt.FramelessWindowHint |
                                Qt.WindowSystemMenuHint |
                                Qt.WindowCloseButtonHint |
                                Qt.WindowMinimizeButtonHint |
                                Qt.WindowMaximizeButtonHint)
            if sys.platform not in ["darwin"] and self.__transparent_window:
                self.setAttribute(Qt.WA_TranslucentBackground, True)  # no need for translucency on macOS
            if sys.platform == 'win32':
                self.setAttribute(Qt.WA_OpaquePaintEvent, True)  # avoid flickering on window resize on Windows
            else:
                self.setAttribute(Qt.WA_OpaquePaintEvent, False)
            self.setAttribute(Qt.WA_NoSystemBackground, True)
            self.setWindowTitle(self.__window.windowTitle())
            self.setGeometry(self.__window.geometry())
            height = titlebar_height
            if self.__use_shadow:
                height += self.__style.window.SHADOW_RADIUS_PX * 2
            self.setMinimumHeight(self.__window.minimumSizeHint().height() + height)
            self.setMinimumWidth(self.__window.minimumSizeHint().width())

        def add_window_drop_shadow() -> None:
            """Adds a drop-shadow behind the window"""
            if self.__use_shadow:
                self.layout().setMargin(self.__style.window.SHADOW_RADIUS_PX)
                drop_shadow_effect = QGraphicsDropShadowEffect(self)
                drop_shadow_effect.setEnabled(True)
                drop_shadow_effect.setBlurRadius(self.__style.window.SHADOW_RADIUS_PX)
                color = QColor(self.__style.window.SHADOW_COLOR_RGB)
                color.setAlpha(self.__style.window.SHADOW_OPACITY_HEX)
                drop_shadow_effect.setColor(color)
                drop_shadow_effect.setOffset(0)
                self.setGraphicsEffect(drop_shadow_effect)

        def adjust_wrapped_window_object() -> None:
            """Adding attribute to clean up the parent window when the child is closed"""
            assert self.__window is not None
            self.__window.wrapper = self
            self.__window.setAttribute(Qt.WA_DeleteOnClose, True)
            self.__window.destroyed.connect(self.__child_was_closed)

        def add_resizers() -> None:
            """Adds resizer widgets, which act as resize handles, to the window wrapper"""
            if isinstance(window, QDIALOG_TYPES):
                assert self.__window is not None
                self.__window.installEventFilter(self)
            else:
                self.resizer_top = Resizer(self, Resizer.TOP, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_bot = Resizer(self, Resizer.BOTTOM, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_lef = Resizer(self, Resizer.LEFT, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_rig = Resizer(self, Resizer.RIGHT, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_tl = Resizer(self, Resizer.TOP_LEFT, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_tr = Resizer(self, Resizer.TOP_RIGHT, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_br = Resizer(self, Resizer.BOTTOM_RIGHT, self.__style.window.SHADOW_RADIUS_PX)
                self.resizer_bl = Resizer(self, Resizer.BOTTOM_LEFT, self.__style.window.SHADOW_RADIUS_PX)

        def get_window_frame_widget(window_buttons_position: str) -> WindowFrame:
            """Returns a widget which acts as Qt 'windowFrame' element"""
            window_frame_widget = WindowFrame(titlebar_height=self.__titlebar_height,
                                              titlebar_color=self.__titlebar_color,
                                              background_color=self.__style.window.WINDOW_BACKGROUND_RGB,
                                              corner_radius=self.__style.window.WINDOW_CORNER_RADIUS_PX,
                                              parent=self)
            if not isinstance(window, QDIALOG_TYPES):
                window_frame_widget.double_clicked.connect(self.__on_title_bar_double_clicked)  # type: ignore
            window_frame_widget.setObjectName('windowFrame')
            self.__vbox_frame_layout = QVBoxLayout(window_frame_widget)
            self.__vbox_frame_layout.setContentsMargins(0, 0, 0, 0)
            self.__vbox_frame_layout.setSpacing(0)
            if self.__title_bar:  # add optional titlebar
                tcolor = QColor(self.__style.window.TITLE_BAR_FONT_COLOR_RGB)
                if titlebar_text_color is not None:
                    tcolor = titlebar_text_color
                self.__title_widget = WindowTitleLabel(text='',
                                                       height=self.__titlebar_height,
                                                       color=tcolor,
                                                       window_buttons_position=window_buttons_position,
                                                       margin=self.__style.window.TITLE_BAR_TITLE_TEXT_RIGHT_MARGIN_PX,
                                                       button_bar_width=self.window_buttons_width + self.window_buttons_margin,
                                                       minimum_width=self.__style.window.TITLE_LABEL_MINIMUM_WIDTH_PX,
                                                       parent=None)
                self.__title_widget.setMinimumHeight(self.__titlebar_height)
                self.__vbox_frame_layout.addWidget(self.__title_widget)
            else:  # no title-bar; add dummy widget to create a margin
                self.__title_widget = QWidget()
                self.__title_widget.setGeometry(0, 0, 1, self.__style.window.TITLE_BAR_TOP_MARGIN_PX)
                self.__title_widget.setMinimumHeight(self.__style.window.TITLE_BAR_TOP_MARGIN_PX)
                self.__vbox_frame_layout.addWidget(self.__title_widget)
            assert self.__window is not None
            self.__vbox_frame_layout.addWidget(self.__window)
            return window_frame_widget

        QDialog.__init__(self, parent)
        self.__style: Any = style
        if titlebar_height is None:
            titlebar_height = self.__style.window.TITLE_BAR_HEIGHT_PX
        assert window_buttons_position in [None, WINDOW_BUTTONS_LEFT, WINDOW_BUTTONS_RIGHT]
        if window_buttons_position is None:
            window_buttons_position = WINDOW_BUTTONS_LEFT if sys.platform == 'darwin' else WINDOW_BUTTONS_RIGHT
        self.__window: Optional[QWidget] = window
        self.__title_bar: bool = True if isinstance(self.__window, QDIALOG_TYPES) else title_bar
        self.__titlebar_height: int = titlebar_height
        self.__transparent_window: bool = transparent_window  # True if window uses WA_TranslucentBackground
        self.__use_shadow: bool = sys.platform != 'darwin' and transparent_window
        self.__maximized: bool = False
        self.__drag_move_enabled: bool = True
        self.__mouse_pressed: bool = False
        self.__mouse_pos: Optional[QPoint] = None
        self.__window_pos: Optional[QPoint] = None
        self.__window_buttons_width: int = 0
        self.__window_buttons_position: str = window_buttons_position
        self.__center_window_first_time: bool = True  # makes sure the window is only centered on 1st show event
        # create main contaner layout
        self.__vbox_master_layout = QGridLayout(self)
        self.__vbox_master_layout.setContentsMargins(0, 0, 0, 0)
        if titlebar_color is None:
            self.__titlebar_color: QColor = QColor(self.__style.window.TITLE_BAR_COLOR_RGB)
        else:
            self.__titlebar_color = titlebar_color
        if titlebar_nofocus_color is None:
            self.__titlebar_nofocus_color: QColor = QColor(self.__style.window.TITLE_BAR_NOFOCUS_COLOR_RGB)
        else:
            self.__titlebar_nofocus_color = titlebar_nofocus_color
        self.__window_frame_widget: WindowFrame = get_window_frame_widget(window_buttons_position=self.__window_buttons_position)
        self.__vbox_master_layout.addWidget(self.__window_frame_widget, 0, 0)
        # run window initialization methods
        add_resizers()
        if isinstance(self.__window, QMessageBox):
            expose_msgbox_methods()
        adjust_wrapped_window_object()
        add_window_drop_shadow()
        add_window_buttons()
        set_window_properties(self.__titlebar_height)
        # connect slot to detect if window/app loses focus
        app = QApplication.instance()
        app.focusChanged.connect(self.__app_focus_changed_slot)
        self.setFocus()
        self.layout().setSizeConstraint(QLayout.SetMinimumSize)  # ensure widgets cannot be resized below their min size
        # attributes for title-bar tab widget
        self.__tab_widget_dummy_close_button: Optional[QWidget] = None
        self.__tab_widget_filter: Optional[TabFilter] = None
        self.__tab_widget: Optional[QTabWidget] = None
        if titlebar_widget is not None:
            self.__adjust_title_tabwidget(titlebar_widget)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Ignore Escape key as it closes the window"""
        if event.key() != Qt.Key_Escape:
            super().keyPressEvent(event)

    # def keyPressEvent(self, e: QKeyPressEvent) -> None:
    #     """
    #     Example code for moving a window that has no titlebar between 2 screens with different
    #     scaling factors on Windows without any graphical artifacts.
    #     """
    #     scr = QApplication.instance().screens()
    #     if e.key() == Qt.Key_1:
    #         s = scr[0].availableSize()
    #         o = 0
    #     elif e.key() == Qt.Key_2:
    #         s = scr[1].availableSize()
    #         o = scr[1].availableSize().width()
    #     else:
    #         return
    #     size = self.size()
    #     pos = QPoint(s.width()/2 - self.width()/2 + o, s.height()/2 - self.height()/2)
    #     self.showMinimized()
    #     self.setGeometry(pos.x(), pos.y(), size.width(), size.height())
    #     self.showNormal()
    #     self.resize(size)

    def setWindowIcon(self, icon: Union[QIcon, QPixmap]) -> None:
        """Sets the window's window icon"""
        super().setWindowIcon(icon)
        if sys.platform == 'win32':  # make icon show up in taskbar on Windows
            import ctypes  # pylint: disable=import-outside-toplevel
            myappid: str = 'mycompany.qtmodern.redux.version'  # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # ############################################################
    # Properties
    # ############################################################

    def get_style(self) -> Any:
        """returns the class (static) which holds all the style's properties"""
        return self.__style

    @property
    def use_shadow(self) -> bool:
        """returns true if the window features a drop-shadow not generated by the OS or window manager"""
        return self.__use_shadow

    @property
    def maximized(self) -> bool:
        """Returns true if the window is maximzed"""
        return self.__maximized

    @property
    def titlebar_height(self) -> int:
        """Returns the title bar's height in pixels"""
        return self.__titlebar_height

    @property
    def window_buttons_width(self) -> int:
        """Returns the width of the area taken up by the titlebar buttons"""
        diameter: int = self.__style.window.TITLE_BAR_BUTTON_DIAMETER_PX
        spacing: int = self.__style.window.TITLE_BAR_BUTTON_SPACING_PX - diameter
        if not isinstance(self.__window, QDIALOG_TYPES):
            return spacing * 2 + diameter * 3
        return diameter

    @property
    def window_buttons_margin(self) -> int:
        """
        Returns the distance of the titlebar buttons from the left window edge.
        The maximum value is the distance of the buttons from the top edge, the minimum distance is defined in the
        window style. This value changes depending on the size of the window.
        """
        margin_y: int = int((self.__titlebar_height - self.__style.window.TITLE_BAR_BUTTON_DIAMETER_PX) / 2)
        min_margin: int = round(self.__style.window.TITLE_BAR_BUTTON_MIN_X_MARGIN_PX
                                if margin_y < self.__style.window.TITLE_BAR_BUTTON_MIN_X_MARGIN_PX else margin_y)
        return min_margin

    # ############################################################
    # Overloaded Qt methods
    # ############################################################

    def resizeEvent(self, r: QResizeEvent) -> None:
        """
        Qt Resize Event - does two things:
        1) applies rounded corners if window transparency has been disabled
        2) ensures resizer widgets and titlebar buttons stay in place
        TODO: the 'rounded_corner_px' value is harcoded. It relates to in '.TitleTabBar::tab' in
              widgetstyle/tabwidget_titlebar.py (border-width and border-image QSS attribute).
              Action: investigate a way so that this value doesn't have to be hard-coded.
        """
        # if transparency is turned off, set a mask for some basic rounded corners:
        if not self.__transparent_window and self.__style.window.WINDOW_CORNER_RADIUS_PX > 0:
            path = QPainterPath()
            path.addRoundedRect(QRectF(self.rect()),
                                self.__style.window.WINDOW_CORNER_RADIUS_PX + 1,  # add 1 to avoid drawing artifacts
                                self.__style.window.WINDOW_CORNER_RADIUS_PX + 1)
            reg = QRegion(path.toFillPolygon().toPolygon())
            self.setMask(reg)
        # adjust window button positions
        if not isinstance(self.__window, QDIALOG_TYPES):
            self.resizer_bl.adjust_resizers(self.geometry())  # adjusting one resizer adjusts all other resizers too
        if self.__window_buttons_position == WINDOW_BUTTONS_RIGHT:
            self.__move_window_buttons()
        # if a titlebar tab widget is set, mask it so that the empty area can be used to drag the window
        if self.__tab_widget is not None:
            width = 0
            tab_bar = self.__tab_widget.tabBar()
            for i in range(0, tab_bar.count() - 1):  # don't count invisible tab at end
                if tab_bar.isTabVisible(i):
                    width += tab_bar.tabRect(i).width()
            rounder_corner_px = 8  # TODO  # related to hardcoded border-image value in widgetstyle/tabwidget_titlebar.py
            r = QRect(0, 0, width + rounder_corner_px, self.__titlebar_height)
            self.__tab_widget.tabBar().setMask(r)

    def showEvent(self, _: QShowEvent) -> None:
        """
        Qt Show Event:
        * ensures resizers stay in place
        * ensures window is centered on screen or relative to their parent window
        """
        if not isinstance(self.__window, QDIALOG_TYPES):
            self.resizer_bl.adjust_resizers(self.geometry())  # adjusting one resizer adjusts all other resizers too
        parent = self.parent()
        # center MainWindow on screen
        if CENTER_MAINWINDOW:
            if parent is None and self.__center_window_first_time:  # type: ignore
                self.move(QApplication.desktop().screenGeometry(self).center() - self.rect().center())  # type: ignore
                self.__center_window_first_time = False  # only center the window on the initial show event
        # center dialogs relative to parent window
        if ALIGN_CHILD_WINDOWS and parent is not None:
            try:
                pos = parent.wrapper.pos()  # parent is wrapped in a QtModernRedux window
                width = parent.wrapper.width()
                height = parent.wrapper.height()
            except AttributeError:
                pos = parent.pos()  # parent isn't wrapped
                width = parent.width()
                height = parent.height()
            x = pos.x() + (width / 2 - self.width() / 2)
            y = pos.y() + (height / 2 - self.height() / 2)
            self.move(x, y)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Qt Close Event: Window close & cleanup"""
        if not self.__window:
            event.accept()
        else:
            self.__window.close()
            event.setAccepted(self.__window.isHidden())

    def eventFilter(self, target: QObject, event: QEvent) -> bool:
        """Qt Event Filter: This event filter is used when display QDialogs, such as message boxes."""
        # FOR MESSAGEBOX:
        if isinstance(event, QResizeEvent):
            assert self.__window is not None
            geometry = self.__window.geometry()
            if sys.platform in ['darwin']:
                self.setFixedSize(geometry.width() + self.__style.window.SHADOW_RADIUS_PX * 2,  # macOS, Windows (?)
                                  geometry.height() + self.__style.window.SHADOW_RADIUS_PX * 2)
            else:
                self.setFixedSize(geometry.width() + self.__style.window.SHADOW_RADIUS_PX * 2,
                                  geometry.height() + self.__style.window.SHADOW_RADIUS_PX * 2 + self.__titlebar_height)
            return True
        return QObject.eventFilter(self, target, event)

    def setIcon(self, icon: Any) -> None:
        """Qt setIcon: sets custom icons from the theme for QMessageBox"""
        if isinstance(self.__window, QMessageBox) and icon != QMessageBox.NoIcon:
            icons = {
                QMessageBox.Information: self.__style.window.MSGBOX_ICON_INFORMATION,
                QMessageBox.Question: self.__style.window.MSGBOX_ICON_QUESTION,
                QMessageBox.Warning: self.__style.window.MSGBOX_ICON_WARNING,
                QMessageBox.Critical: self.__style.window.MSGBOX_ICON_CRITICAL,
            }
            self.__window.setIconPixmap(self.__load_svg(icons[icon]))

    def setWindowTitle(self, title: str) -> None:
        """Qt setWindowTitle: ensures the titlebar displays the window title"""
        super().setWindowTitle(title)
        if self.__title_bar:
            self.__title_widget.setWindowTitle(title)

    def setWindowFlag(self, flag: Any, on: bool = True) -> None:
        """Qt setWindowFlag"""
        button_hints = [
            Qt.WindowCloseButtonHint,
            Qt.WindowMinimizeButtonHint,
            Qt.WindowMaximizeButtonHint
        ]
        if flag in button_hints:
            self.__set_window_button_state(flag, on)
        else:
            QWidget.setWindowFlag(self, flag, on)

    def setWindowFlags(self, flags: Any) -> None:
        """Qt setWindowFlags"""
        button_hints = [
            Qt.WindowCloseButtonHint,
            Qt.WindowMinimizeButtonHint,
            Qt.WindowMaximizeButtonHint
        ]
        for hint in button_hints:
            self.__set_window_button_state(hint, bool(flags & hint))
        QWidget.setWindowFlags(self, flags)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Qt Mouse-Press Event: Window dragging"""
        if not self.__drag_move_enabled:
            return
        radius = self.__style.window.SHADOW_RADIUS_PX if self.__use_shadow else 0
        ep = event.pos()
        if radius <= ep.y() <= self.__titlebar_height + radius + 1:
            epx = ep.x()
            if radius < epx < self.width() - radius:
                self.__mouse_pressed = True
                self.__mouse_pos = event.globalPos()
                self.__window_pos = self.pos()
                # self.__os = self.size()  # use when dragging between screens with different scale factors

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Qt Mouse-Move Event: Window dragging"""
        if self.__mouse_pressed and self.__drag_move_enabled:
            # CODE TO DETECT DISPLAY CHANGE
            # display = self.screen().virtualSiblingAt(event.globalPos()).name()
            # if display != self.__old_display:
            #     print('DISPLAY CHANGED TO %s' % display, self.__old_size)
            #     self.__old_display = display
            self.move(self.__window_pos + (event.globalPos() - self.__mouse_pos))

    def mouseReleaseEvent(self, _: QMouseEvent) -> None:
        """Qt Mouse-Release Event: Window dragging"""
        self.__mouse_pressed = False
        # self.resize(self.__os)  # use when dragging between screens with different scale factors

    # ############################################################
    # PRIVATE Custom methods
    # ############################################################

    def __move_window_buttons(self) -> None:
        """
        MacOS:
            * buttons are on the right side of the titlebar
            * order (left to right): close, minimize/restore, maximize
        Windows and most Linux:
            * buttons are on the left side of the titlebar
            * order (left to right): minimize/restore, maximize, close
        """
        # determine shadow radius
        radius: int = self.__style.window.SHADOW_RADIUS_PX
        if self.__use_shadow is False or self.__maximized:
            radius = 0
        # determine combined button width
        diameter = self.__style.window.TITLE_BAR_BUTTON_DIAMETER_PX
        spacing = self.__style.window.TITLE_BAR_BUTTON_SPACING_PX - diameter
        buttons_width: int = self.window_buttons_width
        # determine individual button positions
        margin_y: int = int((self.__titlebar_height - diameter) / 2)
        min_margin = self.window_buttons_margin
        if self.__window_buttons_position == WINDOW_BUTTONS_RIGHT:
            ofs_min = 0
            ofs_max = diameter + spacing
            if not isinstance(self.__window, QDIALOG_TYPES):
                ofs_close = (diameter + spacing) * 2
            else:
                ofs_close = 0
            margin_x: int = self.width() - buttons_width - min_margin - radius
        else:
            ofs_close = 0
            ofs_min = diameter + spacing
            ofs_max = (diameter + spacing) * 2
            margin_x = min_margin + radius
        # move buttons
        self._close_button.move(margin_x + ofs_close, margin_y + radius)
        if not isinstance(self.__window, QDIALOG_TYPES):  # no additional window buttons for message-boxes
            self._minimize_button.move(margin_x + ofs_min, margin_y + radius)
            self._restore_button.move(margin_x + ofs_max, margin_y + radius)
            self._maximize_button.move(margin_x + ofs_max, margin_y + radius)

    def __load_svg(self, svg_file: str) -> QPixmap:
        """Loads a SVG file and scales it correctly for High-DPI screens"""
        svg_renderer = QSvgRenderer(svg_file)
        pixmap = QPixmap(svg_renderer.defaultSize() * self.devicePixelRatio())
        pixmap.fill(Qt.transparent)
        painter = QPainter()
        painter.begin(pixmap)
        svg_renderer.render(painter)
        painter.end()
        pixmap.setDevicePixelRatio(self.devicePixelRatio())
        return pixmap

    def __show_resizers(self, show: bool) -> None:
        """Shows / hides the resizer widgets"""
        self.resizer_top.setVisible(show)
        self.resizer_bot.setVisible(show)
        self.resizer_lef.setVisible(show)
        self.resizer_rig.setVisible(show)
        self.resizer_tl.setVisible(show)
        self.resizer_tr.setVisible(show)
        self.resizer_bl.setVisible(show)
        self.resizer_br.setVisible(show)

    def __child_was_closed(self) -> None:
        """Wrapped window was closed"""
        self.__window = None  # The child was deleted, remove the reference to it and close the parent window
        self.close()

    def __set_window_button_state(self, hint: Any, state: Any) -> None:  # pylint: disable=too-many-branches
        """Adjusts button state (enabled/disabled) based on window status"""
        buttons = {Qt.WindowCloseButtonHint: self._close_button}
        if not isinstance(self.__window, QDIALOG_TYPES):
            buttons[Qt.WindowMinimizeButtonHint] = self._minimize_button
            buttons[Qt.WindowMaximizeButtonHint] = self._maximize_button
        button = buttons.get(hint)
        maximized = bool(self.windowState() & Qt.WindowMaximized)
        if not isinstance(self.__window, QDIALOG_TYPES):
            if button == self._maximize_button:  # special rules for max/restore
                self._restore_button.setEnabled(state)
                self._maximize_button.setEnabled(state)
                if maximized:
                    self._restore_button.setVisible(state)
                    self._maximize_button.setVisible(False)
                else:
                    self._maximize_button.setVisible(state)
                    self._restore_button.setVisible(False)
            elif button is not None:
                button.setEnabled(state)
        elif button is not None:
            button.setEnabled(state)
        all_buttons = [self._close_button]
        if not isinstance(self.__window, QDIALOG_TYPES):
            all_buttons.append(self._minimize_button)
            all_buttons.append(self._maximize_button)
            all_buttons.append(self._restore_button)
        if True in [button.isEnabled() for button in all_buttons]:
            for button in all_buttons:
                button.setVisible(True)
            if not isinstance(self.__window, QDIALOG_TYPES):
                if maximized:
                    self._maximize_button.setVisible(False)
                else:
                    self._restore_button.setVisible(False)
        else:
            for button in all_buttons:
                button.setVisible(False)

    @Slot()  # type: ignore
    def __on_minimize_button_clicked(self) -> None:
        """
        macOS workaround: Frameless windows cannot be minimized on macOS, therefore we need
        to reinstate the titlebar before we minimize the window. Once the window minimize
        command has been issued, we can hide the titlebar again.
        """
        if sys.platform == 'darwin':
            self.setWindowFlags(Qt.Window |
                                Qt.WindowSystemMenuHint |
                                Qt.WindowCloseButtonHint |
                                Qt.WindowMinimizeButtonHint |
                                Qt.WindowMaximizeButtonHint)
            self.show()
        self.setWindowState(Qt.WindowMinimized)
        self._minimize_button.setAttribute(Qt.WA_UnderMouse, False)  # prevent hover state form getting stuck
        if sys.platform == 'darwin':
            self.setWindowFlags(Qt.Window |
                                Qt.FramelessWindowHint |
                                Qt.WindowSystemMenuHint |
                                Qt.WindowCloseButtonHint |
                                Qt.WindowMinimizeButtonHint |
                                Qt.WindowMaximizeButtonHint)
            self.show()

    @Slot()  # type: ignore
    def __on_restore_button_clicked(self) -> None:
        """Restore button clicked"""
        if self._maximize_button.isEnabled() or self._restore_button.isEnabled():
            self._restore_button.setVisible(False)
            self._restore_button.setEnabled(False)
            self._maximize_button.setVisible(True)
            self._maximize_button.setEnabled(True)
        self.__maximized = False

        if self.__use_shadow:
            self.__show_resizers(True)
            self.__drag_move_enabled = True
            self.setWindowState(Qt.WindowNoState)
            self.layout().setMargin(self.__style.window.SHADOW_RADIUS_PX)  # adjust window for drop-shadow margin
            if sys.platform == 'win32':
                # There is a problem with correct redraw / update on Win10 - the transparency of the
                # shadow effect may be broken on window restore. Re-adjusting the height of the window
                # fixes this.
                size = self.size()
                self.resize(size.width(), size.height() - 1)
                QApplication.instance().processEvents()
                self.resize(size.width(), size.height())
        else:
            self.setWindowState(Qt.WindowNoState)

        self.__move_window_buttons()  # adjust window for drop-shadow margin
        self._maximize_button.setAttribute(Qt.WA_UnderMouse, False)  # prevent hover state form getting stuck
        self._restore_button.setAttribute(Qt.WA_UnderMouse, False)

    @Slot()  # type: ignore
    def __on_maximize_button_clicked(self) -> None:
        """Maximize button clicked"""
        if self._maximize_button.isEnabled() or self._restore_button.isEnabled():
            self._restore_button.setVisible(True)
            self._restore_button.setEnabled(True)
            self._maximize_button.setVisible(False)
            self._maximize_button.setEnabled(False)
        self.__maximized = True

        if self.__use_shadow:
            self.setWindowState(Qt.WindowMaximized)  # adjust window for drop-shadow margin
            self.layout().setMargin(0)
            self.__show_resizers(False)
            self.__drag_move_enabled = False
        else:
            self.setWindowState(Qt.WindowMaximized)  # adjust window for drop-shadow margin

        self.__move_window_buttons()  # adjust window for drop-shadow margin
        self._maximize_button.setAttribute(Qt.WA_UnderMouse, False)  # prevent hover state form getting stuck
        self._restore_button.setAttribute(Qt.WA_UnderMouse, False)

    @Slot()  # type: ignore
    def __on_close_button_clicked(self) -> None:
        """Close button clicked"""
        self.close()

    @Slot()  # type: ignore
    def __on_title_bar_double_clicked(self) -> None:
        """Maximize / Restore window on titlebar double click"""
        if not bool(self.windowState() & Qt.WindowMaximized):
            self.__on_maximize_button_clicked()
        else:
            self.__on_restore_button_clicked()

    def __get_title_tabwidget_style(self, background: QColor) -> str:
        """Gets the QSS for the TabBar widget and adjusts margins"""
        margin_top_px = self.__style.window.TITLE_BAR_TOP_MARGIN_PX
        top_bottom_border_px = (self.__style.window.TITLE_BAR_TAB_CSS_TOP_BORDER_PX +
                                self.__style.window.TITLE_BAR_TAB_CSS_BOTTOM_BORDER_PX)
        height_px = self.titlebar_height - margin_top_px - top_bottom_border_px
        style: str = self.__style.get_title_tabwidget_stylesheet()
        style = style.replace('{TITLEBAR_HEIGHT}', str(height_px))
        button_margin = str(self.window_buttons_margin +
                            self.window_buttons_width +
                            self.__style.window.TITLE_BAR_BUTTON_MIN_X_MARGIN_PX)
        if self.__window_buttons_position == WINDOW_BUTTONS_RIGHT:
            style = style.replace('{WINDOW_BUTTON_MARGIN_LEFT}', str(0))
            style = style.replace('{WINDOW_BUTTON_MARGIN_RIGHT}', button_margin)
        else:
            style = style.replace('{WINDOW_BUTTON_MARGIN_LEFT}', button_margin)
            style = style.replace('{WINDOW_BUTTON_MARGIN_RIGHT}', str(0))
        style = style.replace('{BACKGROUND_COLOR}', background.name())
        return style

    @Slot()  # type: ignore
    def __app_focus_changed_slot(self) -> None:
        """Changes the titlebar's background color when the window acquires/loses focus"""
        if self.isActiveWindow():
            self.__window_frame_widget.set_background_color(self.__titlebar_color)
        else:
            self.__window_frame_widget.set_background_color(self.__titlebar_nofocus_color)
        self.__window_frame_widget.update()

        if self.__tab_widget is not None:
            if self.isActiveWindow():
                self.__tab_widget.setStyleSheet(self.__get_title_tabwidget_style(self.__titlebar_color))
            else:
                self.__tab_widget.setStyleSheet(self.__get_title_tabwidget_style(self.__titlebar_nofocus_color))

    def __adjust_title_tabwidget(self, tab_widget: QTabWidget) -> None:
        """
        Adjusts a TabWidget to work as a Google Chrome style tab bar in the window's title bar.
        TODO: to properly center the Widget (doesn't apply to TabWidgets) a bottom margin of 2px is needed;
              why is that? Action: track down source for this offset in the QSS definitions and figure out the
              proper calculation of this value.
        """
        # add properties to ensure style is only applied tabwidget in titlebar
        if isinstance(tab_widget, QTabWidget):
            self.__tab_widget = tab_widget
            tab_widget.setProperty("class", "TitleTabWidget")  # type: ignore
            tab_widget.tabBar().setProperty("class", "TitleTabBar")  # type: ignore
            tab_widget.setStyleSheet(self.__get_title_tabwidget_style(self.__titlebar_color))
            # insert empty disabled tab for rounded effect on last tab
            idx = tab_widget.addTab(QWidget(), "")
            tab_widget.setTabEnabled(idx, False)
            self.__tab_widget_dummy_close_button = QWidget()
            self.__tab_widget_dummy_close_button.setGeometry(0, 0, 1, 1)
            # remove close button for last widget
            tab_widget.tabBar().setTabButton(idx, QTabBar.RightSide, self.__tab_widget_dummy_close_button)
            self.__tab_widget_filter = TabFilter(tab_widget.tabBar())
            tab_widget.tabBar().installEventFilter(self.__tab_widget_filter)
            tab_widget.tabBar().setDocumentMode(True)
            tab_widget.tabBar().setExpanding(False)
        else:
            margin_top_px: int = self.__style.window.TITLE_BAR_TOP_MARGIN_PX  # type: ignore
            margin_bottom_px: int = self.__style.window.TITLE_BAR_TAB_CSS_BOTTOM_BORDER_PX
            height_px: int = self.titlebar_height - margin_top_px - margin_bottom_px
            button_margin: int = (self.window_buttons_margin +
                                  self.window_buttons_width +
                                  self.__style.window.TITLE_BAR_BUTTON_MIN_X_MARGIN_PX)
            non_button_margin: int = self.__style.window.TITLE_BAR_BUTTON_MIN_X_MARGIN_PX
            if self.__window_buttons_position == WINDOW_BUTTONS_RIGHT:
                tab_widget.layout().setContentsMargins(non_button_margin, 2, button_margin, 0)  # TODO: why 2?
            else:
                tab_widget.layout().setContentsMargins(button_margin, 2, non_button_margin, 0)  # TODO: why 2?
            tab_widget.setMaximumHeight(height_px)
            tab_widget.setMinimumHeight(height_px)
