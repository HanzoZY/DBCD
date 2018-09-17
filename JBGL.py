# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JBGL.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JBGL_M(object):
    def setupUi(self, JBGL_M):
        JBGL_M.setObjectName("JBGL_M")
        JBGL_M.setEnabled(True)
        JBGL_M.resize(600, 450)
        JBGL_M.setMinimumSize(QtCore.QSize(600, 450))
        JBGL_M.setMaximumSize(QtCore.QSize(600, 450))
        self.frame = QtWidgets.QFrame(JBGL_M)
        self.frame.setGeometry(QtCore.QRect(200, 20, 391, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 61, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 10, 67, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.GH_L = QtWidgets.QLineEdit(self.frame)
        self.GH_L.setGeometry(QtCore.QRect(80, 81, 101, 21))
        self.GH_L.setObjectName("GH_L")
        self.XM_L = QtWidgets.QLineEdit(self.frame)
        self.XM_L.setGeometry(QtCore.QRect(80, 256, 101, 21))
        self.XM_L.setObjectName("XM_L")
        self.RQ_E = QtWidgets.QDateEdit(self.frame)
        self.RQ_E.setGeometry(QtCore.QRect(270, 80, 110, 24))
        self.RQ_E.setDate(QtCore.QDate(2018, 3, 1))
        self.RQ_E.setObjectName("RQ_E")
        self.JB_Box = QtWidgets.QSpinBox(self.frame)
        self.JB_Box.setGeometry(QtCore.QRect(270, 256, 111, 24))
        self.JB_Box.setMinimum(1)
        self.JB_Box.setMaximum(9)
        self.JB_Box.setObjectName("JB_Box")
        self.Cancal = QtWidgets.QPushButton(JBGL_M)
        self.Cancal.setGeometry(QtCore.QRect(60, 390, 150, 50))
        self.Cancal.setStyleSheet("font: 75 14pt \"Heiti SC\";")
        self.Cancal.setObjectName("Cancal")
        self.Photo_B = QtWidgets.QPushButton(JBGL_M)
        self.Photo_B.setGeometry(QtCore.QRect(10, 100, 181, 181))
        self.Photo_B.setText("")
        self.Photo_B.setObjectName("Photo_B")
        self.Sure = QtWidgets.QPushButton(JBGL_M)
        self.Sure.setGeometry(QtCore.QRect(410, 390, 150, 50))
        self.Sure.setObjectName("Sure")

        self.retranslateUi(JBGL_M)
        QtCore.QMetaObject.connectSlotsByName(JBGL_M)

    def retranslateUi(self, JBGL_M):
        _translate = QtCore.QCoreApplication.translate
        JBGL_M.setWindowTitle(_translate("JBGL_M", "JBGL"))
        self.label.setText(_translate("JBGL_M", "工号："))
        self.label_2.setText(_translate("JBGL_M", "姓名："))
        self.label_3.setText(_translate("JBGL_M", "日期："))
        self.label_8.setText(_translate("JBGL_M", "加班时长："))
        self.Cancal.setText(_translate("JBGL_M", "返回"))
        self.Sure.setText(_translate("JBGL_M", "确认"))

