# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdf/PycharmProjects/validitychecker/Source/selector_row.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_row_selector(object):
    def setupUi(self, row_selector):
        row_selector.setObjectName("row_selector")
        row_selector.resize(580, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(row_selector.sizePolicy().hasHeightForWidth())
        row_selector.setSizePolicy(sizePolicy)
        row_selector.setMinimumSize(QtCore.QSize(580, 300))
        row_selector.setMaximumSize(QtCore.QSize(580, 300))
        row_selector.setBaseSize(QtCore.QSize(580, 300))
        row_selector.setSizeGripEnabled(True)
        row_selector.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(row_selector)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(row_selector)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(row_selector)
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
        self.tableView = QtWidgets.QTableView(row_selector)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setHighlightSections(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(17)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.tableView.verticalHeader().setHighlightSections(True)
        self.tableView.verticalHeader().setSortIndicatorShown(True)
        self.tableView.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(row_selector)
        self.buttonBox.accepted.connect(row_selector.accept)
        self.buttonBox.rejected.connect(row_selector.reject)
        QtCore.QMetaObject.connectSlotsByName(row_selector)

    def retranslateUi(self, row_selector):
        _translate = QtCore.QCoreApplication.translate
        row_selector.setWindowTitle(_translate("row_selector", "Select row..."))
        self.label.setText(_translate("row_selector", "Select the row:"))
