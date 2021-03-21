__author__ = "Robert Kist"


# QScrollBar
scrollbar_style = '''
QScrollBar:vertical {
    background: palette(base);
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    width: 16px;
    min-width: 16px;
    max-width: 16px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: palette(midlight);
    border-radius: 3px;
    min-height: 20px;
    min-height: 20px;
    max-height: 20px;
    margin: 2px 4px 2px 4px;
}

QScrollBar::add-line:vertical {
    background: none;
    height: 0px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar:horizontal {
    background: palette(base);
    height: 16px;
    min-height: 16px;
    max-height: 16px;
    margin: 0px;
}

QScrollBar::handle:horizontal {
    background-color: palette(midlight);
    border-radius: 3px;
    min-width: 20px;
    margin: 4px 2px 4px 2px;
}

QScrollBar::add-line:horizontal {
    background: none;
    width: 0px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    background: none;
    width: 0px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
'''
