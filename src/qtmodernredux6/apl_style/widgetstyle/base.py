__author__ = "Robert Kist"


"""
base style: applies to all
Note: QSizegrip must remain disabled as it causes excessive flickering on the Windows platform.
      When using Qmodernwindow there is no need for QSizegrip as the window can be resized from any corner.
"""


base_style = '''
* {
      font-family: Roboto;
      font-size: 12px;
      font-weight: Normal;
      outline: none;
}

QSizeGrip {
    width: 0px;
    height: 0px;
}
'''
