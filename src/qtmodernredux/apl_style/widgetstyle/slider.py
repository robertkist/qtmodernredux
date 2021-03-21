__author__ = "Robert Kist"


# QSlider
slider_style = '''
QSlider::handle {
    background: palette(light);
    border-radius: 7px;
}

QSlider::handle:disabled {
    background: {GREY_127_RGB};
    border-radius: 7px;
}

QSlider::add-page:horizontal {
    background: palette(base);
    border-radius: 3px;
}

QSlider::sub-page:horizontal {
    background: palette(highlight);
    border-radius: 3px;
}

QSlider::sub-page:horizontal:disabled {
    background-color: palette(midlight);
    border-radius: 3px;
}
'''
