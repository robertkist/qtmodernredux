__author__ = "Robert Kist"


# QGroupBox
groupbox_style = '''
QGroupBox {
    border: 1px solid palette(midlight);
    background: transparent;
    border-radius: 5px;
    margin-top: 8px;
    padding: 4px;
    padding-top: 6px;
    padding-bottom: 2px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    margin-bottom: 0px;
    margin-top: 1px;
    background-color: palette(alternatebase);
    min-height: 14px;
    height: 14px;
}

QGroupBox::indicator {
    margin-left: 2px;
    width: 8px;
    height: 8px;
    background: palette(highlight);
    border: 3px solid palette(dark);
}

QGroupBox::indicator:unchecked {
    background: palette(dark);
    border: 3px solid palette(dark);
}
'''
