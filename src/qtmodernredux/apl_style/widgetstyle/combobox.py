__author__ = "Robert Kist"


# QComboBox
combobox_style = '''
QComboBox {
    background: palette(button);
    border-radius: 5px;
    height: 22px;
    min-height: 22px;
    max-height: 22px;
    padding-left: 5px;
    padding-right: 10px;
    selection-background-color: palette(highlight);
    border: 2px solid transparent;
    margin-left: 0px;
    margin-right: 1px;
}

QComboBox:disabled {
    background: transparent;
    margin: 1px;
    border: 1px solid palette(button);
}

QComboBox:editable:disabled {
     background: palette(dark);
     height: 22px;
     min-height: 22px;
     max-height: 22px;
     border: 1px solid palette(dark);;
}

QComboBox:editable {
     background: palette(dark);
     height: 22px;
     min-height: 22px;
     max-height: 22px;
     border: 2px solid transparent;
}

QComboBox:editable:focus {
    border-radius: 5px;
    height: 22px;
    min-height: 22px;
    max-height: 22px;
    border: 2px solid palette(highlight);
}

QComboBox:drop-down, QComboBox::drop-down:editable {
    height: 24px;
    subcontrol-origin: margin;
    subcontrol-position: center right;
    background: palette(button);
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    border: 0px solid transparent;
    margin-right: 1px;
}

QComboBox::drop-down:editable:focus {
    height: 22px;
    subcontrol-origin: margin;
    subcontrol-position: center right;
    background: palette(button);
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    border: 2px solid palette(highlight);
    border-left: 0px;
    padding-left: 1px;
}

QComboBox::drop-down:disabled {
    height: 24px;
    subcontrol-origin: margin;
    subcontrol-position: center right;
    background: transparent;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    border: 0px solid transparent;
    margin-right: 1px;
}

QComboBox::drop-down:pressed {
    height: 24px;
    subcontrol-origin: margin;
    subcontrol-position: center right;
    background: palette(highlight);
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    border: 0px solid transparent;
    margin-right: 1px;
}

QComboBox::down-arrow {
    image: url(:/third_party/icons/arrow-down.svg);
}
'''
