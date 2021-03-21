__author__ = "Robert Kist"


# QProgressBar
progressbar_style = '''
QProgressBar {
    border: 0px;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    height: 8px;
    min-height: 8px;
    max-height: 8px;
    margin-top: 7px;
    margin-bottom: 7px;
    color: transparent;
}

QProgressBar::chunk {
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    background: palette(highlight);
}

QProgressBar::chunk:disabled {
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    background: palette(midlight);
}
'''
