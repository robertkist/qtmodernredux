#  * There is a bug in Qt 5.15.2 with the Fusion style: the selected cell will have a slight blue gradient
#  * in the same color of the highlight.
treeview_style = '''
QTreeView {
    border: 0px;
    alternate-background-color: yellow;
    show-decoration-selected: 1;
    selection-background-color: palette(highlight); /* Used on Mac */
    selection-color: palette(light); /* Used on Mac */
}

QTreeView::item {
    background: transparent;
    padding: 2px;
    border: 0px;
    selection-background-color: transparent;
}

QTreeView::item:active {
    background: transparent;
    padding: 2px;
    border: 0px;
}

QTreeView::item:selected {
    background: palette(highlight);
    selection-background-color: palette(highlight);
    border: 0px;
}
'''
