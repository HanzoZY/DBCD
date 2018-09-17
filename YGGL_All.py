#-*- coding:utf-8 -*-
from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog, QPushButton, QMessageBox

from PyQt5 import QtGui,QtCore
from  YGGL import Ui_YGGL_M

import time




class YGGL_All(Ui_YGGL_M,QDialog):
    def __init__(self,StaffInfo,conn,YGGL_right=1):
        super(YGGL_All, self).__init__()
        self.setupUi(self)
        self.SC_B =QPushButton(self)
        self.SC_B.setGeometry(QtCore.QRect(30, 300, 150, 50))
        self.SC_B.setText("删除员工")

        self.Info=StaffInfo
        self.conn=conn
        self.Set_Info()
        self.signal_slot()
        self.File_Path=""
        self.GH_L.setEnabled(False)
        if YGGL_right==0:
            self.Disable()

    def time_refresh(self):

    def Set_Info(self):
        self.ComBox_init()
        self.ID=self.Info[0]
        Name=self.Info[1]
        WorkDay=self.Info[2]
        Position=self.Info[3]
        Photo=self.Info[5]

        #print(Photo)
        temp=str(Photo)
        Age=self.Info[6]
        Department=self.Info[7]
        LeaderID=self.Info[9]
        Sex=self.Info[10]
        LeaderName=""
        # command = "select Name from StaffInfo WHERE StaffID ='" + LeaderID + "';"
        # cursor = self.conn.cursor()
        # cursor.execute(command)
        # LeaderName = cursor.fetchone()[0]
        #print(LeaderName)
        cursor = self.conn.cursor()
        try:
            command="select Name from StaffInfo WHERE StaffID ='"+LeaderID+"';"
            cursor.execute(command)
            LeaderName+=cursor.fetchone()[0]
        except:
            print('no leader')
        try:
            self.LD_L.setText(LeaderName)
            self.GH_L.setText(self.ID)
            self.XM_L.setText(Name)
            self.NL_Box.setValue(Age)
            self.XB_Box.setCurrentText(Sex)
            self.BM_Box.setCurrentText(Department)
            self.ZW_Box.setCurrentText(Position)
            self.RZ_L.setDate(QDate.fromString(WorkDay.strftime("%Y-%m-%d"), 'yyyy-MM-dd'))
            pix_map = QtGui.QPixmap()
            flag = pix_map.loadFromData(QtCore.QByteArray(Photo))
            if flag:
                print('员工管理部分图片加载成功')
                self.Photo_B.setIcon(QIcon(pix_map))
                self.Photo_B.setIconSize(QSize(171, 171))
            else:
                print('图片加载失败')


        except:
            print ('员工管理部分查询失败')
        finally:
            cursor.close()

    def ComBox_init(self):
        self.BM_Box.addItem('管理层')
        self.BM_Box.addItem('人事部')
        self.BM_Box.addItem('财务部')
        self.BM_Box.addItem('产品部')
        self.XB_Box.addItem('男')
        self.XB_Box.addItem('女')
        self.ZW_Box.addItem('老板')
        self.ZW_Box.addItem('董事员')
        self.ZW_Box.addItem('经理')
        self.ZW_Box.addItem('主任')
        self.ZW_Box.addItem('科长')
        self.ZW_Box.addItem('科员')

    def Disable(self):
        self.LD_L.setEnabled(False)
        self.XM_L.setEnabled(False)
        self.NL_Box.setEnabled(False)
        self.XB_Box.setEnabled(False)
        self.BM_Box.setEnabled(False)
        self.ZW_Box.setEnabled(False)
        self.RZ_L.setEnabled(False)
        self.Photo_B.setEnabled(False)
        self.Sure.setEnabled(False)
        self.SC_B.setEnabled(False)



    def change_photo(self):

        try:
            self.File_Path,filetype=QFileDialog.getOpenFileName(self,"选取文件","/Users/zhangyuhan/Desktop/水浒头像","All Files (*);;Iamge Files (*.jpg);;Iamge Files (*.png);;Iamge Files (*.png)")
            del filetype
        except:
            print("开启文件选择器失败")
        if self.File_Path!="":
            self.Photo_B.setIcon(QIcon(QtGui.QPixmap(self.File_Path)))
            self.Photo_B.setIconSize(QSize(161,161))
    def Fanhui(self):
        self.close()
    def Queren(self):
        ID = "'" + self.GH_L.text() + "'"
        Name = "'" + self.XM_L.text() + "'"
        Age = self.NL_Box.text()
        Sex = "'" + self.XB_Box.currentText() + "'"
        Department = "'" + self.BM_Box.currentText() + "'"
        DepartmentID = ""
        Leader = "'" + self.LD_L.text() + "'"
        LeaderID = ''
        Position = "'" + self.ZW_Box.currentText() + "'"
        PositionID = ''
        RZ = self.RZ_L.text()
        print(RZ)
        RZ = "str_to_date('" + RZ + "','%Y/%m/%d')"
        doubao = ","
        photo = None
        cursor = self.conn.cursor()
        try:
            command = "Select DepartmentID from DepartmentInfo where Department =" + Department + ";"
            cursor.execute(command)
            DepartmentID = "'" + cursor.fetchone()[0] + "'"

        except:
            print("查询部门出错")
            print(command)
            return
        finally:
            cursor.close()
            del cursor

        cursor = self.conn.cursor()
        try:
            command = "Select PositionID from WageInfo where Position =" + Position + ";"
            cursor.execute(command)
            PositionID = "'" + cursor.fetchone()[0] + "'"

        except:
            print("查询职位出错")
            print(command)
            return
        finally:
            cursor.close()
            del cursor
        cursor = self.conn.cursor()
        try:
            command = "Select StaffID from StaffInfo where Name =" + Leader + ";"
            cursor.execute(command)
            LeaderID = "'" + cursor.fetchone()[0] + "'"
            cursor.close()
        except:
            print("查询领导出错")
            print(command)
            OK = QMessageBox.critical(self, ("反馈"), ("""您输入的领导名字有误，请重新确认"""),
                                      QMessageBox.StandardButton(QMessageBox.Yes))
            return
        finally:
            cursor.close()
            del cursor

        if self.File_Path != "":
            print(self.File_Path)
            file = open(self.File_Path, 'rb')
            photo = file.read()
            file.close()

            cursor = self.conn.cursor()
            try:
                command = "UPDATE `StaffInfo` SET Name="+Name+",WorkDay="+RZ+",Position="+Position+",PositionID="+PositionID+",Age="+Age+",Department="+Department+",DepartmentID="+DepartmentID+",Leader="+LeaderID+",Sex="+Sex+"where StaffID="+ID+";"
                print(command)
                cursor.execute(command)
                command = "UPDATE StaffInfo SET Photo=%s where StaffID=" + ID + ";"
                cursor.execute(command, (photo))
                self.conn.commit()

            except:
                print("有照片情况修改数据错误")
            finally:
                cursor.close()
        else:
            cursor = self.conn.cursor()
            try:
                command = "UPDATE `StaffInfo` SET Name=" + Name + ",WorkDay=" + RZ + ",Position=" + Position + ",PositionID=" + PositionID + ",Age=" + Age + ",Department=" + Department + ",DepartmentID=" + DepartmentID + ",Leader=" + LeaderID + ",Sex=" + Sex + "where StaffID=" + ID + ";"
                print(command)
                cursor.execute(command)
                cursor.execute(command)
                self.conn.commit()
            except:
                print("无照片情况修改数据错误")
            finally:
                cursor.close()

        self.close()
    def SC_Fun(self):
        cursor=self.conn.cursor()
        try:
            ID = "'" + self.GH_L.text() + "'"
            command = "Delete from StaffInfo WHERE StaffID ="+ID+";"
            print(command)
            cursor.execute(command)
            self.conn.commit()
            OK = QMessageBox.information(self, ("反馈"), ("""职员已被下岗"""),
                                  QMessageBox.StandardButton(QMessageBox.Yes))
            self.close()
        except:
            wrong = QMessageBox.critical(self, ("反馈"), ("""删除失败"""),
                                         QMessageBox.StandardButton(QMessageBox.Yes))
        finally:
            cursor.close()

    def signal_slot(self):
        self.Photo_B.clicked.connect(self.change_photo)
        self.Cancal.clicked.connect(self.Fanhui)
        self.Sure.clicked.connect(self.Queren)
        self.SC_B.clicked.connect(self.SC_Fun)






















#########################以下为添加员工模块#######################

class YGGL_Insert(Ui_YGGL_M,QDialog):
    def __init__(self,conn):
        super(YGGL_Insert, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.signal_slot()
        self.ComBox_init()
        self.Photo_B.setText('点击选择头像')
        self.File_Path=""

    def ComBox_init(self):
        self.BM_Box.addItem('管理层')
        self.BM_Box.addItem('人事部')
        self.BM_Box.addItem('财务部')
        self.BM_Box.addItem('产品部')
        self.XB_Box.addItem('男')
        self.XB_Box.addItem('女')
        self.ZW_Box.addItem('老板')
        self.ZW_Box.addItem('董事员')
        self.ZW_Box.addItem('经理')
        self.ZW_Box.addItem('主任')
        self.ZW_Box.addItem('科长')
        self.ZW_Box.addItem('科员')

    def change_photo(self):

        try:
            self.File_Path,filetype=QFileDialog.getOpenFileName(self,"选取文件","/Users/zhangyuhan/Desktop/水浒头像","All Files (*);;Iamge Files (*.jpg);;Iamge Files (*.png);;Iamge Files (*.png)")
            del filetype
        except:
            print("开启文件选择器失败")
        if self.File_Path!="":
            self.Photo_B.setText('')
            self.Photo_B.setIcon(QIcon(QtGui.QPixmap(self.File_Path)))
            self.Photo_B.setIconSize(QSize(161,161))


    def Fanhui(self):
        self.close()
    def Queren(self):
        ID="'"+self.GH_L.text()+"'"
        Name="'"+self.XM_L.text()+"'"
        Age=self.NL_Box.text()
        Sex="'"+self.XB_Box.currentText()+"'"
        Department="'"+self.BM_Box.currentText()+"'"
        DepartmentID=""
        Leader="'"+self.LD_L.text()+"'"
        LeaderID=''
        Position="'"+self.ZW_Box.currentText()+"'"
        PositionID=''
        RZ=self.RZ_L.text()
        print (RZ)
        RZ="str_to_date('"+RZ+"','%Y/%m/%d')"
        doubao=","
        photo=None
        cursor = self.conn.cursor()
        try:
            command = "Select DepartmentID from DepartmentInfo where Department =" + Department + ";"
            cursor.execute(command)
            DepartmentID = "'" + cursor.fetchone()[0] + "'"

        except:
            print("查询部门出错")
            print(command)
            return
        finally:
            cursor.close()
            del cursor

        cursor = self.conn.cursor()
        try:
            command = "Select PositionID from WageInfo where Position =" + Position + ";"
            cursor.execute(command)
            PositionID = "'" + cursor.fetchone()[0] + "'"

        except:
            print("查询职位出错")
            print(command)
            return
        finally:
            cursor.close()
            del cursor
        cursor = self.conn.cursor()
        try:
            command = "Select StaffID from StaffInfo where Name =" + Leader + ";"
            cursor.execute(command)
            LeaderID = "'" + cursor.fetchone()[0] + "'"
            cursor.close()
        except:
            print("查询领导出错")
            print(command)
            OK = QMessageBox.critical(self, ("反馈"), ("""您输入的领导名字有误，请重新确认"""), QMessageBox.StandardButton(QMessageBox.Yes))
            return
        finally:
            cursor.close()
            del cursor


        if self.File_Path!="":
            print (self.File_Path)
            file=open(self.File_Path,'rb')
            photo=file.read()
            file.close()



            try:
                cursor = self.conn.cursor()
                command = "INSERT INTO `StaffInfo` (StaffID,Name,WorkDay,Position,PositionID,Age,Department,DepartmentID,Leader,Sex) VALUES (" + ID + doubao + Name + doubao + RZ + doubao + Position + doubao + PositionID + doubao + Age + doubao + Department + doubao + DepartmentID + doubao + LeaderID + doubao + Sex + ");"
                cursor.execute(command)
                command = "UPDATE StaffInfo SET Photo=%s where StaffID=" + ID + ";"
                cursor.execute(command, (photo))
                self.conn.commit()

            except:
                print("有照片情况插入数据错误")
                somethingwrong = QMessageBox.critical(self, ("反馈"), ("""您输入的原始信息有误，请重新确认"""),
                                          QMessageBox.StandardButton(QMessageBox.Yes))
                return
            finally:
                cursor.close()
        else:
            try:
                cursor = self.conn.cursor()
                command="INSERT INTO `StaffInfo` (StaffID,Name,WorkDay,Position,PositionID,Age,Department,DepartmentID,Leader,Sex) VALUES ("+ID+doubao+Name+doubao+RZ+doubao+Position+doubao+PositionID+doubao+Age+doubao+Department+doubao+DepartmentID+doubao+LeaderID+doubao+Sex+");"
                print(command)
                cursor.execute(command)
                self.conn.commit()
                print(command)
            except:
                print("无照片情况插入数据错误")
                somethingwrong = QMessageBox.critical(self, ("反馈"), ("""您输入的原始信息有误，请重新确认"""),
                                                      QMessageBox.StandardButton(QMessageBox.Yes))
                return 
            finally:
                cursor.close()

        self.close()


    def signal_slot(self):
        self.Photo_B.clicked.connect(self.change_photo)
        self.Sure.clicked.connect(self.Queren)
        self.Cancal.clicked.connect(self.Fanhui)