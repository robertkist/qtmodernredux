__author__ = "Robert Kist"


# QTabWidget and QTabBar sub-component
tabwidget_style = '''
QTabBar {
    background-color: transparent;
    qproperty-drawBase: 0;
    border: 0px;
}

QTabWidget::pane {
    border: 0px;
    border-top: 1px solid palette(dark);
}

QTabWidget::tab-bar {
    left: 0px;
}

QTabBar::tear {
    width: 0px;
}

QTabBar::tab{
    margin-top: 4px;
    padding-left: 15px;
    padding-right: 15px;
    height: 28px;
    border-top: 2px solid transparent;
    background-color: transparent;
    border-bottom: 4px solid transparent;
    color: #a0a0a0;
}

QTabBar::tab:selected {
    border-bottom: 4px solid palette(highlight);
    color: palette(light);
}

QTabBar::tab:disabled {
    border-bottom: 4px solid transparent;
    color: palette(midlight);
}

QTabBar::tab:selected:disabled {
    border-bottom: 4px solid palette(midlight);
    color: palette(midlight);
}

QTabBar::close-button {
    image: url(:/third_party/icons/button_cancel.svg) 1;
}

QTabBar::close-button:pressed {
    image: url(:/third_party/icons/button_cancel_pressed.svg) 1;
}

QTabBar QToolButton {
    background-color: {WINDOW_BACKGROUND_RGB};
    border: none;
}

QTabBar QToolButton::right-arrow {
    image: url(:/third_party/icons/arrow-right.svg) 1;
}

QTabBar QToolButton::right-arrow:pressed {
    image: url(:/third_party/icons/arrow-right-pressed.svg) 1;
}

QTabBar QToolButton::right-arrow:disabled {
    image: url(:/third_party/icons/arrow-right-disabled.svg) 1;
}

QTabBar QToolButton::left-arrow {
    image: url(:/third_party/icons/arrow-left.svg) 1;
}

QTabBar QToolButton::left-arrow:pressed {
    image: url(:/third_party/icons/arrow-left-pressed.svg) 1;
}

QTabBar QToolButton::left-arrow:disabled {
    image: url(:/third_party/icons/arrow-left-disabled.svg) 1;
}

'''
