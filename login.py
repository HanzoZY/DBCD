# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWin(object):
    def setupUi(self, LoginWin):
        LoginWin.setObjectName("LoginWin")
        LoginWin.setWindowModality(QtCore.Qt.NonModal)
        LoginWin.setEnabled(True)
        LoginWin.resize(354, 218)
        LoginWin.setMinimumSize(QtCore.QSize(354, 218))
        LoginWin.setMaximumSize(QtCore.QSize(354, 218))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("idol.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWin.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(LoginWin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 20, 161, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(4, 5, 0, 0)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UserName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.UserName.setEnabled(True)
        self.UserName.setObjectName("UserName")
        self.verticalLayout.addWidget(self.UserName)
        self.Passwd = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Passwd.setObjectName("Passwd")
        self.verticalLayout.addWidget(self.Passwd)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(LoginWin)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 20, 51, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginWin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelB = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CancelB.setObjectName("CancelB")
        self.horizontalLayout.addWidget(self.CancelB)
        self.loginB = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginB.setObjectName("loginB")
        self.horizontalLayout.addWidget(self.loginB)
        self.LogImage = QtWidgets.QLabel(LoginWin)
        self.LogImage.setGeometry(QtCore.QRect(20, 30, 91, 91))
        self.LogImage.setText("")
        self.LogImage.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.LogImage.setObjectName("LogImage")

        self.retranslateUi(LoginWin)
        self.loginB.clicked.connect(LoginWin.login)
        self.CancelB.clicked.connect(LoginWin.close)
        QtCore.QMetaObject.connectSlotsByName(LoginWin)

    def retranslateUi(self, LoginWin):
        _translate = QtCore.QCoreApplication.translate
        LoginWin.setWindowTitle(_translate("LoginWin", "工资管理"))
        self.label.setText(_translate("LoginWin", "用户名"))
        self.label_2.setText(_translate("LoginWin", "密   码"))
        self.CancelB.setText(_translate("LoginWin", "退出"))
        self.loginB.setText(_translate("LoginWin", "登录"))


