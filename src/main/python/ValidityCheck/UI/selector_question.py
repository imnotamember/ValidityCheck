# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdf/PycharmProjects/validitychecker/UI/selector_question.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_question_selector(object):
    def setupUi(self, question_selector):
        question_selector.setObjectName("question_selector")
        question_selector.setWindowModality(QtCore.Qt.ApplicationModal)
        question_selector.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(question_selector.sizePolicy().hasHeightForWidth())
        question_selector.setSizePolicy(sizePolicy)
        question_selector.setMinimumSize(QtCore.QSize(400, 300))
        question_selector.setMaximumSize(QtCore.QSize(400, 600))
        question_selector.setFocusPolicy(QtCore.Qt.StrongFocus)
        question_selector.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        question_selector.setAutoFillBackground(False)
        question_selector.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(question_selector)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(6, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(question_selector)
        self.buttonBox.accepted.connect(question_selector.accept)
        self.buttonBox.rejected.connect(question_selector.reject)
        QtCore.QMetaObject.connectSlotsByName(question_selector)

    def retranslateUi(self, question_selector):
        _translate = QtCore.QCoreApplication.translate
        question_selector.setWindowTitle(_translate("question_selector", "Select Validity Questions to Analyze"))
        self.label.setText(_translate("question_selector", "Select from the following items:"))
