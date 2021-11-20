import sys
import sqlite3
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.printtt)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT name FROM cofe''').fetchall()
        b = []
        for i in result:
            b.append(i[0])
        self.comboBox.addItems(b)
        self.show()
            
    def printtt(self):
        print(self.comboBox.currentText())
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        a = self.comboBox.currentText()
        result = cur.execute('''SELECT * FROM cofe WHERE name = (?)''', (a,)).fetchall()
        self.plainTextEdit.setPlainText(':')
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText('название:')
        self.plainTextEdit.appendPlainText(str(str(result[0][1]) + '\n'))
        self.plainTextEdit.appendPlainText('жарка:')
        self.plainTextEdit.appendPlainText(str(list(['сильная', 'нормальная'])[result[0][2] - 1] + '\n'))
        self.plainTextEdit.appendPlainText('состояние:')
        self.plainTextEdit.appendPlainText(str(list(['порошок', 'зёрна'])[result[0][3] - 1] + '\n'))
        self.plainTextEdit.appendPlainText('вкус:')
        self.plainTextEdit.appendPlainText(str(str(result[0][4]) + '\n'))
        self.plainTextEdit.appendPlainText('цена:')
        self.plainTextEdit.appendPlainText(str(str(result[0][5]) + '\n'))
        self.plainTextEdit.appendPlainText('размер:')
        self.plainTextEdit.appendPlainText(str(str(result[0][6]) + '\n'))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
