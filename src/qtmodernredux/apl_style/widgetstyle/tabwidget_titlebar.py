__author__ = "Robert Kist"


# This qss is for styling a tab-bar that exists in the windows' titlebar (e.g. like in Google's Chrome browser).
# QTabWidget and sub-component QTabBar in titlebar
tabwidget_titlebar_style = '''
.TitleTabWidget {
    background-color: #ff0000;
    border: 0px;
}

.TitleTabWidget::pane {
    border: 0px;
}

.TitleTabWidget::tab-bar {
    alignment: left;
    left: {WINDOW_BUTTON_MARGIN_LEFT}px;
    right: {WINDOW_BUTTON_MARGIN_RIGHT}px;
}

.TitleTabBar QToolButton {
    background-color: {BACKGROUND_COLOR};
    border: none;
}

.TitleTabBar QToolButton::right-arrow {
    image: url(:/third_party/icons/arrow-right.svg) 1;
}

.TitleTabBar QToolButton::right-arrow:pressed {
    image: url(:/third_party/icons/arrow-right-pressed.svg) 1;
}

.TitleTabBar QToolButton::right-arrow:disabled {
    image: url(:/third_party/icons/arrow-right-disabled.svg) 1;
}

.TitleTabBar QToolButton::left-arrow {
    image: url(:/third_party/icons/arrow-left.svg) 1;
}

.TitleTabBar QToolButton::left-arrow:pressed {
    image: url(:/third_party/icons/arrow-left-pressed.svg) 1;
}

.TitleTabBar QToolButton::left-arrow:disabled {
    image: url(:/third_party/icons/arrow-left-disabled.svg) 1;
}

.TitleTabBar::tab, .TitleTabBar::tab:disabled, .TitleTabBar::tab:selected:disabled {
    margin-top: 0px;
    height: {TITLEBAR_HEIGHT};
    padding-left: 10px;
    padding-right: 10px;
    border-width: 8px 16px 8px 16px;
    border-image: url(:/icons/tab-inactive.svg) 16 32 stretch;
    padding: 0px 0px;
}

.TitleTabBar::tab:selected {
    padding-left: 10px;
    padding-right: 10px;
    border-width: 8px 16px 8px 16px;
    border-image: url(:/icons/tab-active.svg) 16 32 stretch;
}

.TitleTabBar::tab:!first {
    margin-left: -9px;
    padding-left: 19px;
}

.TitleTabBar::tab:!last {
    margin-right: -9px;
    padding-right: 19px;
}

.TitleTabBar::tab:first {
    margin-left: -2px;
    padding-left: 12px;
}

.TitleTabBar::tear {
    width: 0px;
}

.TitleTabBar::close-button {
    image: url(:/third_party/icons/button_cancel.svg) 1;
}

.TitleTabBar::close-button:pressed {
    image: url(:/third_party/icons/button_cancel_pressed.svg) 1;
}
'''
