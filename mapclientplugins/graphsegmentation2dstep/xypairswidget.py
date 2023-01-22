from PySide6 import QtGui, QtWidgets
from mapclientplugins.graphsegmentation2dstep.ui_xypairswidget import Ui_XYPairsWidget


class XYPairsWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(XYPairsWidget, self).__init__(parent)

        self._ui = Ui_XYPairsWidget()
        self._ui.setupUi(self)
        self._ui.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)

        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonAdd.clicked.connect(self._addClicked)

    def _addClicked(self):
        index = self._ui.horizontalLayout.indexOf(self._ui.pushButtonAdd)
        label_1 = QtWidgets.QLabel(self._ui.scrollAreaWidgetContents)
        label_1.setText("(")
        self._ui.horizontalLayout.insertWidget(index + 0, label_1)
        doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self._ui.scrollAreaWidgetContents)
        doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        doubleSpinBox_2.setMinimum(-999999999.99)
        doubleSpinBox_2.setMaximum(999999999.99)
        self._ui.horizontalLayout.insertWidget(index + 1, doubleSpinBox_2)
        label_3 = QtWidgets.QLabel(self._ui.scrollAreaWidgetContents)
        label_3.setText(",")
        self._ui.horizontalLayout.insertWidget(index + 2, label_3)
        doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self._ui.scrollAreaWidgetContents)
        doubleSpinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        doubleSpinBox_4.setMinimum(-999999999.99)
        doubleSpinBox_4.setMaximum(999999999.99)
        self._ui.horizontalLayout.insertWidget(index + 3, doubleSpinBox_4)
        label_5 = QtWidgets.QLabel(self._ui.scrollAreaWidgetContents)
        label_5.setText(")")
        self._ui.horizontalLayout.insertWidget(index + 4, label_5)
        label_6 = QtWidgets.QLabel(self._ui.scrollAreaWidgetContents)
        label_6.setText(",")
        self._ui.horizontalLayout.insertWidget(index + 5, label_6)

    def _getDoubleSpinBoxes(self):
        kids = self._ui.scrollAreaWidgetContents.children()
        spin_boxes = []
        for child in kids:
            if type(child) == QtWidgets.QDoubleSpinBox:
                spin_boxes.append(child)

        return spin_boxes

    def setData(self, data):
        spin_boxes = self._getDoubleSpinBoxes()

        while len(data) < len(spin_boxes):
            pass

        while len(spin_boxes) < len(data):
            self._addClicked()
            spin_boxes = self._getDoubleSpinBoxes()

        for index, spine_box in enumerate(spin_boxes):
            spine_box.setValue(data[index])

    def getData(self):
        data = []
        spin_boxes = self._getDoubleSpinBoxes()
        for spin_box in spin_boxes:
            data.append(spin_box.value())

        return data
