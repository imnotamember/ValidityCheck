# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdf/PycharmProjects/validitychecker/UI/selector_response.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_response_selector(object):
    def setupUi(self, response_selector):
        response_selector.setObjectName("response_selector")
        response_selector.setWindowModality(QtCore.Qt.ApplicationModal)
        response_selector.resize(559, 300)
        response_selector.setModal(True)
        self.gridLayoutWidget = QtWidgets.QWidget(response_selector)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 19, 521, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(response_selector)
        self.buttonBox.accepted.connect(response_selector.accept)
        self.buttonBox.rejected.connect(response_selector.reject)
        QtCore.QMetaObject.connectSlotsByName(response_selector)

    def retranslateUi(self, response_selector):
        _translate = QtCore.QCoreApplication.translate
        response_selector.setWindowTitle(_translate("response_selector", "Select Validity Questions\' Correct Responses"))
