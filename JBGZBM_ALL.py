from JBGZBM import Ui_JBGZBM_M
from PyQt5.QtWidgets import QDialog
class JBGZ_BM_ALL(Ui_JBGZBM_M,QDialog):
    def __init__(self,conn,Info):
        super(JBGZ_BM_ALL,self).__init__()
        self.setupUi(self)
        self.Info=Info
        self.conn=conn
        print(self.Info)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.Set_Info()
        self.signal_and_slot()

    def Set_Info(self):
        self.lineEdit.setText(self.Info[1])
        self.lineEdit_2.setText(self.Info[0])
        self.spinBox.setValue(int(self.Info[2]))

    def OK(self):
        data=self.spinBox.value()
        cursor=self.conn.cursor()
        command="Update DepartmentInfo set Allowance ="+str(data)+" where DepartmentID ='"+self.Info[1]+"';"
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
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.OK)