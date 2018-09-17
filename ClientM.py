import sys

from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QIcon
from datetime import *
from login import *
from MainWinC import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QDialog, QMessageBox
from PyQt5 import QtGui,QtCore
import numpy as np
import pymysql
import sys
import openpyxl
from JBGZBM_ALL import JBGZ_BM_ALL
from JBGZZW_ALL import JBGZ_ZW_ALL


from YGGL_All import YGGL_All,YGGL_Insert
from JBGL_ALL import JBGL_All,JBGL_Insert
class ClientL(QWidget,Ui_LoginWin):
    def __init__(self,conn):
        super(ClientL, self).__init__()
        #Ui_LoginWin.__init__(self)
        self.conn=conn
        # cursor = self.conn.cursor()
        # cursor.execute('select VERSION()')
        # data = cursor.fetchone()
        # print(data)
        # cursor.close()
        self.setupUi(self)
    def login(self):

        self.usr=self.UserName.text()
        self.pw=self.Passwd.text()
        print(self.usr, self.pw)
        cursor = self.conn.cursor()
###################
        try:
            command = "select PassWD from UandP where StaffID ='" + self.usr + "'"
            print(command)
            cursor.execute(command)
            data = cursor.fetchone()[0]


            if data == self.pw:
                print('密码正确')
                self.hide()
                self.newWin = ClientM(self.usr, self.conn)
                self.newWin.show()
            else:
                OK = QMessageBox.critical(self, ("反馈"), ("""密码或账号有误，请重新确认"""), QMessageBox.StandardButton(QMessageBox.Yes ))
                print('密码错误')
        except:
            OK = QMessageBox.critical(self, ("反馈"), ("""密码或账号有误，请重新确认"""), QMessageBox.StandardButton(QMessageBox.Yes))
            print('密码错误')
        finally:
            cursor.close()
#######################

        # try:
        #
        #     command="select PassWD from UandP where StaffID ='"+self.usr+"'"
        #     print (command)
        #     cursor=self.conn.cursor()
        #     print('lalala')
        #     cursor.execute(command)
        #     print('hahaha')
        #     data =cursor.fetchone()[0]
        #     cursor.close()
        #     print(data)
        #
        #     if data==self.pw:
        #         print ('密码正确')
        #         self.hide()
        #         self.newWin = ClientM(self.usr,self.conn)
        #         self.newWin.show()
        #     else:
        #         print('密码错误')
        # except:
        #     print("登录失败")






class ClientM(QMainWindow,Ui_MainWindowC):
    def __init__(self,usr,conn):
        super(ClientM, self).__init__()
        self.conn=conn
        self.usr = usr
        print('进入用户主界面')
        # cursor = self.conn.cursor()
        # cursor.execute('select VERSION()')
        # data = cursor.fetchone()
        # print(data)
        # cursor.close()
        self.setupUi(self)

        self.name1.setText(self.usr)

        self.tabWidget.setCurrentWidget(self.tab0)
        self.set_init_Info()
        self.YGGL_Info=[]
        self.KQGL_Info=[]
        self.JBGL_Info=[]
        self.YGGZ_Info=[]
        self.JBGZ_Info=[]
        self.YGGL_init()
        self.KQGL_init()
        self.JBGL_init()
        self.YGGZ_init()
        self.JBGZ_init()
        self.set_slot_and_signal()
#############################员工管理#############################
    def YGGL_init(self):
        self.BM_BOX.addItem('不限')
        self.BM_BOX.addItem('管理层')
        self.BM_BOX.addItem('人事部')
        self.BM_BOX.addItem('财务部')
        self.BM_BOX.addItem('产品部')
        self.SEX_BOX.addItem('不限')
        self.SEX_BOX.addItem('男')
        self.SEX_BOX.addItem('女')


    def YGGLsearch_Fun(self):
        all_command=[]
        departmt=self.BM_BOX.currentText()
        if departmt!='不限':
            dpmt_Command="Department = '"+departmt+"' "
            all_command.append(dpmt_Command)
            all_command.append("and ")

        sex=self.SEX_BOX.currentText()
        if sex!='不限':
            sex_command="Sex = '"+sex+"'"
            all_command.append(sex_command)
            all_command.append("and ")
        GL_Flag=self.GL_CK.checkState()
        # print(GL_Flag,'GL_Flag')
        if GL_Flag==2:
            GL_Low=self.GLspinBox1.value()
            GL_High=self.GLspinBox2.value()
            GL_command="year(`WorkDay`)<=year(date_sub(now(),interval "+str(GL_Low)+" year)) and year(`WorkDay`)>=year(date_sub(now(),interval "+str(GL_High)+" year)) "
            all_command.append(GL_command)
            all_command.append("and ")

        XM_Flag=self.XM_CK.checkState()
        if XM_Flag==2:
            Name=self.XM_Line1.text()
            Name_Command="Name = '"+Name+"' "
            all_command.append(Name_Command)
            all_command.append("and ")

        GH_Flag=self.GH_CK.checkState()
        if GH_Flag==2:
            GH=self.GH_Line1.text()
            GH_Command="StaffID ='"+GH+"' "
            all_command.append(GH_Command)
            all_command.append("and ")





        # total_command ="select * from StaffInfo"
        # if len(all_command)>0:
        #     all_command.pop()
        #     total_command += " where "
        #     for i in all_command:
        #         total_command+=i
        # total_command+=";"

        total_command = "select * from StaffInfo"
        if self.DepartMTID=="003":

            if len(all_command) > 0:
                all_command.pop()
                total_command += " where "
                for i in all_command:
                    total_command += i
            total_command += ";"
        else:
            total_command += " where "
            if len(all_command) > 0:
                all_command.pop()
                for i in all_command:
                    total_command += i
                total_command+=' and '
            total_command += "(StaffID='"+self.ID+"' or Leader='"+self.ID+"');"






        print(total_command)
        cursor = self.conn.cursor()
        try:
            self.YGGL_Info.clear()
            self.YGGLTable.clearContents()
            cursor.execute(total_command)
            data = cursor.fetchall()
            #print(data)
            StaffID=[]
            Name=[]
            WorkDay=[]
            Position=[]
            PositionID=[]
            Photo=[]
            Age=[]
            Department=[]
            DepartmentID=[]
            Leader=[]
            Sex=[]
            for row in data:
                StaffID.append(row[0])
                Name.append(row[1])
                WorkDay.append(row[2])
                Position.append(row[3])
                PositionID.append(row[4])
                Photo.append(row[5])
                Age.append(row[6])
                Department.append(row[7])
                DepartmentID.append(row[8])
                Leader.append(row[9])
                Sex.append(row[10])
                self.YGGL_Info.append(row)
            count=len(StaffID)
            print(count)
            print(np.shape(self.YGGL_Info))
            if self.DepartMTID=='003':
                self.YGGLTable.setRowCount((count+1))
            else:self.YGGLTable.setRowCount((count))
            for i in range(count):
                # print(StaffID[i],Name[i],Department[i],Position[i])
                self.YGGLTable.setItem(i, 0, QTableWidgetItem(str(StaffID[i])))
                self.YGGLTable.setItem(i, 1, QTableWidgetItem(str(Name[i])))
                self.YGGLTable.setItem(i,2,QTableWidgetItem(str(Department[i])))
                self.YGGLTable.setItem(i, 3, QTableWidgetItem(str(Position[i])))
                # self.YGGLTable.setItem(i,4,QTableWidgetItem('更多'))

            if self.DepartMTID=='003':
                tempItem=QTableWidgetItem('增加')
                tempItem.setTextAlignment(0x0004|0x0080)
                self.YGGLTable.setItem(count, 0, tempItem)
                # self.YGGLTable.setSpan(count, 0, 1, 5)
        except:
            print('员工信息查询失败')
        finally:
            cursor.close()
            self.YGGLTable.show()


    def YGGL_M(self):
        self.setEnabled(False)
        # print(self.YGGLTable.currentRow())
        # print(self.YGGLTable.currentItem())
        index=self.YGGLTable.currentRow()
        right=0
        if self.DepartMTID=='003':
            right=1
        if index>=len(self.YGGL_Info):
            ygInsert=YGGL_Insert(self.conn)
            ygInsert.exec_()
            self.setEnabled(True)
        else:
            yggl = YGGL_All(self.YGGL_Info[index], self.conn,right)
            yggl.exec_()
            self.setEnabled(True)



    #########################考勤管理###################################################
    def KQGL_init(self):
        self.BM_BOX_2.addItem('不限')
        self.BM_BOX_2.addItem('管理层')
        self.BM_BOX_2.addItem('人事部')
        self.BM_BOX_2.addItem('财务部')
        self.BM_BOX_2.addItem('产品部')
        self.JL_BOX.addItem('不限')
        self.JL_BOX.addItem('迟到')
        self.JL_BOX.addItem('早退')


    def KQSearch_Fun(self):
        all_command=[]
        departmt = self.BM_BOX_2.currentText()
        if departmt!='不限':
            dpmt_Command="Department = '"+departmt+"' "
            all_command.append(dpmt_Command)
            all_command.append("and ")
        behavior=self.JL_BOX.currentText()
        if behavior!='不限':
            Behavior_command="Behavior ='"+behavior+"'"
            all_command.append(Behavior_command)
            all_command.append("and ")
        else:
            Behavior_command = "(Behavior ='迟到'or Behavior='早退')"
            all_command.append(Behavior_command)
            all_command.append("and ")


        XM_Flag = self.XM_CK_2.checkState()
        if XM_Flag == 2:
            Name = self.lineEdit_3.text()
            Name_Command = "Name ='" + Name + "'"
            all_command.append(Name_Command)
            all_command.append("and ")

        GH_Flag = self.GH_CK_2.checkState()
        if GH_Flag == 2:
            GH = self.lineEdit_4.text()
            GH_Command = "StaffID ='" + GH + "' "
            all_command.append(GH_Command)
            all_command.append("and ")


        Date_S=self.dateEdit_2.text()
        Date_E=self.dateEdit_3.text()
        Date_Command="OccurDate >=str_to_date('" + Date_S + "','%Y/%m/%d') and OccurDate <=str_to_date('" + Date_E + "','%Y/%m/%d')"
        all_command.append(Date_Command)
        # all_command.append("and ")
        # print (Date_S,Date_E)


        #
        # if len(all_command) > 0:
        #     all_command.pop()
        #     total_command += " where "
        #     for i in all_command:
        #         total_command += i
        # total_command += ";"

        total_command = "select * from KQ_VIEW "
        if self.DepartMTID=='001':

            if len(all_command) > 0:
                # all_command.pop()
                total_command += " where "
                for i in all_command:
                    total_command += i
            total_command += ";"
        else:
            if len(all_command) > 0:
                # all_command.pop()
                total_command += " where "
                for i in all_command:
                    total_command += i
                total_command+=' and '
            total_command += "(StaffID='"+self.ID+"' or Leader='"+self.ID+"');"





        print(total_command)
        cursor=self.conn.cursor()
        try:
            self.KQGL_Info.clear()
            self.KQ_Table.clearContents()
            cursor.execute(total_command)
            data = cursor.fetchall()
            Name=[]
            Behavior=[]
            StaffID=[]
            Date=[]
            Department=[]
            for row in data:
                Name.append(row[6])
                Behavior.append(row[5])
                StaffID.append(row[1])
                Date.append(row[3])
                Department.append(row[0])
                self.KQGL_Info.append(row)
            count = len(StaffID)
            print(count)
            self.KQ_Table.setRowCount((count))
            for i in range(count):
                    # print(StaffID[i],Name[i],Department[i],Position[i])
                self.KQ_Table.setItem(i, 0, QTableWidgetItem(str(Name[i])))
                self.KQ_Table.setItem(i, 1, QTableWidgetItem(str(Behavior[i])))
                self.KQ_Table.setItem(i,2,QTableWidgetItem(str(StaffID[i])))
                self.KQ_Table.setItem(i, 3, QTableWidgetItem(str(Date[i].strftime("%Y-%m-%d"))))
                self.KQ_Table.setItem(i,4,QTableWidgetItem(str(Department[i])))



        except:
            print("考勤查询失败")
        finally:
            cursor.close()
            self.KQ_Table.show()



##############################加班管理   恢复try#############################
    def JBGL_init(self):
        self.BM_BOX_4.addItem('不限')
        self.BM_BOX_4.addItem('管理层')
        self.BM_BOX_4.addItem('人事部')
        self.BM_BOX_4.addItem('财务部')
        self.BM_BOX_4.addItem('产品部')

    def JBSearch_Fun(self):
        all_command = []
        departmt = self.BM_BOX_4.currentText()
        if departmt != '不限':
            dpmt_Command = "Department = '" + departmt + "' "
            all_command.append(dpmt_Command)
            all_command.append("and ")

        XM_Flag = self.GL_CK_7.checkState()
        if XM_Flag == 2:
            Name = self.lineEdit_5.text()
            Name_Command = "Name ='" + Name + "'"
            all_command.append(Name_Command)
            all_command.append("and ")

        GH_Flag = self.GL_CK_8.checkState()
        if GH_Flag == 2:
            GH = self.lineEdit_6.text()
            GH_Command = "StaffID ='" + GH + "' "
            all_command.append(GH_Command)
            all_command.append("and ")

        Date_S = self.dateEdit_5.text()
        Date_E = self.dateEdit_4.text()
        Date_Command = "OccurDate >=str_to_date('" + Date_S + "','%Y/%m/%d') and OccurDate <=str_to_date('" + Date_E + "','%Y/%m/%d')"
        all_command.append(Date_Command)
        total_command = "select * from KQ_VIEW "
        if self.DepartMTID=='001':

            if len(all_command) > 0:
                total_command += " where "
                for i in all_command:
                    total_command += i
                total_command += ' and '
            total_command += " Behavior ='加班';"
        else:
            if len(all_command) > 0:
                total_command += " where "
                for i in all_command:
                    total_command += i
                total_command+=' and '
            total_command += "Behavior ='加班' and (StaffID='"+self.ID+"' or Leader='"+self.ID+"');"

        cursor = self.conn.cursor()
        try:
            self.JBGL_Info.clear()
            self.JB_Table.clearContents()
            cursor.execute(total_command)
            data = cursor.fetchall()
            # print(data)
            Name = []
            StaffID = []
            Date = []
            Department = []
            LastTime=[]
            for row in data:
                Name.append(row[6])
                StaffID.append(row[2])
                Date.append(row[3])
                Department.append(row[0])
                LastTime.append(row[4])
                self.JBGL_Info.append(row)
            count = len(StaffID)
            print('加班数据数量',count)
            self.JB_Table.setRowCount((count+1))
            for i in range(count):
                # print(StaffID[i],Name[i],Department[i],Position[i])
                self.JB_Table.setItem(i, 0, QTableWidgetItem(str(StaffID[i])))
                self.JB_Table.setItem(i, 1, QTableWidgetItem(str(Name[i])))
                self.JB_Table.setItem(i, 2, QTableWidgetItem(str(Department[i])))
                self.JB_Table.setItem(i, 3, QTableWidgetItem(str(Date[i].strftime("%Y-%m-%d"))))
                self.JB_Table.setItem(i, 4, QTableWidgetItem(str(LastTime[i])))
            tempItem = QTableWidgetItem('增加')
            tempItem.setTextAlignment(0x0004 | 0x0080)
            self.JB_Table.setItem(count, 0, tempItem)

        except:
            print("考勤查询失败")
        finally:
            cursor.close()
            self.JB_Table.show()




        print(total_command)
    def JBGL_M(self):
        self.setEnabled(False)
        index=self.JB_Table.currentRow()
        if index>=len(self.JBGL_Info):
            print('加班增加')
            jbgl_Insert=JBGL_Insert(User_Info=self.ID,conn=self.conn)
            jbgl_Insert.exec_()
            self.setEnabled(True)
        else:
            print('加班修改',self.JBGL_Info[index])
            jbgl_M=JBGL_All(JB_Info=self.JBGL_Info[index],conn=self.conn)
            jbgl_M.exec_()
            self.setEnabled(True)



###################################员工工资#################################
    def YGGZ_init(self):

        self.BM_BOX_5.addItem('不限')
        self.BM_BOX_5.addItem('管理层')
        self.BM_BOX_5.addItem('人事部')
        self.BM_BOX_5.addItem('财务部')
        self.BM_BOX_5.addItem('产品部')


    def YGGZ_Search(self):
        self.YGGZ_Info.clear()
        self.YGGZ_Table.clearContents()
        all_command = []
        departmt = self.BM_BOX_5.currentText()
        if departmt != '不限':
            dpmt_Command = "b.Department = '" + departmt + "' and "
            all_command.append(dpmt_Command)

        XM_Flag = self.XM_CK_9.checkState()
        if XM_Flag == 2:
            Name = self.lineEdit_7.text()
            Name_Command = "b.Name = '" + Name + "' and "
            all_command.append(Name_Command)

        GH_Flag = self.GH_CK_10.checkState()
        if GH_Flag == 2:
            GH = self.lineEdit_8.text()
            GH_Command = "b.StaffID ='" + GH + "' and "
            all_command.append(GH_Command)

        Month=self.MonthEdit.text()
        MonthC="DATE_FORMAT(a.OccurDate , '%Y%m')=DATE_FORMAT(str_to_date('"+Month+"/1','%Y/%m/%d') , '%Y%m')"
        #all_command.append(MonthC)
        total_command = "select sum(a.LastTime),b.StaffID,b.Name,b.PositionID,b.Department,Behavior from KQ_VIEW a join StaffInfo b on a.StaffID=b.StaffID  "
        """select sum(a.LastTime),b.StaffID,b.Name,b.PositionID,b.Department,Behavior from KQ_VIEW a join StaffInfo b on a.StaffID=b.StaffID where DATE_FORMAT(a.OccurDate , '%Y%m')=DATE_FORMAT(str_to_date('2018/2/1','%Y/%m/%d') , '%Y%m') group by a.StaffID,`Behavior` ;"""
        total_command_1="select * from StaffInfo "
        if self.DepartMTID=='004':
            total_command += " where "

            if len(all_command) > 0:
                total_command_1 += " where "
                for i in all_command:
                    total_command += i
                    total_command_1 +=i[2:]
                total_command_1 = total_command_1[:-4]
            total_command+=MonthC
            total_command += " group by a.StaffID,`Behavior` ;"

        else:
            total_command += " where "
            total_command_1 += "where"
            if len(all_command) > 0:

                for i in all_command:
                    total_command += i
                    total_command_1 += i[2:]
                total_command_1 = total_command_1[:-4]
            total_command+=MonthC
            total_command += " and b.StaffID='"+self.ID+"' group by a.StaffID,`Behavior` ;"
            total_command_1+=" StaffID='"+self.ID+"';"
        print(total_command)
        print(total_command_1)
        cursor=self.conn.cursor()
        All_Info = {}
        try:

            cursor.execute(total_command)
            data = cursor.fetchall()
            for row in data:
                self.YGGZ_Info.append(row)
            ####使用一个字典存储所有信息，key是职员的ID，value是该ID对应职员的信息####
            #####结构 ID Name PositionID DepartMent 加班时间 迟到时间 早退时间
            All_Info={}
            for row in self.YGGZ_Info:
                if row[1] not in All_Info:
                    All_Info[row[1]]=['','','','',0,0,0]
                    All_Info[row[1]][0]=row[1]
                    All_Info[row[1]][1]=row[2]
                    All_Info[row[1]][2]=row[3]
                    All_Info[row[1]][3]=row[4]

                if row[-1]=='加班':
                    All_Info[row[1]][4] = row[0]
                if row[-1]=='迟到':
                    All_Info[row[1]][5] = row[0]
                if row[-1]=='早退':
                    All_Info[row[1]][6] = row[0]
            #print(All_Info)


        except:
            print ('员工工资查询first出错')
        finally:
            cursor.close()
            self.YGGZ_Info.clear()

        #补全所有人的工资信息
        cursor=self.conn.cursor()
        try:
            print(total_command_1)
            cursor.execute(total_command_1)
            data = cursor.fetchall()
            self.YGGZ_Info.clear()
            for row in data:
                self.YGGZ_Info.append(row)
            for row in self.YGGZ_Info:
                if row[0] not in All_Info:
                    All_Info[row[0]] = ['', '', '', '', 0, 0, 0]
                    All_Info[row[0]][0] = row[0]
                    All_Info[row[0]][1] = row[1]
                    All_Info[row[0]][2] = row[4]
                    All_Info[row[0]][3] = row[7]
        except:
            print('员工工资查询second出错')
        finally:
            cursor.close()
            self.YGGZ_Info.clear()

##########################################################


        for staff in All_Info:
            staffI=All_Info[staff]
            cursor=self.conn.cursor()
            TempCommand="select BaseWage,OvertimePay,LEarly,Late from WageInfo WHERE PositionID='"+staffI[2]+"';"
            ######staffInfo结构 ID name department 基本工资 津贴 扣罚 总工资
            try:
                cursor.execute(TempCommand)
                TempData=cursor.fetchone()
                staffInfo=[staffI[0],staffI[1],staffI[3],TempData[0],int(TempData[1]*(staffI[4])),int(-TempData[3]*staffI[5]-TempData[2]*(staffI[6])),0]
                self.YGGZ_Info.append(staffInfo)
            except:
                print('计算工资出错')
            finally:
                cursor.close()
        # print(self.YGGZ_Info)
        for i in self.YGGZ_Info:
            cursor = self.conn.cursor()
            TempCommand = "select Allowance from DepartmentInfo WHERE Department='" + i[2] + "';"
            print(TempCommand)
            try:
                cursor.execute(TempCommand)
                TempData = cursor.fetchone()[0]
                i[4]+=int(TempData)
                i[6]=i[3]+i[4]+i[5]
            except:
                print('工资计算出错222')
            finally:
                cursor.close()

        print(self.YGGZ_Info)
        #显示出工资表

        self.YGGZ_Table.setRowCount((len(self.YGGZ_Info)))
        for i in range(len(self.YGGZ_Info)):
            # print(StaffID[i],Name[i],Department[i],Position[i])
            self.YGGZ_Table.setItem(i, 0, QTableWidgetItem(str(self.YGGZ_Info[i][0])))
            self.YGGZ_Table.setItem(i, 1, QTableWidgetItem(str(self.YGGZ_Info[i][1])))
            self.YGGZ_Table.setItem(i, 2, QTableWidgetItem(str(self.YGGZ_Info[i][2])))
            self.YGGZ_Table.setItem(i, 3, QTableWidgetItem(str(self.YGGZ_Info[i][3])))
            self.YGGZ_Table.setItem(i, 4, QTableWidgetItem(str(self.YGGZ_Info[i][4])))
            self.YGGZ_Table.setItem(i, 5, QTableWidgetItem(str(self.YGGZ_Info[i][5])))
            self.YGGZ_Table.setItem(i, 6, QTableWidgetItem(str(self.YGGZ_Info[i][6])))
        self.YGGZ_Table.show()



    def export(self):
        tempInfo=self.YGGZ_Info.copy()
        title=['工号','姓名','部门','基本工资','津贴','扣罚','总工资']
        tempInfo.append(title)
        tempInfo[0],tempInfo[-1]=tempInfo[-1],tempInfo[0]
        try:
            wrt2xl(tempInfo,self.Name)
            OK=QMessageBox.information(self, ("反馈"), ("""导出完成"""),
                                  QMessageBox.StandardButton(QMessageBox.Yes))
        except:
            wrong = QMessageBox.critical(self, ("反馈"), ("""导出失败"""),
                                  QMessageBox.StandardButton(QMessageBox.Yes))







            ################################加班管理######################################
    def JBGZ_init(self):

        self.BM_BOX_6.addItem('不限')
        self.BM_BOX_6.addItem('管理层')
        self.BM_BOX_6.addItem('人事部')
        self.BM_BOX_6.addItem('财务部')
        self.BM_BOX_6.addItem('产品部')
        self.ZW_BOX.addItem('不限')
        self.ZW_BOX.addItem('老板')
        self.ZW_BOX.addItem('董事员')
        self.ZW_BOX.addItem('经理')
        self.ZW_BOX.addItem('主任')
        self.ZW_BOX.addItem('科长')
        self.ZW_BOX.addItem('科员')
        if self.DepartMTID!='004':
            self.JBGZsarch_B.setEnabled(False)
            self.BM_BOX_6.setEnabled(False)
            self.ZW_BOX.setEnabled(False)


    def JBGZ_Search(self):
        #用户选择了部门
        if self.radioButton.isChecked():
            self.JBGZflag=0
            self.JBGZ_Info.clear()
            self.JBGZ_Table.clearContents()
            #根据选择调整界面
            self.JBGZ_Table.setColumnCount(2)
            item0 = QtWidgets.QTableWidgetItem()
            item0.setText("部门")
            self.JBGZ_Table.setHorizontalHeaderItem(0, item0)
            item1 = QtWidgets.QTableWidgetItem()
            item1.setText('部门津贴')
            self.JBGZ_Table.setHorizontalHeaderItem(1, item1)
            self.JBGZ_Table.horizontalHeader().setDefaultSectionSize(310)

            total_command = "select * from DepartmentInfo "
            departmt = self.BM_BOX_6.currentText()
            if departmt != '不限':
                dpmt_Command = " where Department = '" + departmt + "';"
                total_command+=dpmt_Command
            else:
                total_command+=";"
            cursor=self.conn.cursor()
            try:
                cursor.execute(total_command)
                data=cursor.fetchall()
                Department=[]
                Allowance=[]
                for row in data:
                    Department.append(row[0])
                    Allowance.append(row[2])
                    self.JBGZ_Info.append(row)
                count = len(Department)
                print(count)
                self.JBGZ_Table.setRowCount((count))
                for i in range(count):
                    # print(StaffID[i],Name[i],Department[i],Position[i])
                    self.JBGZ_Table.setItem(i, 0, QTableWidgetItem(str(Department[i])))
                    self.JBGZ_Table.setItem(i, 1, QTableWidgetItem(str(Allowance[i])))
            except:
                print("基本部门工资查询失败")

            finally:
                cursor.close()
                self.JBGZ_Table.show()






        elif self.radioButton_2.isChecked():
            #根据选择调整界面
            self.JBGZflag=1
            self.JBGZ_Info.clear()
            self.JBGZ_Table.clearContents()
            self.JBGZ_Table.setColumnCount(5)
            item0 = QtWidgets.QTableWidgetItem()
            item0.setText("职位")
            self.JBGZ_Table.setHorizontalHeaderItem(0, item0)
            item1 = QtWidgets.QTableWidgetItem()
            item1.setText('基本工资')
            self.JBGZ_Table.setHorizontalHeaderItem(1, item1)
            item2 = QtWidgets.QTableWidgetItem()
            item2.setText('加班工资/小时')
            self.JBGZ_Table.setHorizontalHeaderItem(2, item2)
            item3 = QtWidgets.QTableWidgetItem()
            item3.setText('迟到扣罚/小时')
            self.JBGZ_Table.setHorizontalHeaderItem(3, item3)
            item4 = QtWidgets.QTableWidgetItem()
            item4.setText('早退扣罚/小时')
            self.JBGZ_Table.setHorizontalHeaderItem(4, item4)
            self.JBGZ_Table.horizontalHeader().setDefaultSectionSize(125)

            total_command = "select * from WageInfo "
            Position = self.ZW_BOX.currentText()
            if Position != '不限':
                ps_Command = " where Department = '" + Position + "';"
                total_command += ps_Command
            else:
                total_command += ";"
            cursor = self.conn.cursor()
            try:
                cursor.execute(total_command)
                data = cursor.fetchall()
                Position = []
                BaseWage = []
                OvertimePay=[]
                LEarly=[]
                Late=[]
                for row in data:
                    Position.append(row[1])
                    BaseWage.append(row[2])
                    OvertimePay.append(row[3])
                    LEarly.append(row[4])
                    Late.append(row[5])
                    self.JBGZ_Info.append(row)
                count = len(Position)
                print(count)
                self.JBGZ_Table.setRowCount((count))
                for i in range(count):
                    # print(StaffID[i],Name[i],Department[i],Position[i])
                    self.JBGZ_Table.setItem(i, 0, QTableWidgetItem(str(Position[i])))
                    self.JBGZ_Table.setItem(i, 1, QTableWidgetItem(str(BaseWage[i])))
                    self.JBGZ_Table.setItem(i, 2, QTableWidgetItem(str(OvertimePay[i])))
                    self.JBGZ_Table.setItem(i, 3, QTableWidgetItem(str(LEarly[i])))
                    self.JBGZ_Table.setItem(i, 4, QTableWidgetItem(str(Late[i])))
            except:
                print("基本工资职位查询失败")

            finally:
                cursor.close()
                self.JBGZ_Table.show()

        else:
            print('none')

    def JBGZ_M(self):
        self.setEnabled(False)
        index = self.JBGZ_Table.currentRow()
        Info=self.JBGZ_Info[index]
        if self.JBGZflag==0:
            print('部门基本工资修改')
            jbgzbm = JBGZ_BM_ALL(Info=Info, conn=self.conn)
            jbgzbm.exec_()
            self.setEnabled(True)
        elif self.JBGZflag==1:
            jbgzzw=JBGZ_ZW_ALL(Info=Info,conn=self.conn)
            jbgzzw.exec_()
            print('职位基本工资修改')
            self.setEnabled(True)
        else:print('修改基本工资表error')

################################基本工资#######################################
    def set_init_Info(self):
        cursor = self.conn.cursor()
        command = "select StaffID,Name,Photo from StaffInfo WHERE StaffID='" + self.usr + "';"
        try:
            cursor.execute(command)
            data = cursor.fetchone()
            photo_data = data[2]
            Name=data[1]
            ID=data[0]
            # print(data)
            pix_map = QtGui.QPixmap()
            flag = pix_map.loadFromData(QtCore.QByteArray(photo_data))
            self.name1.setText(Name)
            self.ID1.setText(ID)


            if flag:
                print('图片加载成功')
                self.GRM_B.setIcon(QIcon(pix_map))
                self.GRM_B.setIconSize(QSize(161, 161))


            else:
                print('图片加载失败')

        except:print('读取失败')
        finally:
            cursor.close()
        self.refresh_GRW()


    def refresh_GRW(self):
        cursor = self.conn.cursor()
        command = "select * from StaffInfo WHERE StaffID='" + self.usr + "';"
        try:
            cursor.execute(command)
            data = cursor.fetchone()
            # print(data)
            # print('-----------------------------------')
            self.ID = data[0]
            self.Name = data[1]
            self.InTime = data[2].strftime("%Y-%m-%d")
            # print(InTime)
            self.Position = data[3]
            self.PositionID = data[4]
            PhotoData = data[5]
            self.Age = data[6]
            self.DepartMT = data[7]
            self.DepartMTID = data[8]
            self.Leader = data[9]
            self.Sex = data[10]
            pix_map = QtGui.QPixmap()
            flag = pix_map.loadFromData(QtCore.QByteArray(PhotoData))
            if flag:
                self.label_2.setText(self.Name)
                self.label_4.setText(self.ID)
                self.label_6.setText(self.Sex)
                self.label_8.setText(str(self.Age))
                self.label_10.setText(self.DepartMT)
                self.label_12.setText(self.Position)
                self.label_14.setText(self.InTime)
                self.label_3.setText(self.Leader)
                self.Photo_L1.setPixmap(pix_map)
            else:
                print('refresh flag error')
        except:
            print('refresh failed')


        cursor.close()




    def set_slot_and_signal(self):
        #在点击之后加入刷新
        self.GRM_B.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab1))
        self.YGM_B.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab2))
        self.KQM_B.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab3))
        self.JBM_B.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab4))
        self.GZM_B.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab5))
        self.JBGZ_B.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab6))
        self.YGGLSearch_B.clicked.connect(self.YGGLsearch_Fun)
        self.GLspinBox1.valueChanged.connect (lambda: self.GLspinBox2.setMinimum(self.GLspinBox1.value()))
        self.GLspinBox2.valueChanged.connect(lambda: self.GLspinBox1.setMaximum(self.GLspinBox2.value()))
        self.YGGLTable.itemDoubleClicked.connect(self.YGGL_M)
        self.dateEdit_2.dateChanged.connect(lambda :self.dateEdit_3.setMinimumDate(QDate.fromString(self.dateEdit_2.text(),'yyyy/M/d')))

        self.dateEdit_3.dateChanged.connect(lambda: self.dateEdit_2.setMaximumDate(QDate.fromString(self.dateEdit_3.text(),'yyyy/M/d')))
        # self.dateEdit_2.dateChanged.connect(lambda: print(str(self.dateEdit_2.text())))
        # self.dateEdit_2.dateChanged.connect(lambda: print(QDate.fromString(self.dateEdit_2.text(), 'yyyy/M/d')))

        self.KQsearch_B.clicked.connect(self.KQSearch_Fun)
        self.JBsearch_B.clicked.connect(self.JBSearch_Fun)
        self.JB_Table.itemDoubleClicked.connect(self.JBGL_M)
        self.YGGZsearch_B.clicked.connect(self.YGGZ_Search)
        self.DC_B.clicked.connect(self.export)
        self.JBGZsarch_B.clicked.connect(self.JBGZ_Search)
        self.JBGZ_Table.itemDoubleClicked.connect(self.JBGZ_M)

def Main():

    app = QtWidgets.QApplication(sys.argv)
    conn=pymysql.Connect(host='localhost', port=3306, user='Server', passwd='Server', db='DBCD', charset='utf8')
    myWindow = ClientL(conn)
    myWindow.show()
    # conn.close()
    sys.exit(app.exec_())





def wrt2xl(listone,name):
    path='/Users/zhangyuhan/Desktop/reportXL/'+name+'.xlsx'
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = name
    for i in range(0, len(listone)):
        for j in range(0, len(listone[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(listone[i][j]))

    wb.save(path)
    print("写入EXCEL成功！")


if __name__ == '__main__':
    Main()


