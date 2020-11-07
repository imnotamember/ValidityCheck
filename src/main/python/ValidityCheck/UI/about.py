# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdf/PycharmProjects/ValidityCheck/src/main/resources/base/about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.WindowModal)
        About.resize(536, 286)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(About)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.centralWidget = QtWidgets.QWidget(About)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appName = QtWidgets.QLabel(self.centralWidget)
        self.appName.setOpenExternalLinks(True)
        self.appName.setObjectName("appName")
        self.verticalLayout.addWidget(self.appName)
        self.developerName = QtWidgets.QLabel(self.centralWidget)
        self.developerName.setOpenExternalLinks(True)
        self.developerName.setObjectName("developerName")
        self.verticalLayout.addWidget(self.developerName)
        self.email = QtWidgets.QLabel(self.centralWidget)
        self.email.setOpenExternalLinks(True)
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.website = QtWidgets.QLabel(self.centralWidget)
        self.website.setOpenExternalLinks(True)
        self.website.setObjectName("website")
        self.verticalLayout.addWidget(self.website)
        self.license = QtWidgets.QLabel(self.centralWidget)
        self.license.setOpenExternalLinks(True)
        self.license.setObjectName("license")
        self.verticalLayout.addWidget(self.license)
        self.resourcesLabel = QtWidgets.QLabel(self.centralWidget)
        self.resourcesLabel.setOpenExternalLinks(True)
        self.resourcesLabel.setObjectName("resourcesLabel")
        self.verticalLayout.addWidget(self.resourcesLabel)
        self.resourcesListing = QtWidgets.QLabel(self.centralWidget)
        self.resourcesListing.setWordWrap(True)
        self.resourcesListing.setOpenExternalLinks(True)
        self.resourcesListing.setObjectName("resourcesListing")
        self.verticalLayout.addWidget(self.resourcesListing)
        self.verticalLayout_2.addWidget(self.centralWidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Validity Check"))
        self.appName.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Validity Check</span></p></body></html>"))
        self.developerName.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600;\">Developed by: Joshua E. Zosky</span></p></body></html>"))
        self.email.setText(_translate("About", "<html><head/><body><p><a href=\"mailto:joshua.e.zosky@gmail.com\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">joshua.e.zosky@gmail.com</span></a></p></body></html>"))
        self.website.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600;\">Developer\'s website: </span><a href=\"https://imnotamember.github.io/\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">https://imnotamember.github.io/</span></a></p></body></html>"))
        self.license.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600;\">This software is open-source, licensed under the </span><a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">GPLv3 License</span></a><span style=\" font-weight:600;\"> (November 2020)</span></p></body></html>"))
        self.resourcesLabel.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Resources</span></p></body></html>"))
        self.resourcesListing.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">fbs: compiling standalone app</span></p><p><span style=\" font-size:10pt; font-weight:600;\">PyQt: GUI</span></p><p><span style=\" font-size:10pt; font-weight:600;\">QtModern: better looking UI</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Pandas: data processing</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Thank you!</span></p></body></html>"))
