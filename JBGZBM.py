# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JBGZBM.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JBGZBM_M(object):
    def setupUi(self, JBGZBM_M):
        JBGZBM_M.setObjectName("JBGZBM_M")
        JBGZBM_M.setEnabled(True)
        JBGZBM_M.resize(250, 300)
        JBGZBM_M.setMinimumSize(QtCore.QSize(250, 300))
        JBGZBM_M.setMaximumSize(QtCore.QSize(250, 300))
        self.label = QtWidgets.QLabel(JBGZBM_M)
        self.label.setGeometry(QtCore.QRect(20, 30, 60, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(JBGZBM_M)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(JBGZBM_M)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(JBGZBM_M)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(JBGZBM_M)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.spinBox = QtWidgets.QSpinBox(JBGZBM_M)
        self.spinBox.setGeometry(QtCore.QRect(110, 170, 118, 24))
        self.spinBox.setMaximum(100000)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(JBGZBM_M)
        self.pushButton.setGeometry(QtCore.QRect(133, 230, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(JBGZBM_M)
        self.pushButton_2.setGeometry(QtCore.QRect(14, 230, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(JBGZBM_M)
        QtCore.QMetaObject.connectSlotsByName(JBGZBM_M)

    def retranslateUi(self, JBGZBM_M):
        _translate = QtCore.QCoreApplication.translate
        JBGZBM_M.setWindowTitle(_translate("JBGZBM_M", "JBGZBM"))
        self.label.setText(_translate("JBGZBM_M", "部门编号："))
        self.label_2.setText(_translate("JBGZBM_M", "部       门："))
        self.label_3.setText(_translate("JBGZBM_M", "部门津贴："))
        self.pushButton.setText(_translate("JBGZBM_M", "确认"))
        self.pushButton_2.setText(_translate("JBGZBM_M", "取消"))

