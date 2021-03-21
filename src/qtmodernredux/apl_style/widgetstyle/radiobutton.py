__author__ = "Robert Kist"


# QRadioButton
radiobutton_style = '''
QRadioButton:disabled {
    background: transparent;
}

QRadioButton::indicator {
    background: palette(dark);
    width: 8px;
    height: 8px;
    border: 3px solid palette(dark);
    border-radius: 7px;
}

QRadioButton::indicator:checked {
    background: palette(highlight);
}

QRadioButton::indicator:checked:disabled {
    background: palette(midlight);
}
'''
