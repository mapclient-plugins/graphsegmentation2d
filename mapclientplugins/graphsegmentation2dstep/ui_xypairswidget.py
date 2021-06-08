# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xypairswidget.ui'
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

class Ui_XYPairsWidget(object):
    def setupUi(self, XYPairsWidget):
        if not XYPairsWidget.objectName():
            XYPairsWidget.setObjectName(u"XYPairsWidget")
        XYPairsWidget.resize(553, 87)
        self.verticalLayout = QVBoxLayout(XYPairsWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(XYPairsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-523, 0, 1074, 64))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_3.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_3)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_4.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_4.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_4)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_5.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_5.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_5)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_6.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_6.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_6)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_7.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_7.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_7)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout.addWidget(self.label_16)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_8.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_8.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_8)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout.addWidget(self.label_15)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_9.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_9.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_9)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout.addWidget(self.label_17)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_10.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_10.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_10)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout.addWidget(self.label_18)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_11.setMinimum(-999999999.990000009536743)
        self.doubleSpinBox_11.setMaximum(999999999.990000009536743)

        self.horizontalLayout.addWidget(self.doubleSpinBox_11)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout.addWidget(self.label_19)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout.addWidget(self.label_20)

        self.pushButtonAdd = QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        icon = QIcon()
        icon.addFile(u":/plotsettingsstep/images/Action-edit-add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAdd.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButtonAdd)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(XYPairsWidget)

        QMetaObject.connectSlotsByName(XYPairsWidget)
    # setupUi

    def retranslateUi(self, XYPairsWidget):
        XYPairsWidget.setWindowTitle(QCoreApplication.translate("XYPairsWidget", u"XY Pairs", None))
        self.label.setText(QCoreApplication.translate("XYPairsWidget", u"(", None))
        self.label_2.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_3.setText(QCoreApplication.translate("XYPairsWidget", u")", None))
        self.label_4.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_6.setText(QCoreApplication.translate("XYPairsWidget", u"(", None))
        self.label_7.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_8.setText(QCoreApplication.translate("XYPairsWidget", u")", None))
        self.label_5.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_9.setText(QCoreApplication.translate("XYPairsWidget", u"(", None))
        self.label_11.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_12.setText(QCoreApplication.translate("XYPairsWidget", u")", None))
        self.label_10.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_16.setText(QCoreApplication.translate("XYPairsWidget", u"(", None))
        self.label_15.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_13.setText(QCoreApplication.translate("XYPairsWidget", u")", None))
        self.label_14.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_17.setText(QCoreApplication.translate("XYPairsWidget", u"(", None))
        self.label_18.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.label_19.setText(QCoreApplication.translate("XYPairsWidget", u")", None))
        self.label_20.setText(QCoreApplication.translate("XYPairsWidget", u",", None))
        self.pushButtonAdd.setText("")
    # retranslateUi

