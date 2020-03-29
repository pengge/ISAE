from PyQt5 import QtCore, QtWidgets, QtGui
from Crypto.MorseModule.ui_MorseModule import ui_MorsePanel
from Crypto.MorseModule.MorseModuleUtils import *


class MorsePanel(ui_MorsePanel):
    def __init__(self):
        super(MorsePanel, self).__init__()
        self.MorseEncodeButton.clicked.connect(self.MorseEncode)
        self.MorseDecodeButton.clicked.connect(self.MorseDecode)
        self.MorseCipherBox.textChanged.connect(self.setFontColorCipher)
        self.MorseTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.MorseCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.MorseTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def MorseEncode(self):
        spilt = self.MorseSpiltBox.text()
        if spilt == '':
            spilt = ' '
        elif spilt.find('.') != -1 or spilt.find('-') != -1:
            self.MorseCipherBox.setText('分隔符含有摩斯电码字符!')
            return
        try:
            self.MorseCipherBox.setText(MorseEncode(
                self.MorseTextBox.toPlainText(), spilt))
        except:
            self.MorseCipherBox.setText('编码出现错误!')

    def MorseDecode(self):
        spilt = self.MorseSpiltBox.text()
        if spilt == '':
            spilt = ' '
        elif spilt.find('.') != -1 or spilt.find('-') != -1:
            self.MorseTextBox.setText('分隔符含有摩斯电码字符!')
            return
        try:
            self.MorseTextBox.setText(MorseDecode(
                self.MorseCipherBox.toPlainText(), spilt))
        except:
            self.MorseTextBox.setText('解码出现错误!')
