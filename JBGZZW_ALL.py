from JBGZZW import Ui_JBGZ_ZW
from PyQt5.QtWidgets import QDialog
class JBGZ_ZW_ALL(Ui_JBGZ_ZW,QDialog):
    def __init__(self,conn,Info):
        super(JBGZ_ZW_ALL,self).__init__()
        self.setupUi(self)
        self.Info=Info
        self.conn=conn
        print(self.Info)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.Set_Info()
        self.signal_and_slot()

    def Set_Info(self):
        self.lineEdit.setText(self.Info[0])
        self.lineEdit_2.setText(self.Info[1])
        self.spinBox.setValue(int(self.Info[2]))
        self.spinBox_2.setValue(int(self.Info[3]))
        self.spinBox_3.setValue(int(self.Info[4]))
        self.spinBox_4.setValue(int(self.Info[4]))

    def OK(self):
        BaseWage=self.spinBox.value()
        OvertimePay=self.spinBox_2.value()
        LEarly=self.spinBox_3.value()
        Late=self.spinBox_4.value()
        cursor=self.conn.cursor()
        command="Update WageInfo set BaseWage ="+str(BaseWage)+",OvertimePay="+str(OvertimePay)+",LEarly="+str(LEarly)+",Late="+str(Late)+" where PositionID ='"+self.Info[0]+"';"
        print(command)
        try:
            cursor.execute(command)
            self.conn.commit()
        except:
            print('提交失败')
        finally:
            cursor.close()
            self.close()
    def signal_and_slot(self):
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.OK)