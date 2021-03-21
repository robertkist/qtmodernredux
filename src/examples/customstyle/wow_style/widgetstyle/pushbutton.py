qpushbutton_style = '''
QPushButton {
    background: palette(button);
    border-radius: 5px;
    
    height: 24px;
    min-height: 24px;
    max-height: 24px;
    
    margin-top: 1px;
    margin-bottom: 1px;
    margin-left: 1px;
    margin-right: 1px;
    padding-left: 4px;
    padding-right: 4px;
}

QPushButton:flat {
    background: transparent;
    border:1px solid palette(midlight);
}

QPushButton:checked {
    background: #2a2b34;
    border-radius: 5px;
    
    height: 24px;
    min-height: 24px;
    max-height: 24px;
    
    margin-top: 1px;
    margin-bottom: 1px;
    margin-left: 1px;
    margin-right: 1px;
}

QPushButton:pressed {
    background: #00629d;
    color: #87adcd;
}

QPushButton:flat:pressed {
    background: #00629d;
    border:1px solid #00629d;
    color: #87adcd;
}

QPushButton:flat:disabled {
    background: transparent;
}

QPushButton:disabled {
    background: transparent;
    border:1px solid palette(midlight);
}
'''
