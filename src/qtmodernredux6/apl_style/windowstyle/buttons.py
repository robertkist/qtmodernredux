__author__ = "Robert Kist; Gerard Marull-Paretas"


# Styling for maximize, minimize, close buttons in the window titlebar
buttons_style = '''
/* ***** Restore and Maximize Button Sizes ***** */
#btnClose, #btnRestore, #btnMaximize, #btnMinimize {
    min-width: {TITLE_BAR_BUTTON_DIAMETER_PX}px;
    min-height: {TITLE_BAR_BUTTON_DIAMETER_PX}px;
    max-width: {TITLE_BAR_BUTTON_DIAMETER_PX}px;
    max-height: {TITLE_BAR_BUTTON_DIAMETER_PX}px;
    border-radius: {BUTTON_DIAMETER_HALF_PX}px;
}

/* ***** Restore and Maximize Button Colors ***** */
#btnRestore, #btnMaximize {
  background-color: {BTN_MAXIMIZE_COLOR_DEFAULT_RGB};
}
#btnRestore::hover, #btnMaximize::hover {
  background-color: {BTN_MAXIMIZE_COLOR_HOVER_RGB};
}
#btnRestore::pressed, #btnMaximize::pressed {
  background-color: {BTN_MAXIMIZE_COLOR_PRESSED_RGB};
}

/* ***** Minimize Button Colors ***** */
#btnMinimize {
  background-color: {BTN_MINIMIZE_COLOR_DEFAULT_RGB};
}
#btnMinimize::hover {
  background-color: {BTN_MINIMIZE_COLOR_HOVER_RGB};
}
#btnMinimize::pressed {
  background-color: {BTN_MINIMIZE_COLOR_PRESSED_RGB};
}

/* ***** Close Button Colors ***** */
#btnClose {
  background-color: {BTN_CLOSE_COLOR_DEFAULT_RGB};
}
#btnClose::hover {
  background-color: {BTN_CLOSE_COLOR_HOVER_RGB};
}
#btnClose::pressed {
  background-color: {BTN_CLOSE_COLOR_PRESSED_RGB};
}
'''
