# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(412, 277)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.msgInformation = QPushButton(self.centralwidget)
        self.msgInformation.setObjectName(u"msgInformation")

        self.gridLayout.addWidget(self.msgInformation, 4, 1, 1, 1)

        self.msgWarning = QPushButton(self.centralwidget)
        self.msgWarning.setObjectName(u"msgWarning")

        self.gridLayout.addWidget(self.msgWarning, 0, 1, 1, 1)

        self.msgCritical = QPushButton(self.centralwidget)
        self.msgCritical.setObjectName(u"msgCritical")

        self.gridLayout.addWidget(self.msgCritical, 1, 1, 1, 1)

        self.msgNoIcon = QPushButton(self.centralwidget)
        self.msgNoIcon.setObjectName(u"msgNoIcon")

        self.gridLayout.addWidget(self.msgNoIcon, 3, 1, 1, 1)

        self.msgQuestion = QPushButton(self.centralwidget)
        self.msgQuestion.setObjectName(u"msgQuestion")

        self.gridLayout.addWidget(self.msgQuestion, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 412, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.msgInformation.setText(QCoreApplication.translate("MainWindow", u"Msg Information", None))
        self.msgWarning.setText(QCoreApplication.translate("MainWindow", u"Msg Warning", None))
        self.msgCritical.setText(QCoreApplication.translate("MainWindow", u"Msg Critical", None))
        self.msgNoIcon.setText(QCoreApplication.translate("MainWindow", u"Msg NoIcon", None))
        self.msgQuestion.setText(QCoreApplication.translate("MainWindow", u"Msg Question", None))
    # retranslateUi

