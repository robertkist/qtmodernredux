__author__ = "Robert Kist"


class Constants:
    """Global constants for the style"""
    # Window Title Bar
    TITLE_BAR_COLOR_RGB: str = '#363636'
    TITLE_BAR_NOFOCUS_COLOR_RGB: str = '#282828'
    TITLE_BAR_FONT_COLOR_RGB: str = '#eaeaea'
    TITLE_BAR_HEIGHT_PX: int = 28
    TITLE_BAR_BUTTON_DIAMETER_PX: int = 12
    TITLE_BAR_BUTTON_SPACING_PX: int = 20  # distance from left-button edge to next button's left edge
    TITLE_BAR_BUTTON_MIN_X_MARGIN_PX: int = 8  # min distance to left / right window border
    TITLE_BAR_TOP_MARGIN_PX: int = 6  # margin to top edge of titlebar for widgets in titlebar
    TITLE_BAR_TITLE_TEXT_RIGHT_MARGIN_PX: int = 20  # space between right text edge and window right edge
    TITLE_LABEL_MINIMUM_WIDTH_PX: int = 64
    # Title bar Tab Widget Settings
    TITLE_BAR_TAB_CSS_TOP_BORDER_PX: int = 8
    TITLE_BAR_TAB_CSS_BOTTOM_BORDER_PX: int = 8
    # Window Title Bar: Maximize Button
    BTN_MAXIMIZE_COLOR_DEFAULT_RGB: str = '#64c455'
    BTN_MAXIMIZE_COLOR_HOVER_RGB: str = '#83d077'
    BTN_MAXIMIZE_COLOR_PRESSED_RGB: str = '#46893b'
    # Window Title Bar: Minimize Button
    BTN_MINIMIZE_COLOR_DEFAULT_RGB: str = '#f3be4f'
    BTN_MINIMIZE_COLOR_HOVER_RGB: str = '#ffd83c'
    BTN_MINIMIZE_COLOR_PRESSED_RGB: str = '#c2993f'
    # Window Title Bar: Close Button
    BTN_CLOSE_COLOR_DEFAULT_RGB: str = '#eb6a5e'
    BTN_CLOSE_COLOR_HOVER_RGB: str = '#ff6d60'
    BTN_CLOSE_COLOR_PRESSED_RGB: str = '#da4234'
    # QMessageBox Icons
    MSGBOX_ICON_INFORMATION: str = ':/third_party/icons/emblem-information.svg'
    MSGBOX_ICON_QUESTION: str = ':/third_party/icons/emblem-question.svg'
    MSGBOX_ICON_WARNING: str = ':/third_party/icons/emblem-important.svg'
    MSGBOX_ICON_CRITICAL: str = ':/third_party/icons/emblem-error.svg'
    # Window Drop-Shadow - for platforms where the window manager doesn't add a shadow (e.g. some Linux versions).
    SHADOW_RADIUS_PX: int = 14
    SHADOW_COLOR_RGB: str = '#000000'
    SHADOW_OPACITY_HEX: int = 200
    # General Window Properties
    WINDOW_CORNER_RADIUS_PX: int = 5
    WINDOW_BACKGROUND_RGB: str = '#393939'  # This is the background color for the window
