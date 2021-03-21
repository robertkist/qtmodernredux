__author__ = "Robert Kist"


# QTableView, QTableWidget
tableview_style = '''
QTableView {
    border: 0px;
    gridline-color: palette(alternatebase);
    background-color: palette(base);
    alternate-background-color: palette(window);
}

QTableView QScrollBar:vertical {
    background: {WINDOW_BACKGROUND_RGB};
    width: 16px;
    min-width: 16px;
    max-width: 16px;
    margin: 0px;
}

QTableView QScrollBar:horizontal{
    background: {WINDOW_BACKGROUND_RGB};
    height: 16px;
    min-height: 16px;
    max-height: 16px;
    margin: 0px;
}

QTableView:corner {
    background: {WINDOW_BACKGROUND_RGB};
}
'''
