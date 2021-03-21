__author__ = "Robert Kist"


# QSpinBox, QDateTimeEdit
spinbox_style = '''
QSpinBox, QDateTimeEdit {
    background: palette(button);
    border-radius: 5px;
    height: 22px;
    min-height: 22px;
    max-height: 22px;
    padding-left: 10px;
    padding-right: 10px;
    selection-background-color: palette(highlight);
    border: 2px solid transparent;
    margin-left: 0px;
    margin-right: 0px;
}

QSpinBox:disabled, QDateTimeEdit:disabled {
    border-radius: 5px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 1px;
    margin-left: 1px;
    background: transparent;
    border:1px solid palette(midlight);
}

QSpinBox::down-button, QDateTimeEdit::down-button {
    subcontrol-origin: margin;
    subcontrol-position: bottom right;
    border-image: url(:/third_party/icons/arrow-down.svg) 1;
}

QSpinBox::up-button, QDateTimeEdit::up-button {
    subcontrol-origin: margin;
    subcontrol-position: top right;
    border-image: url(:/third_party/icons/arrow-up.svg) 1;
}

QSpinBox::up-button:disabled, QDateTimeEdit::up-button:disabled {
    subcontrol-origin: margin;
    subcontrol-position: top right;
    border-image: url(:/third_party/icons/arrow-up.svg) 1;
}

QSpinBox::down-button:disabled, QDateTimeEdit::down-button:disabled {
    subcontrol-origin: margin;
    subcontrol-position: bottom right;
    border-image: url(:/third_party/icons/arrow-down.svg) 1;
}

QSpinBox::up-button:pressed, QDateTimeEdit::up-button:pressed {
    margin: 1px;
    subcontrol-origin: margin;
    subcontrol-position: top right;
    border-top-right-radius: 5px;
    background-color: palette(highlight);
}

QSpinBox::down-button:pressed, QDateTimeEdit::down-button:pressed {
    margin: 1px;
    subcontrol-origin: margin;
    subcontrol-position: bottom right;
    border-bottom-right-radius: 5px;
    background-color: palette(highlight);
}
'''
