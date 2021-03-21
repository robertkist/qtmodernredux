import sys
from typing import Any, Sequence, Optional, Union
from PySide2.QtWidgets import QApplication, QTabWidget, QWidget
from PySide2.QtGui import Qt, QFontDatabase, QColor
import qtmodernredux.resources.qt_resources  # pylint: disable=unused-import
from qtmodernredux.windowstyle.modernwindow import ModernWindow, WINDOW_BUTTONS_LEFT, WINDOW_BUTTONS_RIGHT
from .apl_style import Style


__author__ = "Robert Kist"


STYLES_LIST = ['APL']  # list of built-in style
DEFAULT_STYLE = 'APL'


class QtModernRedux:
    """
    This class implements the primary API for the QtModern module.
    """
    WINDOW_BUTTONS_RIGHT = WINDOW_BUTTONS_RIGHT
    WINDOW_BUTTONS_LEFT = WINDOW_BUTTONS_LEFT
    __style: str = DEFAULT_STYLE
    __style_object: Optional[Any] = None

    @classmethod
    def wrap(cls,
             window: Any,
             parent: Optional[Any] = None,
             title_bar: bool = True,
             transparent_window: bool = True,
             titlebar_height: Optional[int] = None,
             titlebar_color: Optional[QColor] = None,
             titlebar_nofocus_color: Optional[QColor] = None,
             titlebar_text_color: Optional[QColor] = None,
             titlebar_widget: Optional[Union[QWidget, QTabWidget]] = None,
             window_buttons_position: Optional[str] = None) -> ModernWindow:
        """Wraps the given widget into a styled window frame"""
        assert cls.__style_object is not None, "ERROR: must create a QModernRedux qApplication object first"
        return ModernWindow(window=window,
                            parent=parent,
                            style=cls.__style_object,
                            title_bar=title_bar,
                            transparent_window=transparent_window,
                            titlebar_height=titlebar_height,
                            titlebar_color=titlebar_color,
                            titlebar_nofocus_color=titlebar_nofocus_color,
                            titlebar_text_color=titlebar_text_color,
                            titlebar_widget=titlebar_widget,
                            window_buttons_position=window_buttons_position)

    @classmethod
    def __load_custom_fonts(cls) -> None:
        """Loads custom fonts - must be called after the QApplication object has been constructed"""
        font_list = [
            ':/third_party/fonts/Roboto/Roboto-Black.ttf',
            ':/third_party/fonts/Roboto/Roboto-BlackItalic.ttf',
            ':/third_party/fonts/Roboto/Roboto-Bold.ttf',
            ':/third_party/fonts/Roboto/Roboto-BoldItalic.ttf',
            ':/third_party/fonts/Roboto/Roboto-Italic.ttf',
            ':/third_party/fonts/Roboto/Roboto-Light.ttf',
            ':/third_party/fonts/Roboto/Roboto-LightItalic.ttf',
            ':/third_party/fonts/Roboto/Roboto-Medium.ttf',
            ':/third_party/fonts/Roboto/Roboto-MediumItalic.ttf',
            ':/third_party/fonts/Roboto/Roboto-Regular.ttf',
            ':/third_party/fonts/Roboto/Roboto-Thin.ttf',
            ':/third_party/fonts/Roboto/Roboto-ThinItalic.ttf',
        ]
        for font in font_list:
            assert QFontDatabase.addApplicationFont(font) != -1, "ERROR: could not load font: %s" % font

    @classmethod
    def get_style(cls, style_name: str) -> Optional[Any]:
        """
        Returns a style object from the built-in styles. Returns None if style not found
        """
        if style_name == 'APL':
            return Style
        return None

    @classmethod
    def QApplication(cls, argv: Optional[Sequence[Any]] = None,
                     style_name: Optional[str] = None,
                     style: Any = None) -> QApplication:  # pylint: disable=dangerous-default-value
        """
        This method returns a QApplication object with all the settings applied to make this theme
        work flawlessly across different platforms and screens with different DPI settings.
        Arguments:
            * argv: pass sys.argv contents
            * style_name: name of the application style
            * style: an object which carries the appropriate arguments and methods to act as a style
        """
        argv = [] if argv is None else argv
        style_name = 'APL' if style_name is None else style_name
        assert style_name in STYLES_LIST, "ERROR: unknown style %s" % style
        cls.__style = style_name
        if sys.platform == "darwin":
            QApplication.setDesktopSettingsAware(False)
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app = QApplication(argv)
        cls.__load_custom_fonts()
        app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
        cls.__style_object = cls.get_style(style_name) if style is None else style
        assert cls.__style_object is not None, "ERROR: cannot load default style"
        cls.__style_object.apply_theme(app)
        return app
