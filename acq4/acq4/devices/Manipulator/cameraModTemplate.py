# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraModTemplate.ui'
#
# Created: Tue Mar 31 21:04:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(138, 214)
        self.gridLayout_3 = QtGui.QGridLayout(Form)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.standbyBtn = QtGui.QPushButton(self.groupBox_2)
        self.standbyBtn.setEnabled(False)
        self.standbyBtn.setObjectName(_fromUtf8("standbyBtn"))
        self.gridLayout_2.addWidget(self.standbyBtn, 3, 0, 1, 1)
        self.targetBtn = QtGui.QPushButton(self.groupBox_2)
        self.targetBtn.setEnabled(False)
        self.targetBtn.setObjectName(_fromUtf8("targetBtn"))
        self.gridLayout_2.addWidget(self.targetBtn, 4, 0, 1, 1)
        self.setTargetBtn = QtGui.QPushButton(self.groupBox_2)
        self.setTargetBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.setTargetBtn.setCheckable(True)
        self.setTargetBtn.setObjectName(_fromUtf8("setTargetBtn"))
        self.gridLayout_2.addWidget(self.setTargetBtn, 4, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.slowRadio = QtGui.QRadioButton(self.groupBox_2)
        self.slowRadio.setChecked(True)
        self.slowRadio.setObjectName(_fromUtf8("slowRadio"))
        self.horizontalLayout.addWidget(self.slowRadio)
        self.fastRadio = QtGui.QRadioButton(self.groupBox_2)
        self.fastRadio.setObjectName(_fromUtf8("fastRadio"))
        self.horizontalLayout.addWidget(self.fastRadio)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.inBtn = QtGui.QPushButton(self.groupBox_2)
        self.inBtn.setObjectName(_fromUtf8("inBtn"))
        self.gridLayout_2.addWidget(self.inBtn, 2, 0, 1, 1)
        self.outBtn = QtGui.QPushButton(self.groupBox_2)
        self.outBtn.setObjectName(_fromUtf8("outBtn"))
        self.gridLayout_2.addWidget(self.outBtn, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setMargin(3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.setCenterBtn = QtGui.QPushButton(self.groupBox)
        self.setCenterBtn.setCheckable(True)
        self.setCenterBtn.setObjectName(_fromUtf8("setCenterBtn"))
        self.gridLayout.addWidget(self.setCenterBtn, 0, 0, 1, 1)
        self.setOrientationBtn = QtGui.QPushButton(self.groupBox)
        self.setOrientationBtn.setCheckable(True)
        self.setOrientationBtn.setObjectName(_fromUtf8("setOrientationBtn"))
        self.gridLayout.addWidget(self.setOrientationBtn, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_2.setTitle(_translate("Form", "Set points", None))
        self.standbyBtn.setText(_translate("Form", "Standby", None))
        self.targetBtn.setText(_translate("Form", "Target", None))
        self.setTargetBtn.setText(_translate("Form", "Set", None))
        self.slowRadio.setText(_translate("Form", "slow", None))
        self.fastRadio.setText(_translate("Form", "fast", None))
        self.inBtn.setText(_translate("Form", "Electrode In", None))
        self.outBtn.setText(_translate("Form", "Electrode Out", None))
        self.groupBox.setTitle(_translate("Form", "Calibration", None))
        self.setCenterBtn.setText(_translate("Form", "Set center", None))
        self.setOrientationBtn.setText(_translate("Form", "Set orientation", None))

