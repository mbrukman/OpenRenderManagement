# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsrc/mainwindow.ui'
#
# Created: Wed Apr  9 17:33:02 2014
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 580)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblEndDate = QtGui.QLabel(self.centralwidget)
        self.lblEndDate.setObjectName("lblEndDate")
        self.gridLayout.addWidget(self.lblEndDate, 3, 0, 1, 1)
        self.lblLength = QtGui.QLabel(self.centralwidget)
        self.lblLength.setObjectName("lblLength")
        self.gridLayout.addWidget(self.lblLength, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkWorking = QtGui.QCheckBox(self.centralwidget)
        self.chkWorking.setChecked(True)
        self.chkWorking.setObjectName("chkWorking")
        self.horizontalLayout_2.addWidget(self.chkWorking)
        self.chkIdle = QtGui.QCheckBox(self.centralwidget)
        self.chkIdle.setChecked(True)
        self.chkIdle.setObjectName("chkIdle")
        self.horizontalLayout_2.addWidget(self.chkIdle)
        self.chkPaused = QtGui.QCheckBox(self.centralwidget)
        self.chkPaused.setChecked(True)
        self.chkPaused.setObjectName("chkPaused")
        self.horizontalLayout_2.addWidget(self.chkPaused)
        self.chkOffline = QtGui.QCheckBox(self.centralwidget)
        self.chkOffline.setChecked(True)
        self.chkOffline.setObjectName("chkOffline")
        self.horizontalLayout_2.addWidget(self.chkOffline)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.lblSelectReport = QtGui.QLabel(self.centralwidget)
        self.lblSelectReport.setObjectName("lblSelectReport")
        self.gridLayout.addWidget(self.lblSelectReport, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chkNow = QtGui.QCheckBox(self.centralwidget)
        self.chkNow.setChecked(True)
        self.chkNow.setObjectName("chkNow")
        self.horizontalLayout_5.addWidget(self.chkNow)
        self.dtEndDate = QtGui.QDateTimeEdit(self.centralwidget)
        self.dtEndDate.setEnabled(False)
        self.dtEndDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2014, 1, 1), QtCore.QTime(8, 0, 0)))
        self.dtEndDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2014, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtEndDate.setMinimumDate(QtCore.QDate(2014, 1, 1))
        self.dtEndDate.setCalendarPopup(True)
        self.dtEndDate.setObjectName("dtEndDate")
        self.horizontalLayout_5.addWidget(self.dtEndDate)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.cbReport = QtGui.QComboBox(self.centralwidget)
        self.cbReport.setEnabled(False)
        self.cbReport.setObjectName("cbReport")
        self.cbReport.addItem("")
        self.cbReport.addItem("")
        self.gridLayout.addWidget(self.cbReport, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.slLength = QtGui.QSlider(self.centralwidget)
        self.slLength.setMinimum(1)
        self.slLength.setMaximum(168)
        self.slLength.setSingleStep(1)
        self.slLength.setPageStep(24)
        self.slLength.setProperty("value", 24)
        self.slLength.setSliderPosition(24)
        self.slLength.setOrientation(QtCore.Qt.Horizontal)
        self.slLength.setInvertedAppearance(False)
        self.slLength.setInvertedControls(False)
        self.slLength.setTickPosition(QtGui.QSlider.NoTicks)
        self.slLength.setTickInterval(20)
        self.slLength.setObjectName("slLength")
        self.horizontalLayout_4.addWidget(self.slLength)
        self.spLength = QtGui.QSpinBox(self.centralwidget)
        self.spLength.setMinimum(1)
        self.spLength.setMaximum(168)
        self.spLength.setProperty("value", 24)
        self.spLength.setObjectName("spLength")
        self.horizontalLayout_4.addWidget(self.spLength)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblResolution = QtGui.QLabel(self.centralwidget)
        self.lblResolution.setObjectName("lblResolution")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblResolution)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.slResolution = QtGui.QSlider(self.centralwidget)
        self.slResolution.setMinimum(8)
        self.slResolution.setMaximum(60)
        self.slResolution.setSingleStep(1)
        self.slResolution.setProperty("value", 30)
        self.slResolution.setOrientation(QtCore.Qt.Horizontal)
        self.slResolution.setObjectName("slResolution")
        self.horizontalLayout_7.addWidget(self.slResolution)
        self.spResolution = QtGui.QSpinBox(self.centralwidget)
        self.spResolution.setMinimum(8)
        self.spResolution.setMaximum(60)
        self.spResolution.setSingleStep(1)
        self.spResolution.setProperty("value", 30)
        self.spResolution.setObjectName("spResolution")
        self.horizontalLayout_7.addWidget(self.spResolution)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.lblGraphType = QtGui.QLabel(self.centralwidget)
        self.lblGraphType.setObjectName("lblGraphType")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblGraphType)
        self.cbGraphType = QtGui.QComboBox(self.centralwidget)
        self.cbGraphType.setObjectName("cbGraphType")
        self.cbGraphType.addItem("")
        self.cbGraphType.addItem("")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbGraphType)
        self.lblScaleType = QtGui.QLabel(self.centralwidget)
        self.lblScaleType.setObjectName("lblScaleType")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblScaleType)
        self.cbScaleType = QtGui.QComboBox(self.centralwidget)
        self.cbScaleType.setObjectName("cbScaleType")
        self.cbScaleType.addItem("")
        self.cbScaleType.addItem("")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbScaleType)
        self.lblStyle = QtGui.QLabel(self.centralwidget)
        self.lblStyle.setObjectName("lblStyle")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblStyle)
        self.cbGraphStyle = QtGui.QComboBox(self.centralwidget)
        self.cbGraphStyle.setObjectName("cbGraphStyle")
        self.cbGraphStyle.addItem("")
        self.cbGraphStyle.addItem("")
        self.cbGraphStyle.addItem("")
        self.cbGraphStyle.addItem("")
        self.cbGraphStyle.addItem("")
        self.cbGraphStyle.addItem("")
        self.cbGraphStyle.addItem("")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbGraphStyle)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.log = QtGui.QPlainTextEdit(self.centralwidget)
        self.log.setUndoRedoEnabled(False)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setEnabled(False)
        self.menuFile.setObjectName("menuFile")
        self.menuSnapshots = QtGui.QMenu(self.menubar)
        self.menuSnapshots.setEnabled(False)
        self.menuSnapshots.setObjectName("menuSnapshots")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSnapshot = QtGui.QAction(MainWindow)
        self.actionSnapshot.setObjectName("actionSnapshot")
        self.actionCreate = QtGui.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionClear_all_snapshots = QtGui.QAction(MainWindow)
        self.actionClear_all_snapshots.setObjectName("actionClear_all_snapshots")
        self.actionGenerate = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../homes/jsa/.designer/backup/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenerate.setIcon(icon)
        self.actionGenerate.setIconVisibleInMenu(True)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setEnabled(False)
        self.actionReset.setObjectName("actionReset")
        self.actionExport_as = QtGui.QAction(MainWindow)
        self.actionExport_as.setObjectName("actionExport_as")
        self.menuFile.addAction(self.actionExport_as)
        self.menuSnapshots.addAction(self.actionCreate)
        self.menuSnapshots.addAction(self.actionDelete)
        self.menuSnapshots.addAction(self.actionClear_all_snapshots)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSnapshots.menuAction())
        self.toolBar.addAction(self.actionGenerate)
        self.toolBar.addAction(self.actionReset)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.chkNow, QtCore.SIGNAL("toggled(bool)"), self.dtEndDate.setDisabled)
        QtCore.QObject.connect(self.spLength, QtCore.SIGNAL("valueChanged(int)"), self.slLength.setValue)
        QtCore.QObject.connect(self.slLength, QtCore.SIGNAL("valueChanged(int)"), self.spLength.setValue)
        QtCore.QObject.connect(self.spResolution, QtCore.SIGNAL("valueChanged(int)"), self.slResolution.setValue)
        QtCore.QObject.connect(self.slResolution, QtCore.SIGNAL("valueChanged(int)"), self.spResolution.setValue)
        QtCore.QObject.connect(self.cbGraphType, QtCore.SIGNAL("currentIndexChanged(QString)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.cbScaleType, QtCore.SIGNAL("currentIndexChanged(QString)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.cbGraphStyle, QtCore.SIGNAL("currentIndexChanged(QString)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.slLength, QtCore.SIGNAL("sliderReleased()"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.slResolution, QtCore.SIGNAL("sliderReleased()"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.spResolution, QtCore.SIGNAL("editingFinished()"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.chkNow, QtCore.SIGNAL("toggled(bool)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.chkIdle, QtCore.SIGNAL("toggled(bool)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.chkWorking, QtCore.SIGNAL("toggled(bool)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.chkOffline, QtCore.SIGNAL("toggled(bool)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.chkPaused, QtCore.SIGNAL("toggled(bool)"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.dtEndDate, QtCore.SIGNAL("editingFinished()"), self.actionGenerate.trigger)
        QtCore.QObject.connect(self.spLength, QtCore.SIGNAL("editingFinished()"), self.actionGenerate.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblEndDate.setText(QtGui.QApplication.translate("MainWindow", "Until", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLength.setText(QtGui.QApplication.translate("MainWindow", "Display last N hours", None, QtGui.QApplication.UnicodeUTF8))
        self.chkWorking.setText(QtGui.QApplication.translate("MainWindow", "Working", None, QtGui.QApplication.UnicodeUTF8))
        self.chkIdle.setText(QtGui.QApplication.translate("MainWindow", "Idle", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPaused.setText(QtGui.QApplication.translate("MainWindow", "Paused", None, QtGui.QApplication.UnicodeUTF8))
        self.chkOffline.setText(QtGui.QApplication.translate("MainWindow", "Offline", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSelectReport.setText(QtGui.QApplication.translate("MainWindow", "Select a report", None, QtGui.QApplication.UnicodeUTF8))
        self.chkNow.setText(QtGui.QApplication.translate("MainWindow", "Now", None, QtGui.QApplication.UnicodeUTF8))
        self.dtEndDate.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "dd MMM hh:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.cbReport.setItemText(0, QtGui.QApplication.translate("MainWindow", "RN Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.cbReport.setItemText(1, QtGui.QApplication.translate("MainWindow", "Job Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResolution.setText(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGraphType.setText(QtGui.QApplication.translate("MainWindow", "Graph type", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphType.setItemText(0, QtGui.QApplication.translate("MainWindow", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphType.setItemText(1, QtGui.QApplication.translate("MainWindow", "Stacked", None, QtGui.QApplication.UnicodeUTF8))
        self.lblScaleType.setText(QtGui.QApplication.translate("MainWindow", "Scale type", None, QtGui.QApplication.UnicodeUTF8))
        self.cbScaleType.setItemText(0, QtGui.QApplication.translate("MainWindow", "Standard", None, QtGui.QApplication.UnicodeUTF8))
        self.cbScaleType.setItemText(1, QtGui.QApplication.translate("MainWindow", "Logarithmic", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStyle.setText(QtGui.QApplication.translate("MainWindow", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(0, QtGui.QApplication.translate("MainWindow", "RedBlue", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(1, QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(2, QtGui.QApplication.translate("MainWindow", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(3, QtGui.QApplication.translate("MainWindow", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(4, QtGui.QApplication.translate("MainWindow", "Clean", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(5, QtGui.QApplication.translate("MainWindow", "DarkColorized", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGraphStyle.setItemText(6, QtGui.QApplication.translate("MainWindow", "DarkGreenBlue", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSnapshots.setTitle(QtGui.QApplication.translate("MainWindow", "&Snapshots", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnapshot.setText(QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate.setText(QtGui.QApplication.translate("MainWindow", "&Create", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_all_snapshots.setText(QtGui.QApplication.translate("MainWindow", "Clear all snapshots", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate.setToolTip(QtGui.QApplication.translate("MainWindow", "Create graph with current parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create graph with current parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setToolTip(QtGui.QApplication.translate("MainWindow", "Set parameter values to default", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_as.setText(QtGui.QApplication.translate("MainWindow", "&Export to...", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
