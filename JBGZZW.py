# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JBGZZW.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JBGZ_ZW(object):
    def setupUi(self, JBGZ_ZW):
        JBGZ_ZW.setObjectName("JBGZ_ZW")
        JBGZ_ZW.setEnabled(True)
        JBGZ_ZW.resize(400, 300)
        JBGZ_ZW.setMinimumSize(QtCore.QSize(400, 300))
        JBGZ_ZW.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(JBGZ_ZW)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(JBGZ_ZW)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(JBGZ_ZW)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(JBGZ_ZW)
        self.label_4.setGeometry(QtCore.QRect(205, 20, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(JBGZ_ZW)
        self.label_5.setGeometry(QtCore.QRect(205, 90, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(JBGZ_ZW)
        self.label_6.setGeometry(QtCore.QRect(205, 160, 60, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(JBGZ_ZW)
        self.lineEdit.setGeometry(QtCore.QRect(85, 20, 95, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(JBGZ_ZW)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 20, 95, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.spinBox = QtWidgets.QSpinBox(JBGZ_ZW)
        self.spinBox.setGeometry(QtCore.QRect(85, 90, 113, 24))
        self.spinBox.setMaximum(100000)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(JBGZ_ZW)
        self.spinBox_2.setGeometry(QtCore.QRect(270, 90, 113, 24))
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(JBGZ_ZW)
        self.spinBox_3.setGeometry(QtCore.QRect(85, 160, 113, 24))
        self.spinBox_3.setMaximum(100000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(JBGZ_ZW)
        self.spinBox_4.setGeometry(QtCore.QRect(270, 160, 113, 24))
        self.spinBox_4.setMaximum(100000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.pushButton = QtWidgets.QPushButton(JBGZ_ZW)
        self.pushButton.setGeometry(QtCore.QRect(50, 230, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(JBGZ_ZW)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 230, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(JBGZ_ZW)
        QtCore.QMetaObject.connectSlotsByName(JBGZ_ZW)

    def retranslateUi(self, JBGZ_ZW):
        _translate = QtCore.QCoreApplication.translate
        JBGZ_ZW.setWindowTitle(_translate("JBGZ_ZW", "基本工资(职位)"))
        self.label.setText(_translate("JBGZ_ZW", "职位编号："))
        self.label_2.setText(_translate("JBGZ_ZW", "基本工资："))
        self.label_3.setText(_translate("JBGZ_ZW", "早退扣罚："))
        self.label_4.setText(_translate("JBGZ_ZW", "职        位："))
        self.label_5.setText(_translate("JBGZ_ZW", "加班工资："))
        self.label_6.setText(_translate("JBGZ_ZW", "迟到扣罚"))
        self.pushButton.setText(_translate("JBGZ_ZW", "取消"))
        self.pushButton_2.setText(_translate("JBGZ_ZW", "确认"))

