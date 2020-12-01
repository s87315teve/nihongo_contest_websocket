# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""


from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

from Ui_nihongo_contest import Ui_Dialog
import readSupport
import os
import sys
import random
class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.fuck=0
        self.mistake=0
    
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        if self.fuck==1:
            input=self.lineEdit_input.text()
            if input==self.outTango[self.shitsumon].yomikata:
                self.point=self.point+1
                self.lcdNumber_point.display(self.point)
                self.textBrowser_answer.setText('おめでとう\n答えは：'+self.outTango[self.shitsumon].yomikata)
                del self.outTango[self.shitsumon]
            else:
                self.mistake=self.mistake+1
                self.lcdNumber_mistake.display(self.mistake)
                str='X!\n'+self.outTango[self.shitsumon].yomikata
                self.textBrowser_answer.setText(str)
                del self.outTango[self.shitsumon]
            
            self.lineEdit_input.clear()
            self.shitsumon=random.randint(0,len(self.outTango)-1)
            self.textBrowser_question.setText(self.outTango[self.shitsumon].kanji)
        else:
            self.fuck=1
            #讀檔
            file = open( 'ver2.txt', 'r',encoding='utf-16')
            tango=[]
            line = file.readline()
            while line:
                tango.append(readSupport.Tango(line.split()[0],line.split()[1]))
                line = file.readline()
            #關檔    
            file.close()
            self.outTango=[]
            self.outTango=tango
            self.point=0
            #印出題目
            self.shitsumon=random.randint(0,len(self.outTango)-1)
            self.textBrowser_question.setText(self.outTango[self.shitsumon].kanji)
    @pyqtSlot()
    def on_pushButton_input_clicked(self):
        input=self.lineEdit_input.text()
        if input==self.outTango[self.shitsumon].yomikata:
            self.point=self.point+1
            self.lcdNumber_point.display(self.point)
            self.textBrowser_answer.setText('おめでとう\n答えは：'+self.outTango[self.shitsumon].yomikata)
            del self.outTango[self.shitsumon]
        else:
            self.mistake=self.mistake+1
            self.lcdNumber_mistake.display(self.mistake)
            str='X!\n'+self.outTango[self.shitsumon].yomikata
            self.textBrowser_answer.setText(str)
            del self.outTango[self.shitsumon]
        self.lineEdit_input.clear()
        self.shitsumon=random.randint(0,len(self.outTango)-1)
        self.textBrowser_question.setText(self.outTango[self.shitsumon].kanji)
if __name__ == "__main__":
   if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
