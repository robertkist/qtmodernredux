__author__ = "Robert Kist"


# QSplitter
splitter_style = '''
QSplitter::handle {
    padding: 2px;
}

QSplitter::handle:horizontal {
    background: url(:/icons/handle_hor.svg) 1;
    background-repeat: no-repeat;
    background-position: center;
}

QSplitter::handle:vertical {
    background: url(:/icons/handle_ver.svg) 1;
    background-repeat: no-repeat;
    background-position: center;
    height: 2px;
}
'''
