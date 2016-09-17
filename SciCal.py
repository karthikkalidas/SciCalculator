import sys
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "scical.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):

	def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.addButton.clicked.connect(self.add)
        self.subtractButton.clicked.connect(self.subtract)
        self.multiplyButton.clicked.connect(self.multiply)
        self.divideButton.clicked.connect(self.divide)
        self.numeral_1.clicked.connect(self.num1)
        self.numeral_2.clicked.connect(self.num2)
        self.numeral_3.clicked.connect(self.num3)
        self.numeral_4.clicked.connect(self.num4)
        self.numeral_5.clicked.connect(self.num5)
        self.numeral_6.clicked.connect(self.num6)
        self.numeral_7.clicked.connect(self.num7)
        self.numeral_8.clicked.connect(self.num8)
        self.numeral_9.clicked.connect(self.num9)
        self.numeral_0.clicked.connect(self.num10)
        self.addButton.clicked.connect(self.Add)
        self.addButton.clicked.connect(self.Add)
        self.addButton.clicked.connect(self.Add)
        self.addButton.clicked.connect(self.Add)
        self.addButton.clicked.connect(self.Add)


	def Add(self):
		;
        

 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())