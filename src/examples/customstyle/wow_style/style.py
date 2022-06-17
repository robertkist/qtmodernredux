from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
import wow_style.widgetstyle as wgs
import wow_style.windowstyle as wds


class Style:
    window = wds.Constants

    @staticmethod
    def get_window_stylesheet() -> str:
        qss = ''.join([wds.frame_style, wds.buttons_style])
        for var in vars(wds.Constants)['__annotations__']:
            qss = qss.replace('{%s}' % var, str(getattr(wds.Constants, var)))
        qss = qss.replace('{BUTTON_DIAMETER_HALF_PX}', str(wds.Constants.TITLE_BAR_BUTTON_DIAMETER_PX / 2))
        return qss

    @staticmethod
    def get_title_tabwidget_style() -> str:
        return wgs.tabwidget_titlebar_style

    @staticmethod
    def apply_theme(app: QApplication) -> None:
        """Definition for the 'APL' style"""
        # get stylesheet
        style = ''.join(
            [wgs.base_style, wgs.combobox_style, wgs.groupbox_style, wgs.headerview_style, wgs.lineedit_style,
             wgs.progressbar_style, wgs.qpushbutton_style, wgs.scrollarea_style, wgs.scrollbar_style, wgs.slider_style,
             wgs.spinbox_style, wgs.splitter_style, wgs.tableview_style, wgs.tabwidget_style, wgs.toolbar_style,
             wgs.treeview_style, wgs.radiobutton_style, wgs.checkbox_style])
        style = style.replace('{GREY_127_RGB}', wgs.Constants.GREY_127_RGB)
        style = style.replace('{WINDOW_BACKGROUND_RGB}', wgs.Constants.WINDOW_BACKGROUND_RGB)
        # apply palette Constants.
        palette = QPalette()
        # highlight color
        palette.setColor(QPalette.Highlight, QColor(wgs.Constants.HIGHLIGHT_RGB))
        # text
        palette.setColor(QPalette.WindowText, QColor(wgs.Constants.GREY_180_RGB))
        palette.setColor(QPalette.BrightText, QColor(wgs.Constants.GREY_180_RGB))
        palette.setColor(QPalette.ButtonText, QColor(wgs.Constants.GREY_180_RGB))
        palette.setColor(QPalette.HighlightedText, QColor(wgs.Constants.GREY_180_RGB))
        palette.setColor(QPalette.ToolTipText, QColor(wgs.Constants.GREY_180_RGB))
        # hyperlinks
        palette.setColor(QPalette.LinkVisited, QColor(wgs.Constants.GREY_80_RGB))
        palette.setColor(QPalette.Link, QColor(wgs.Constants.HYPERLINK_RGB))
        # misc elements
        palette.setColor(QPalette.Button, QColor(wgs.Constants.GREY_5C_RGB))
        palette.setColor(QPalette.Light, QColor(wgs.Constants.GREY_180_RGB))
        palette.setColor(QPalette.Midlight, QColor(wgs.Constants.GREY_90_RGB))
        palette.setColor(QPalette.Dark, QColor(wgs.Constants.GREY_35_RGB))
        palette.setColor(QPalette.Text, QColor(wgs.Constants.GREY_180_RGB))
        palette.setColor(QPalette.Base, QColor(wgs.Constants.GREY_42_RGB))
        palette.setColor(QPalette.Window, QColor(wgs.Constants.GREY_53_RGB))
        palette.setColor(QPalette.Shadow, QColor(wgs.Constants.GREY_20_RGB))
        palette.setColor(QPalette.AlternateBase, QColor(wgs.Constants.GREY_66_RGB))
        palette.setColor(QPalette.ToolTipBase, QColor(wgs.Constants.GREY_90_RGB))
        # disabled
        palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(wgs.Constants.GREY_127_RGB))
        palette.setColor(QPalette.Disabled, QPalette.Text, QColor(wgs.Constants.GREY_127_RGB))
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(wgs.Constants.GREY_127_RGB))
        palette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(wgs.Constants.GREY_127_RGB))
        palette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(wgs.Constants.GREY_80_RGB))
        # apple theme
        app.setStyle('Fusion')  # type: ignore
        app.setPalette(palette)
        app.setStyleSheet(style)
