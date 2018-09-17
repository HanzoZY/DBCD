from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog,  QPushButton, QMessageBox
from PyQt5 import QtGui,QtCore
from  JBGL import Ui_JBGL_M

class JBGL_All(Ui_JBGL_M,QDialog):
    def __init__(self,JB_Info,conn):
        super(JBGL_All, self).__init__()
        self.setupUi(self)
        self.SC_B =QPushButton(self)
        self.SC_B.setGeometry(QtCore.QRect(30, 300, 150, 50))
        self.SC_B.setText("删除记录")
        self.Info=JB_Info
        self.conn=conn
        self.Set_Info()
        self.signal_slot()
        self.GH_L.setEnabled(False)
        self.Photo_B.setEnabled(False)
        self.XM_L.setEnabled(False)
        self.RQ_E.setEnabled(False)

    def Set_Info(self):
        self.ID = self.Info[2]
        self.Name = self.Info[6]
        self.date=self.Info[3]
        self.LastTime=self.Info[4]

        self.GH_L.setText(self.ID)
        self.XM_L.setText(self.Name)
        self.RQ_E.setDate(QDate.fromString(self.date.strftime("%Y-%m-%d"), 'yyyy-MM-dd'))
        self.JB_Box.setValue(self.LastTime)
        cursor=self.conn.cursor()
        try:
            command = "select Photo from StaffInfo WHERE StaffID ='" + self.ID + "';"
            cursor.execute(command)
            self.photo = cursor.fetchone()[0]
            # print(self.photo)
            pix_map = QtGui.QPixmap()
            flag = pix_map.loadFromData(QtCore.QByteArray(self.photo))
            if flag:
                print('加班管理部分图片加载成功')
                self.Photo_B.setIcon(QIcon(pix_map))
                self.Photo_B.setIconSize(QSize(171, 171))
            else:
                print('图片加载失败')

        except:
            print('加班管理图片加载出错')
        finally:cursor.close()
        # command = "select Photo from StaffInfo WHERE StaffID ='" + self.ID + "';"
        # cursor.execute(command)
        # self.photo = cursor.fetchone()[0]
        # print (self.photo)
        # pix_map = QtGui.QPixmap()
        # flag = pix_map.loadFromData(QtCore.QByteArray(self.photo))
        # if flag:
        #     print('加班管理部分图片加载成功')
        #     self.Photo_B.setIcon(QIcon(pix_map))
        #     self.Photo_B.setIconSize(QSize(171, 171))
        # else:
        #     print('图片加载失败')




    def Fanhui(self):
        self.close()
    def Queren(self):
        cursor=self.conn.cursor()
        self.LastTime=self.JB_Box.value()
        command="UPDATE Attendence  SET LastTime="+str(self.LastTime)+" where StaffID='"+self.ID+"'and OccurDate=str_to_date('" + self.date.strftime("%Y-%m-%d")+ "','%Y-%m-%d') and Behavior='加班';"
        try:
            print(command)
            cursor.execute(command)
            self.conn.commit()
        except:
            print('加班信息修改出错')
        finally:cursor.close()
        self.close()
    def SC_Fun(self):
        cursor=self.conn.cursor()
        command="Delete from Attendence WHERE StaffID ='"+self.ID+"'and OccurDate=str_to_date('" + self.date.strftime("%Y-%m-%d")+ "','%Y-%m-%d') and Behavior='加班';"
        try:
            print(command)
            cursor.execute(command)
            self.conn.commit()
        except:
            print('加班信息修改出错')
        finally:cursor.close()
        print('删除')
        self.close()
    def signal_slot(self):
        self.Cancal.clicked.connect(self.Fanhui)
        self.Sure.clicked.connect(self.Queren)
        self.SC_B.clicked.connect(self.SC_Fun)


class JBGL_Insert(Ui_JBGL_M,QDialog):
    def __init__(self,User_Info,conn):
        super(JBGL_Insert, self).__init__()
        self.setupUi(self)
        self.UserInfo=User_Info
        self.conn=conn
        self.signal_slot()
        FilePath="匿名.png"
        self.Photo_B.setIcon(QIcon(QtGui.QPixmap(FilePath)))
        self.Photo_B.setIconSize(QSize(161, 161))



    def Fanhui(self):
        self.close()
    def Queren(self):

        cursor=self.conn.cursor()
        self.LastTime=self.JB_Box.value()
        LastTimeC=str(self.LastTime)
        self.Name=self.XM_L.text()
        self.GH=self.GH_L.text()
        GHC="'"+self.GH+"'"
        self.LastTime=self.JB_Box.value()
        self.date=self.RQ_E.text()
        dateC="str_to_date('"+self.date+"','%Y/%m/%d')"
        doubao = ","
        command="Insert into Attendence (StaffID,OccurDate,Behavior,LastTime) VALUES ("+GHC+doubao+dateC+doubao+"'加班'"+doubao+LastTimeC+");"
        if self.check_name_and_ID()==False:
            return
        if self.check_reInsert()==False:
            return
        try:
            print(command)
            cursor.execute(command)
            self.conn.commit()
        except:
            print('加班信息添加出错')
        finally:cursor.close()
        self.close()
    def check_name_and_ID(self):
        self.Name = self.XM_L.text()
        self.GH = self.GH_L.text()
        command="Select * from StaffInfo WHERE StaffID='"+self.GH+"' and Name='"+self.Name+"' and Leader='"+self.UserInfo+"';"
        print(command)
        cursor=self.conn.cursor()
        try:
            cursor.execute(command)
            data=cursor.fetchall()
            if len(data)==0:
                NameWrong = QMessageBox.critical(self, ("反馈"), ("""您输入的员工及工号有错误，或者您无权为该员工添加加班记录，请重新确认"""), QMessageBox.StandardButton(QMessageBox.Yes))
                return False
            else:
                return True
        except:
            print('加班记录添加名字检查错误')
            return False

    def check_reInsert(self):
        self.Name = self.XM_L.text()
        self.GH = self.GH_L.text()
        self.date = self.RQ_E.text()
        command="select * from Attendence where StaffID='"+self.GH+"' and OccurDate=str_to_date('"+self.date+"','%Y/%m/%d') and Behavior='加班';"
        print(command)
        cursor = self.conn.cursor()
        try:
            cursor.execute(command)
            data = cursor.fetchall()
            if len(data) != 0:
                DateWrong = QMessageBox.critical(self, ("反馈"), ("""您输入的加班信息与数据库中的信息有冲突，请重新确认"""),
                                                 QMessageBox.StandardButton(QMessageBox.Yes))
                return False
            else:
                return True
        except:
            print('加班记录添加时间检查错误')
            return False


    def signal_slot(self):
        self.Cancal.clicked.connect(self.Fanhui)
        self.Sure.clicked.connect(self.Queren)


