# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdf/PycharmProjects/validitychecker/UI/selector_column.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_column_selector(object):
    def setupUi(self, column_selector):
        column_selector.setObjectName("column_selector")
        column_selector.setWindowModality(QtCore.Qt.ApplicationModal)
        column_selector.resize(580, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(column_selector.sizePolicy().hasHeightForWidth())
        column_selector.setSizePolicy(sizePolicy)
        column_selector.setMinimumSize(QtCore.QSize(580, 300))
        column_selector.setMaximumSize(QtCore.QSize(580, 300))
        column_selector.setBaseSize(QtCore.QSize(580, 300))
        column_selector.setToolTipDuration(-4)
        column_selector.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(column_selector)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(column_selector)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(column_selector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(81, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(column_selector)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView.setWordWrap(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(column_selector)
        self.buttonBox.accepted.connect(column_selector.accept)
        self.buttonBox.rejected.connect(column_selector.reject)
        QtCore.QMetaObject.connectSlotsByName(column_selector)

    def retranslateUi(self, column_selector):
        _translate = QtCore.QCoreApplication.translate
        column_selector.setWindowTitle(_translate("column_selector", "Select column..."))
        self.label.setText(_translate("column_selector", "Select the column of interest:"))
