# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdf/PycharmProjects/validitychecker/src/main/resources/base/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 789)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dataGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.dataGroupBox.setObjectName("dataGroupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.dataGroupBox)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rawDataFrame = QtWidgets.QFrame(self.dataGroupBox)
        self.rawDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rawDataFrame.setObjectName("rawDataFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.rawDataFrame)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rawDataFileNameLabel = QtWidgets.QLabel(self.rawDataFrame)
        self.rawDataFileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rawDataFileNameLabel.setObjectName("rawDataFileNameLabel")
        self.verticalLayout_7.addWidget(self.rawDataFileNameLabel)
        self.rawTableView = QtWidgets.QTableView(self.rawDataFrame)
        self.rawTableView.setEnabled(True)
        self.rawTableView.setMinimumSize(QtCore.QSize(0, 219))
        self.rawTableView.setAlternatingRowColors(True)
        self.rawTableView.setSortingEnabled(True)
        self.rawTableView.setObjectName("rawTableView")
        self.rawTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.rawTableView.verticalHeader().setCascadingSectionResizes(True)
        self.rawTableView.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_7.addWidget(self.rawTableView)
        self.verticalLayout_8.addWidget(self.rawDataFrame)
        self.validityReportFrame = QtWidgets.QFrame(self.dataGroupBox)
        self.validityReportFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.validityReportFrame.setObjectName("validityReportFrame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.validityReportFrame)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.validityReportLabel = QtWidgets.QLabel(self.validityReportFrame)
        self.validityReportLabel.setScaledContents(False)
        self.validityReportLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.validityReportLabel.setObjectName("validityReportLabel")
        self.verticalLayout_12.addWidget(self.validityReportLabel)
        self.validityReportTableView = QtWidgets.QTableView(self.validityReportFrame)
        self.validityReportTableView.setMinimumSize(QtCore.QSize(340, 234))
        self.validityReportTableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.validityReportTableView.setAlternatingRowColors(True)
        self.validityReportTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.validityReportTableView.setSortingEnabled(True)
        self.validityReportTableView.setObjectName("validityReportTableView")
        self.validityReportTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.validityReportTableView.horizontalHeader().setSortIndicatorShown(True)
        self.validityReportTableView.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_12.addWidget(self.validityReportTableView)
        self.verticalLayout_8.addWidget(self.validityReportFrame)
        self.gridLayout_2.addWidget(self.dataGroupBox, 4, 2, 1, 1)
        self.fileGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.fileGroupBox.setObjectName("fileGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fileGroupBox)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openDataFileFrame = QtWidgets.QWidget(self.fileGroupBox)
        self.openDataFileFrame.setObjectName("openDataFileFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.openDataFileFrame)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openDataFileButton = QtWidgets.QPushButton(self.openDataFileFrame)
        self.openDataFileButton.setObjectName("openDataFileButton")
        self.verticalLayout_4.addWidget(self.openDataFileButton)
        self.recentDataFileFrame = QtWidgets.QFrame(self.openDataFileFrame)
        self.recentDataFileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recentDataFileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.recentDataFileFrame.setObjectName("recentDataFileFrame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.recentDataFileFrame)
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.openRecentDataFileLabel = QtWidgets.QLabel(self.recentDataFileFrame)
        self.openRecentDataFileLabel.setEnabled(True)
        self.openRecentDataFileLabel.setObjectName("openRecentDataFileLabel")
        self.verticalLayout_13.addWidget(self.openRecentDataFileLabel)
        self.selectRecentDataFileComboBox = QtWidgets.QComboBox(self.recentDataFileFrame)
        self.selectRecentDataFileComboBox.setCurrentText("")
        self.selectRecentDataFileComboBox.setObjectName("selectRecentDataFileComboBox")
        self.verticalLayout_13.addWidget(self.selectRecentDataFileComboBox)
        self.openRecentDataFileButton = QtWidgets.QPushButton(self.recentDataFileFrame)
        self.openRecentDataFileButton.setEnabled(False)
        self.openRecentDataFileButton.setObjectName("openRecentDataFileButton")
        self.verticalLayout_13.addWidget(self.openRecentDataFileButton)
        self.verticalLayout_4.addWidget(self.recentDataFileFrame)
        self.horizontalLayout.addWidget(self.openDataFileFrame)
        self.openSettingsFileFrame = QtWidgets.QWidget(self.fileGroupBox)
        self.openSettingsFileFrame.setEnabled(False)
        self.openSettingsFileFrame.setObjectName("openSettingsFileFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.openSettingsFileFrame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openValiditySettingsFileButton = QtWidgets.QPushButton(self.openSettingsFileFrame)
        self.openValiditySettingsFileButton.setObjectName("openValiditySettingsFileButton")
        self.verticalLayout.addWidget(self.openValiditySettingsFileButton)
        self.recentValiditySettingsFileFrame = QtWidgets.QFrame(self.openSettingsFileFrame)
        self.recentValiditySettingsFileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recentValiditySettingsFileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.recentValiditySettingsFileFrame.setObjectName("recentValiditySettingsFileFrame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.recentValiditySettingsFileFrame)
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.openRecentValiditySettingsFileLabel = QtWidgets.QLabel(self.recentValiditySettingsFileFrame)
        self.openRecentValiditySettingsFileLabel.setEnabled(False)
        self.openRecentValiditySettingsFileLabel.setObjectName("openRecentValiditySettingsFileLabel")
        self.verticalLayout_14.addWidget(self.openRecentValiditySettingsFileLabel)
        self.selectRecentValiditySettingsFileComboBox = QtWidgets.QComboBox(self.recentValiditySettingsFileFrame)
        self.selectRecentValiditySettingsFileComboBox.setCurrentText("")
        self.selectRecentValiditySettingsFileComboBox.setObjectName("selectRecentValiditySettingsFileComboBox")
        self.verticalLayout_14.addWidget(self.selectRecentValiditySettingsFileComboBox)
        self.openRecentValiditySettingsFileButton = QtWidgets.QPushButton(self.recentValiditySettingsFileFrame)
        self.openRecentValiditySettingsFileButton.setEnabled(False)
        self.openRecentValiditySettingsFileButton.setObjectName("openRecentValiditySettingsFileButton")
        self.verticalLayout_14.addWidget(self.openRecentValiditySettingsFileButton)
        self.verticalLayout.addWidget(self.recentValiditySettingsFileFrame)
        self.horizontalLayout.addWidget(self.openSettingsFileFrame)
        self.gridLayout_2.addWidget(self.fileGroupBox, 0, 0, 1, 3)
        self.settingsGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.settingsGroupBox.setEnabled(False)
        self.settingsGroupBox.setMaximumSize(QtCore.QSize(440, 16777215))
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.fileLocationFrame = QtWidgets.QFrame(self.settingsGroupBox)
        self.fileLocationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileLocationFrame.setObjectName("fileLocationFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fileLocationFrame)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dataFileWidget = QtWidgets.QWidget(self.fileLocationFrame)
        self.dataFileWidget.setObjectName("dataFileWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dataFileWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dataFileLocationLabel = QtWidgets.QLabel(self.dataFileWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFileLocationLabel.sizePolicy().hasHeightForWidth())
        self.dataFileLocationLabel.setSizePolicy(sizePolicy)
        self.dataFileLocationLabel.setScaledContents(False)
        self.dataFileLocationLabel.setObjectName("dataFileLocationLabel")
        self.verticalLayout_2.addWidget(self.dataFileLocationLabel)
        self.data_file_location_label = QtWidgets.QLineEdit(self.dataFileWidget)
        self.data_file_location_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.data_file_location_label.setReadOnly(True)
        self.data_file_location_label.setObjectName("data_file_location_label")
        self.verticalLayout_2.addWidget(self.data_file_location_label)
        self.verticalLayout_9.addWidget(self.dataFileWidget)
        self.validitySettingsFileWidget = QtWidgets.QWidget(self.fileLocationFrame)
        self.validitySettingsFileWidget.setObjectName("validitySettingsFileWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.validitySettingsFileWidget)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.validitySettingsFileLocationLabel = QtWidgets.QLabel(self.validitySettingsFileWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validitySettingsFileLocationLabel.sizePolicy().hasHeightForWidth())
        self.validitySettingsFileLocationLabel.setSizePolicy(sizePolicy)
        self.validitySettingsFileLocationLabel.setScaledContents(False)
        self.validitySettingsFileLocationLabel.setObjectName("validitySettingsFileLocationLabel")
        self.verticalLayout_3.addWidget(self.validitySettingsFileLocationLabel)
        self.validity_settings_file_location_label = QtWidgets.QLineEdit(self.validitySettingsFileWidget)
        self.validity_settings_file_location_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.validity_settings_file_location_label.setReadOnly(True)
        self.validity_settings_file_location_label.setObjectName("validity_settings_file_location_label")
        self.verticalLayout_3.addWidget(self.validity_settings_file_location_label)
        self.verticalLayout_9.addWidget(self.validitySettingsFileWidget)
        self.verticalLayout_10.addWidget(self.fileLocationFrame)
        self.setupDataOptionsLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.setupDataOptionsLabel.setObjectName("setupDataOptionsLabel")
        self.verticalLayout_10.addWidget(self.setupDataOptionsLabel, 0, QtCore.Qt.AlignHCenter)
        self.rowColumnSelect = QtWidgets.QWidget(self.settingsGroupBox)
        self.rowColumnSelect.setObjectName("rowColumnSelect")
        self.gridLayout = QtWidgets.QGridLayout(self.rowColumnSelect)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.open_question_select = QtWidgets.QPushButton(self.rowColumnSelect)
        self.open_question_select.setEnabled(False)
        self.open_question_select.setObjectName("open_question_select")
        self.gridLayout.addWidget(self.open_question_select, 4, 0, 1, 1)
        self.open_date_select = QtWidgets.QPushButton(self.rowColumnSelect)
        self.open_date_select.setEnabled(False)
        self.open_date_select.setObjectName("open_date_select")
        self.gridLayout.addWidget(self.open_date_select, 3, 0, 1, 1)
        self.open_remove_rows = QtWidgets.QPushButton(self.rowColumnSelect)
        self.open_remove_rows.setEnabled(False)
        self.open_remove_rows.setAutoFillBackground(False)
        self.open_remove_rows.setObjectName("open_remove_rows")
        self.gridLayout.addWidget(self.open_remove_rows, 0, 0, 1, 1)
        self.open_response_select = QtWidgets.QPushButton(self.rowColumnSelect)
        self.open_response_select.setEnabled(False)
        self.open_response_select.setObjectName("open_response_select")
        self.gridLayout.addWidget(self.open_response_select, 5, 0, 1, 1)
        self.open_header_select = QtWidgets.QPushButton(self.rowColumnSelect)
        self.open_header_select.setEnabled(False)
        self.open_header_select.setObjectName("open_header_select")
        self.gridLayout.addWidget(self.open_header_select, 1, 0, 1, 1)
        self.open_subject_select = QtWidgets.QPushButton(self.rowColumnSelect)
        self.open_subject_select.setEnabled(False)
        self.open_subject_select.setObjectName("open_subject_select")
        self.gridLayout.addWidget(self.open_subject_select, 2, 0, 1, 1)
        self.removeRowsCheckBox = QtWidgets.QCheckBox(self.rowColumnSelect)
        self.removeRowsCheckBox.setEnabled(False)
        self.removeRowsCheckBox.setObjectName("removeRowsCheckBox")
        self.gridLayout.addWidget(self.removeRowsCheckBox, 0, 1, 1, 1)
        self.headersCheckBox = QtWidgets.QCheckBox(self.rowColumnSelect)
        self.headersCheckBox.setEnabled(False)
        self.headersCheckBox.setText("")
        self.headersCheckBox.setObjectName("headersCheckBox")
        self.gridLayout.addWidget(self.headersCheckBox, 1, 1, 1, 1)
        self.subjectCheckBox = QtWidgets.QCheckBox(self.rowColumnSelect)
        self.subjectCheckBox.setEnabled(False)
        self.subjectCheckBox.setText("")
        self.subjectCheckBox.setObjectName("subjectCheckBox")
        self.gridLayout.addWidget(self.subjectCheckBox, 2, 1, 1, 1)
        self.dateCheckBox = QtWidgets.QCheckBox(self.rowColumnSelect)
        self.dateCheckBox.setEnabled(False)
        self.dateCheckBox.setText("")
        self.dateCheckBox.setObjectName("dateCheckBox")
        self.gridLayout.addWidget(self.dateCheckBox, 3, 1, 1, 1)
        self.questionsCheckBox = QtWidgets.QCheckBox(self.rowColumnSelect)
        self.questionsCheckBox.setEnabled(False)
        self.questionsCheckBox.setText("")
        self.questionsCheckBox.setObjectName("questionsCheckBox")
        self.gridLayout.addWidget(self.questionsCheckBox, 4, 1, 1, 1)
        self.responsesCheckBox = QtWidgets.QCheckBox(self.rowColumnSelect)
        self.responsesCheckBox.setEnabled(False)
        self.responsesCheckBox.setText("")
        self.responsesCheckBox.setObjectName("responsesCheckBox")
        self.gridLayout.addWidget(self.responsesCheckBox, 5, 1, 1, 1)
        self.skipRemoveRows = QtWidgets.QPushButton(self.rowColumnSelect)
        self.skipRemoveRows.setObjectName("skipRemoveRows")
        self.gridLayout.addWidget(self.skipRemoveRows, 0, 2, 1, 1)
        self.skipDateSelect = QtWidgets.QPushButton(self.rowColumnSelect)
        self.skipDateSelect.setObjectName("skipDateSelect")
        self.gridLayout.addWidget(self.skipDateSelect, 3, 2, 1, 1)
        self.verticalLayout_10.addWidget(self.rowColumnSelect, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(self.settingsGroupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.clearSettings = QtWidgets.QPushButton(self.settingsGroupBox)
        self.clearSettings.setEnabled(False)
        self.clearSettings.setObjectName("clearSettings")
        self.verticalLayout_10.addWidget(self.clearSettings)
        self.line = QtWidgets.QFrame(self.settingsGroupBox)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setMidLineWidth(-2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_10.addWidget(self.line)
        self.validitySaveExport = QtWidgets.QFrame(self.settingsGroupBox)
        self.validitySaveExport.setEnabled(False)
        self.validitySaveExport.setObjectName("validitySaveExport")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.validitySaveExport)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.saveSettingsButton = QtWidgets.QPushButton(self.validitySaveExport)
        self.saveSettingsButton.setFlat(False)
        self.saveSettingsButton.setObjectName("saveSettingsButton")
        self.verticalLayout_5.addWidget(self.saveSettingsButton)
        self.exportValidityReportButton = QtWidgets.QPushButton(self.validitySaveExport)
        self.exportValidityReportButton.setObjectName("exportValidityReportButton")
        self.verticalLayout_5.addWidget(self.exportValidityReportButton)
        self.verticalLayout_10.addWidget(self.validitySaveExport)
        self.gridLayout_2.addWidget(self.settingsGroupBox, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 793, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpenDataFile = QtWidgets.QAction(MainWindow)
        self.actionOpenDataFile.setAutoRepeat(False)
        self.actionOpenDataFile.setObjectName("actionOpenDataFile")
        self.actionOpenSettingsFile = QtWidgets.QAction(MainWindow)
        self.actionOpenSettingsFile.setObjectName("actionOpenSettingsFile")
        self.actionSaveSettingsFile = QtWidgets.QAction(MainWindow)
        self.actionSaveSettingsFile.setObjectName("actionSaveSettingsFile")
        self.actionExportValidityReport = QtWidgets.QAction(MainWindow)
        self.actionExportValidityReport.setObjectName("actionExportValidityReport")
        self.actionClearSettings = QtWidgets.QAction(MainWindow)
        self.actionClearSettings.setObjectName("actionClearSettings")
        self.actionClearSettingsData = QtWidgets.QAction(MainWindow)
        self.actionClearSettingsData.setObjectName("actionClearSettingsData")
        self.actionClearRecentFiles = QtWidgets.QAction(MainWindow)
        self.actionClearRecentFiles.setObjectName("actionClearRecentFiles")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFiles.addAction(self.actionOpenDataFile)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionOpenSettingsFile)
        self.menuFiles.addAction(self.actionSaveSettingsFile)
        self.menuFiles.addAction(self.actionExportValidityReport)
        self.menuFiles.addSeparator()
        self.menuOptions.addAction(self.actionClearSettings)
        self.menuOptions.addAction(self.actionClearSettingsData)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionClearRecentFiles)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpenDataFile.triggered.connect(self.openDataFileButton.click)
        self.actionOpenSettingsFile.triggered.connect(self.openValiditySettingsFileButton.click)
        self.actionClearSettings.triggered.connect(self.clearSettings.click)
        self.actionSaveSettingsFile.triggered.connect(self.saveSettingsButton.click)
        self.actionExportValidityReport.triggered.connect(self.exportValidityReportButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.selectRecentDataFileComboBox, self.openRecentDataFileButton)
        MainWindow.setTabOrder(self.openRecentDataFileButton, self.selectRecentValiditySettingsFileComboBox)
        MainWindow.setTabOrder(self.selectRecentValiditySettingsFileComboBox, self.openRecentValiditySettingsFileButton)
        MainWindow.setTabOrder(self.openRecentValiditySettingsFileButton, self.open_remove_rows)
        MainWindow.setTabOrder(self.open_remove_rows, self.open_header_select)
        MainWindow.setTabOrder(self.open_header_select, self.open_subject_select)
        MainWindow.setTabOrder(self.open_subject_select, self.open_date_select)
        MainWindow.setTabOrder(self.open_date_select, self.saveSettingsButton)
        MainWindow.setTabOrder(self.saveSettingsButton, self.exportValidityReportButton)
        MainWindow.setTabOrder(self.exportValidityReportButton, self.rawTableView)
        MainWindow.setTabOrder(self.rawTableView, self.validityReportTableView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validity Checker"))
        self.dataGroupBox.setTitle(_translate("MainWindow", "Data"))
        self.rawDataFileNameLabel.setText(_translate("MainWindow", "Original Data"))
        self.validityReportLabel.setText(_translate("MainWindow", "Validity Checking Data"))
        self.fileGroupBox.setTitle(_translate("MainWindow", "Files"))
        self.openDataFileButton.setText(_translate("MainWindow", "Open data file..."))
        self.openRecentDataFileLabel.setText(_translate("MainWindow", "Select recent data file..."))
        self.openRecentDataFileButton.setText(_translate("MainWindow", "Open Selected Data File"))
        self.openValiditySettingsFileButton.setText(_translate("MainWindow", "Open settings file..."))
        self.openRecentValiditySettingsFileLabel.setText(_translate("MainWindow", "Open recent settings files..."))
        self.openRecentValiditySettingsFileButton.setText(_translate("MainWindow", "Open Selected Settings File"))
        self.settingsGroupBox.setTitle(_translate("MainWindow", "Settings"))
        self.dataFileLocationLabel.setText(_translate("MainWindow", "Current Data File Location:"))
        self.data_file_location_label.setPlaceholderText(_translate("MainWindow", "No data file currently open"))
        self.validitySettingsFileLocationLabel.setText(_translate("MainWindow", "Current Settings File Location:"))
        self.validity_settings_file_location_label.setPlaceholderText(_translate("MainWindow", "No settings file currently open"))
        self.setupDataOptionsLabel.setText(_translate("MainWindow", "Setup Validity Settings"))
        self.open_question_select.setText(_translate("MainWindow", "Select validity questions..."))
        self.open_date_select.setText(_translate("MainWindow", "Select column with date info (for sorting)"))
        self.open_remove_rows.setText(_translate("MainWindow", "Remove rows..."))
        self.open_response_select.setText(_translate("MainWindow", "Select validity responses..."))
        self.open_header_select.setText(_translate("MainWindow", "Select row with headers..."))
        self.open_subject_select.setText(_translate("MainWindow", "Select column with subject ID\'s"))
        self.skipRemoveRows.setText(_translate("MainWindow", "Skip"))
        self.skipDateSelect.setText(_translate("MainWindow", "Skip"))
        self.clearSettings.setText(_translate("MainWindow", "Clear settings"))
        self.saveSettingsButton.setText(_translate("MainWindow", "Save settings..."))
        self.exportValidityReportButton.setText(_translate("MainWindow", "Export validity report..."))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpenDataFile.setText(_translate("MainWindow", "Open data file (.csv)..."))
        self.actionOpenDataFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenSettingsFile.setText(_translate("MainWindow", "Open settings file (.json)..."))
        self.actionOpenSettingsFile.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionSaveSettingsFile.setText(_translate("MainWindow", "Save settings file (.json)..."))
        self.actionSaveSettingsFile.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExportValidityReport.setText(_translate("MainWindow", "Export validity report (.csv)..."))
        self.actionExportValidityReport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionClearSettings.setText(_translate("MainWindow", "Clear settings"))
        self.actionClearSettings.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
        self.actionClearSettingsData.setText(_translate("MainWindow", "Clear settings and data"))
        self.actionClearSettingsData.setShortcut(_translate("MainWindow", "Ctrl+Shift+Backspace"))
        self.actionClearRecentFiles.setText(_translate("MainWindow", "Clear recent files"))
        self.actionClearRecentFiles.setShortcut(_translate("MainWindow", "Ctrl+Alt+Backspace"))
        self.actionAbout.setText(_translate("MainWindow", "About Validity Checker..."))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
