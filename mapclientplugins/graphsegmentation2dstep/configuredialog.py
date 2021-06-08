

from PySide2 import QtGui, QtWidgets
from mapclientplugins.graphsegmentation2dstep.ui_configuredialog import Ui_ConfigureDialog
from mapclientplugins.graphsegmentation2dstep.xypairswidget import XYPairsWidget

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._data_rows = {}

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)
        self._ui.pushButtonAdd.clicked.connect(self._addClicked)

    def _addDataRow(self, text, data):
        l, b = _createDataRow(text, data, self._ui.groupBox)

        b.clicked.connect(self._removeClicked)
        self._data_rows[b] = l
        count = self._ui.verticalLayoutData.count()
        self._ui.verticalLayoutData.insertLayout(count - 2, l)

    def _addClicked(self):
        self._addDataRow('data', [0.00] * 10)

    def _removeClicked(self):
        b = self.sender()
        if b in self._data_rows:
            l = self._data_rows[b]
            while l.count():
                item = l.takeAt(0)
                w = item.widget()
                if item.widget():
                    w.hide()
                    w.deleteLater()

            del self._data_rows[b]
            l.deleteLater()

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        layout = self._ui.groupBox.layout()
        count = 0
        kids = layout.children()
        for child in kids:
            if child.count() == 3:
                label = child.itemAt(0).widget()
                xypairs = child.itemAt(1).widget()
                config[str(count)] = [label.text(), xypairs.getData()]
                count += 1

        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        datas = []
        for key in config:
            if key != 'identifier':
                values = config[key]
                try:
                    index = int(key)
                    len_datas = len(datas)
                    if index >= len_datas:
                        datas.extend([None] * (index - len_datas + 1))

                    datas[index] = values

                except ValueError as e:
                    pass

        assert(None not in datas)
        for p in datas:
            self._addDataRow(p[0], p[1])


def _createDataRow(text, data, parent):
    sizePolicyWidget = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
    sizePolicyWidget.setHorizontalStretch(0)
    sizePolicyWidget.setVerticalStretch(0)
    sizePolicyLabel = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicyLabel.setHorizontalStretch(0)
    sizePolicyLabel.setVerticalStretch(0)

    widget = XYPairsWidget(parent)
    sizePolicyWidget.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
    widget.setSizePolicy(sizePolicyWidget)
    widget.setData(data)

    label = QtWidgets.QLineEdit(parent)
    sizePolicyLabel.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
    label.setSizePolicy(sizePolicyLabel)
    label.setText(text)

    pushButton = QtWidgets.QPushButton(parent)
    pushButton.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/graphsegmentation2dstep/images/red_cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    pushButton.setIcon(icon)

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(widget)
    layout.addWidget(pushButton)

    return layout, pushButton
