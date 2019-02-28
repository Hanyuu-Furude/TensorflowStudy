import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QLabel, QPlainTextEdit, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication, QTimer
import t

class ui(QMainWindow):
    def __init__(self):
        super().__init__()

        # code to get and draw ui
        self.autoRead = True
        self.autoWrite = True
        # self=QMainWindow()
        loadUi('mainwindow.ui', self)
        self.checkBoxR = self.findChild(QCheckBox, 'checkBoxR')
        self.checkBoxR.stateChanged.connect(self.checkBoxChanged)
        self.checkBoxW = self.findChild(QCheckBox, 'checkBoxW')
        self.checkBoxW.stateChanged.connect(self.checkBoxChanged)
        self.textRead = self.findChild(QPlainTextEdit,'textOrigin')
        self.textWrite = self.findChild(QPlainTextEdit,'textTranslate')
        self.buttonExit = self.findChild(QPushButton,'buttonExit')
        # self.buttonExit.clicked.connect(QCoreApplication.exit)  # button on exit
        self.buttonExit.clicked.connect(self.text)  # button on exit
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.translate) #计时结束调用operate()方法
        # self.timer.start(1000) #设置计时间隔并启动
        self.show()

    # checkBox function
    def checkBoxChanged(self, state):
        if self.sender() == self.checkBoxR:
            self.autoRead = True if(state == 2) else False
        elif self.sender() == self.checkBoxW:
            self.autoWrite = True if (state == 2) else False
        # print('[auto read]', self.autoRead)
        # print('[suto write]', self.autoWrite)
        # print(self.textRead.toPlainText())
        # self.textWrite.clear()
        # self.textWrite.appendPlainText(self.textRead.toPlainText())
        # print(a.text())
        # a.text('a')
    # get the input box

    # fetch the text from textOrigin
    def fetchPlainText(self):
        return self.textRead.toPlainText()

    # set the text to textTranslate
    def setPlainText(self,text):
        self.textWrite.clear()
        self.textWrite.appendPlainText(text)
        return text

    
    def translate(self):
        # if self.autoRead:
        #     print(t.gettext())
        #     self.setPlainText(str(t.gettext()))
        temp = self.setPlainText(t.translate(self.fetchPlainText()))
        # if self.autoWrite:
        #     t.settext(temp)

    def readClipboard(self):
        return t.gettext()
    def writeClipboard(self,text):
        t.settext(text)
    def text(self):
        a = self.readClipboard()
        a=str(a)
        b = t.translate(a)
        self.writeClipboard(b)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = ui()
    sys.exit(app.exec_())
