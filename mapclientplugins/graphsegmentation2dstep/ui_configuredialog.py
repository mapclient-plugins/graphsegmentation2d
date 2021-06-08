# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc
from  . import resources_rc

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(490, 470)
        self.verticalLayoutMain = QVBoxLayout(ConfigureDialog)
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout = QGridLayout(self.configGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.gridLayout.addWidget(self.label0, 0, 0, 1, 1)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.gridLayout.addWidget(self.lineEdit0, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.configGroupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutData = QVBoxLayout(self.groupBox)
        self.verticalLayoutData.setObjectName(u"verticalLayoutData")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutData.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAdd = QPushButton(self.groupBox)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        icon = QIcon()
        icon.addFile(u":/graphsegmentation2dstep/images/Action-edit-add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAdd.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButtonAdd)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayoutData.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)


        self.verticalLayoutMain.addWidget(self.configGroupBox)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayoutMain.addWidget(self.buttonBox)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConfigureDialog", u"Data", None))
        self.pushButtonAdd.setText("")
    # retranslateUi

