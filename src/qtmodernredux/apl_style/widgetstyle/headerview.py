__author__ = "Robert Kist"


# Note: there is no way in Fusion style to prevent that the header text of the active row/column gets bold.
# QHeaderView
headerview_style = '''
QHeaderView {
    border: 0px;
    background: palette(dark);
    padding: 0px;
    margin: 0px;
}

QTableView QTableCornerButton::section {
    background-color: palette(button);
    border: 0px;
    outline: 1px solid red;
    margin-right: 1px;
    margin-bottom: 1px;
}

QHeaderView::section {
    border-style: none;
    border-bottom: 1px solid palette(base);
    border-right: 1px solid palette(base);
    background-color: palette(button);
    padding-left: 4px;
}

QTreeView QHeaderView::section:last {
    border-style: none;
    border-bottom: 1px solid palette(base);
    background-color: palette(button);
    padding-left: 4px;
}
'''
