__author__ = "Robert Kist"


# QCheckBox
checkbox_style = '''
QCheckBox::indicator {
    background: palette(dark);
    width: 8px;
    height: 8px;
    border: 3px solid palette(dark);
}

QCheckBox::indicator:checked {
    background: palette(highlight);
}

QCheckBox::indicator:checked:disabled {
    background: palette(midlight);
}

QCheckBox::indicator:indeterminate {
    background: palette(midlight);
}

QCheckBox::indicator:indeterminate:disabled {
    background: palette(disabled);
}
'''
