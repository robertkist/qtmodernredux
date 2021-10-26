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
        MainWindow.resize(1125, 743)
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName(u"actionTest")
        self.actionTest_2 = QAction(MainWindow)
        self.actionTest_2.setObjectName(u"actionTest_2")
        self.actionTest_2.setCheckable(True)
        self.actionTest_2.setChecked(True)
        self.actionTest_3 = QAction(MainWindow)
        self.actionTest_3.setObjectName(u"actionTest_3")
        self.actionTest_3.setCheckable(True)
        self.actionTest3 = QAction(MainWindow)
        self.actionTest3.setObjectName(u"actionTest3")
        self.actionTest3_2 = QAction(MainWindow)
        self.actionTest3_2.setObjectName(u"actionTest3_2")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout_2 = QGridLayout(self.centralWidget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.centralWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.centralWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_4 = QCheckBox(self.centralWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(False)

        self.horizontalLayout.addWidget(self.checkBox_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSlider = QSlider(self.groupBox_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setValue(60)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 6, 1, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 2, 0, 1, 3)

        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 4, 0, 1, 3)

        self.fontComboBox = QFontComboBox(self.groupBox_3)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.gridLayout.addWidget(self.fontComboBox, 3, 0, 1, 3)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 5, 0, 1, 3)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 3)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)

        self.horizontalScrollBar = QScrollBar(self.groupBox_3)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setValue(25)
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalScrollBar, 7, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_2 = QTableWidget(self.groupBox_5)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget_2.rowCount() < 10):
            self.tableWidget_2.setRowCount(10)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem22)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(True)

        self.gridLayout_5.addWidget(self.tableWidget_2, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.treeWidget = QTreeWidget(self.verticalLayoutWidget_2)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.treeWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(True)

        self.gridLayout_3.addWidget(self.checkBox_2, 2, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(True)

        self.gridLayout_3.addWidget(self.checkBox, 2, 0, 1, 1)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setToolTipDuration(-10)
        self.radioButton.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget = QTableWidget(self.groupBox_4)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem32)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem45)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_4.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.listWidget = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_6.addWidget(self.listWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_5.addWidget(self.splitter)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1125, 24))
        self.menuTest = QMenu(self.menuBar)
        self.menuTest.setObjectName(u"menuTest")
        self.menuTest2 = QMenu(self.menuBar)
        self.menuTest2.setObjectName(u"menuTest2")
        self.menuTest2_2 = QMenu(self.menuTest2)
        self.menuTest2_2.setObjectName(u"menuTest2_2")
        self.menuStyle = QMenu(self.menuBar)
        self.menuStyle.setObjectName(u"menuStyle")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuTest.menuAction())
        self.menuBar.addAction(self.menuTest2.menuAction())
        self.menuBar.addAction(self.menuStyle.menuAction())
        self.menuTest.addAction(self.actionTest)
        self.menuTest.addAction(self.actionTest_2)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionTest_3)
        self.menuTest2.addAction(self.menuTest2_2.menuAction())
        self.menuTest2_2.addAction(self.actionTest3)
        self.menuTest2_2.addAction(self.actionTest3_2)
        self.menuStyle.addAction(self.actionLight)
        self.menuStyle.addAction(self.actionDark)
        self.mainToolBar.addAction(self.actionTest)
        self.mainToolBar.addAction(self.actionTest_2)
        self.mainToolBar.addAction(self.actionTest3)

        self.retranslateUi(MainWindow)
        self.checkBox_4.toggled.connect(self.groupBox_2.setDisabled)
        self.checkBox_4.toggled.connect(self.groupBox.setDisabled)
        self.checkBox_4.toggled.connect(self.tabWidget.setDisabled)
        self.checkBox_4.toggled.connect(self.groupBox_3.setDisabled)
        self.checkBox_4.toggled.connect(self.progressBar.setDisabled)
        self.checkBox_4.toggled.connect(self.mainToolBar.setDisabled)
        self.checkBox_4.toggled.connect(self.menuBar.setDisabled)
        self.checkBox_4.toggled.connect(self.statusBar.setDisabled)
        self.checkBox_4.toggled.connect(self.comboBox.setDisabled)
        self.checkBox_4.toggled.connect(self.label.setDisabled)
        self.checkBox_4.toggled.connect(self.tableWidget_2.setDisabled)
        self.checkBox_4.toggled.connect(self.treeWidget.setDisabled)
        self.checkBox_4.toggled.connect(self.label_9.setDisabled)
        self.checkBox_4.toggled.connect(self.comboBox_2.setDisabled)
        self.checkBox_4.toggled.connect(self.label_8.setDisabled)
        self.checkBox_4.toggled.connect(self.tableWidget.setDisabled)

        self.pushButton_4.setDefault(True)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionTest.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.actionTest_2.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.actionTest_3.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.actionTest3.setText(QCoreApplication.translate("MainWindow", u"Test3", None))
        self.actionTest3_2.setText(QCoreApplication.translate("MainWindow", u"Test3", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QLabel", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"QComboBox Item 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"QComboBox Item 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"QComboBox Item 3", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Item 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Item 2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Item 3", None))

        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Disable Widgets", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"QGroupBox With Checkbox", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"QScrollbar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"QSlider", None))
        self.groupBox_5.setTitle("")
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem15 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"10", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Cell 1/1", None));
        ___qtablewidgetitem21 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Cell 2/1", None));
        ___qtablewidgetitem22 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell 1/2", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"QTableView - Alternating Rows", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Column2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Column1", None));

        __sortingEnabled1 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Foo2", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Foo2", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Foo1", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Foo1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Bar2", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Bar2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"Bar1", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Bar1", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled1)

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QGroupBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"QCheckBox - Unchecked", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"QRadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"QCheckBox - Checked", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"QRadioButton", None))
        self.groupBox_2.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"QPushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"QPushButton - Checkable", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"QPushButton - Flat", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"QPushButton - Default", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"QProgressBar", None))
        self.groupBox_4.setTitle("")
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem25 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem26 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem27 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem28 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem29 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem30 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem33 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem34 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem35 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem36 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem37 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem38 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem39 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem40 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem41 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem42 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"10", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem43 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Cell 1/1", None));
        ___qtablewidgetitem44 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Cell 2/1", None));
        ___qtablewidgetitem45 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Cell 1/2", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"QTableView", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text';\">test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test"
                        "<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br />test<br /></span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab - QTextEdit", None))

        __sortingEnabled3 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"entry 1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"entry 2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"entry 3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"entry 4", None));
        self.listWidget.setSortingEnabled(__sortingEnabled3)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Empty Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Empty Page", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.menuTest2.setTitle(QCoreApplication.translate("MainWindow", u"Test2", None))
        self.menuTest2_2.setTitle(QCoreApplication.translate("MainWindow", u"Test2", None))
        self.menuStyle.setTitle(QCoreApplication.translate("MainWindow", u"Style", None))
    # retranslateUi

