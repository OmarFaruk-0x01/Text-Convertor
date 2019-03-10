from Text_Converter import Encode
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QVBoxLayout,QGroupBox,QTextEdit,QComboBox,QLabel,QDialog
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
x=Encode()
ui,_=loadUiType("UI/conv_gui.ui")
ui2,_=loadUiType("UI/devloper.ui")
class Devloper(QDialog,ui2):
    def __init__(self,parent):
        super(Devloper,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Devloper Details !!!")
        self.setWindowFlag(Qt.WindowContextHelpButtonHint , False)
class mainApp(QMainWindow,ui):
    def __init__(self):
        super(mainApp,self).__init__()
        self.setupUi(self)
        self.handle_Widgets()
        self.setWindowIcon(QIcon("UI/icon.png"))
        with open("style.css",'r') as f:
            self.setStyleSheet(f.read())
    def menu(self):
        self.actionDevloper.triggered.connect(lambda:self.dev.show())
    def handle_Widgets(self):
        self.textEdit_2.textChanged.connect(self.check_Text_Fields)
        self.dev=Devloper(self)
        self.menu()
    def check_Text_Fields(self):
        text=self.textEdit_2.toPlainText()
        com1=self.comboBox.currentText()
        com2=self.comboBox_2.currentText()
        return_=""
        if com1=="Text" and com2=="Binary":
            return_=x.TextToBinary(text)
        elif com1=="Text" and com2=="Decimal":
            return_=x.TextToDecimal(text)
        elif com1=="Text" and com2=="Hex":
            return_=x.TextToHex(text)
        elif com1=="Text" and com2=="Octal":
            return_=x.TextToOctal(text)
        elif com1=="Text" and com2=="Ceasar":
            return_=x.TextToCeasar(text)
        elif com1=="Binary" and com2=="Text":
            return_=x.BinaryToText(text)
        elif com1=="Binary" and com2=="Decimal":
            return_=x.BinaryToDecimal(text)
        elif com1=="Binary" and com2=="Hex":
            return_=x.BinaryToHex(text)
        elif com1=="Binary" and com2=="Octal":
            return_=x.BinaryToOctal(text)
        elif com1=="Binary" and com2=="Ceasar":
            return_=x.BinaryToCeasar(text)
        elif com1=="Decimal" and com2=="Text":
            return_=x.DecimalToText(text)
        elif com1=="Decimal" and com2=="Binary":
            return_=x.DecimalToBinary(text)
        elif com1=="Decimal" and com2=="Hex":
            return_=x.DecimalToHex(text)
        elif com1=="Decimal" and com2=="Octal":
            return_=x.DecimalToOctal(text)
        elif com1=="Decimal" and com2=="Ceasar":
            return_=x.DecimalToCeasar(text)
        elif com1=="Hex" and com2=="Text":
            return_=x.HexToText(text)
        elif com1=="Hex" and com2=="Binary":
            return_=x.HexToBinary(text)
        elif com1=="Hex" and com2=="Decimal":
            return_=x.HexToDecimal(text)
        elif com1=="Hex" and com2=="Octal":
            return_=x.HexToOctal(text)
        elif com1=="Hex" and com2=="Ceasar":
            return_=x.HexToCeasar(text)
        elif com1=="Octal" and com2=="Text":
            return_=x.OctalToText(text)
        elif com1=="Octal" and com2=="Binary":
            return_=x.OctalToBinary(text)
        elif com1=="Octal" and com2=="Decimal":
            return_=x.OctalToDecimal(text)
        elif com1=="Octal" and com2=="Hex":
            return_=x.OctalToHex(text)
        elif com1=="Octal" and com2=="Ceasar":
            return_=x.OctalToCeasar(text)
        elif com1=="Ceasar" and com2=="Text":
            return_=x.CeasarToText(text)
        elif com1=="Ceasar" and com2=="Binary":
            return_=x.CeasarToBinary(text)
        elif com1=="Ceasar" and com2=="Decimal":
            return_=x.CeasarToText(text)
        elif com1=="Ceasar" and com2=="Hex":
            return_=x.CeasarToHex(text)
        elif com1=="Ceasar" and com2=="Octal":
            return_=x.CeasarToOctal(text)
        else:
            return_=""
        self.textEdit.setPlainText(return_)
def main():
    app=QApplication(sys.argv)
    win=mainApp()
    win.show()
    app.exec_()
if __name__ == '__main__':
    main()
