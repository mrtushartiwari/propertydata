# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import Second_page_rc
import sys
import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 653)
        MainWindow.setStyleSheet("background-image: url(:/Bc/2.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 181, 41))
        self.textBrowser.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 81, 17))
        self.label.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 81, 17))
        self.label_3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_3.setObjectName("label_3")
        
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(130, 160, 281, 27))
        self.comboBox1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItems(['','0','1','2','3','4','5','6','7','8','9','10'])
        self.comboBox1.setItemText(0, "")
        self.comboBox1.currentIndexChanged.connect(self.bathroom_menu)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 81, 17))
        self.label_4.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_4.setObjectName("label_4")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 91, 17))
        self.label_7.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 320, 91, 17))
        self.label_8.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_8.setObjectName("label_8")
        
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(130, 310, 281, 27))
        self.comboBox4.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItems(['','Co-Operative Society', 'Freehold', 'Leasehol', 'Power of Attorney'])
        self.comboBox4.setItemText(0, "")
        self.comboBox4.currentIndexChanged.connect(self.ownership_menu)
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 370, 91, 17))
        self.label_9.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_9.setObjectName("label_9")
        
        self.comboBox5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox5.setGeometry(QtCore.QRect(130, 360, 281, 27))
        self.comboBox5.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox5.setObjectName("comboBox5")
        self.comboBox5.addItems(['','1 feet', '10 feet', '100 feet', '1000 feet', '11 feet', '110 feet', '114 feet', '12 feet', '120 feet', '13 feet', '131 feet', '14 feet', '15 feet', '150 feet', '16 feet', '160 feet', '164 feet', '17 feet', '170 feet', '18 feet', '180 feet', '19 feet', '190 feet', '196 feet', '2 feet', '20 feet', '200 feet', '209 feet', '219 feet', '22 feet', '23 feet', '24 feet', '25 feet', '250 feet', '26 feet', '262 feet', '27 feet', '271 feet', '29 feet', '295 feet', '30 feet', '300 feet', '32 feet', '328 feet', '34 feet', '35 feet', '350 feet', '36 feet', '38 feet', '39 feet', '40 feet', '400 feet', '42 feet', '45 feet', '48 feet', '49 feet', '492 feet', '5 feet', '50 feet', '500 feet', '52 feet', '54 feet', '55 feet', '59 feet', '6 feet', '60 feet', '65 feet', '656 feet', '6561 feet', '66 feet', '68 feet', '7 feet', '70 feet', '72 feet', '780 feet', '8 feet', '80 feet', '82 feet', '85 feet', '9 feet', '90 feet', '98 feet', '984 feet'])
        self.comboBox5.setItemText(0, "")
        self.comboBox5.currentIndexChanged.connect(self.roadfaceing_menu)
        
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 420, 41, 17))
        self.label_10.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_10.setObjectName("label_10")
        
        self.comboBox6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox6.setGeometry(QtCore.QRect(130, 410, 281, 27))
        self.comboBox6.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox6.setObjectName("comboBox6")
        self.comboBox6.addItems(['','2 - 3 years','0 - 1 year','1 - 2 years','6 - 7 years','2 years','3 - 4 years','10 - 11 years','7 - 8 years','4 - 5 years','5 - 6 years','12 - 13 years','11 - 12 years','1 year','17 years','6 years','12 years','7 years','20 years','20 - 21 years','9 - 10 years','13 - 14 years','19 - 20 years','14 - 15 years','15 years','17 - 18 years','8 - 9 years','19 years','25 years','30 years','3 years','18 - 19 years','26 - 27 years','11 years','21 - 22 years','16 - 17 years','15 - 16 years','30 - 31 years','28 - 29 years','5 years','4 years','9 years','10 years','8 years','13 years','22 - 23 years','18 years','21 years','22 years','14 years','16 years','27 - 28 years','28 years','24 - 25 years','25 - 26 years','40 years','37 - 38 years','35 - 36 years','35 years','41 - 42 years','29 - 30 years','27 years','31 - 32 years','42 years','33 - 34 years','23 years','32 - 33 years','26 years','23 - 24 years'])
        self.comboBox6.setItemText(0, "")
        self.comboBox6.currentIndexChanged.connect(self.age_menu)
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 470, 91, 17))
        self.label_11.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_11.setObjectName("label_11")
        
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(130, 460, 281, 27))
        self.lineEdit1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.lineEdit1.setText("")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.textChanged.connect(self.totalfloor_text)
        regex1 = QtCore.QRegExp("[1-9-0]+")
        validator1 = QtGui.QRegExpValidator(regex1)
        self.lineEdit1.setValidator(validator1)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(30, 530, 111, 41))
        self.pushButton1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.next_page)
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(170, 530, 101, 41))
        self.pushButton2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.predict_page)
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(310, 530, 101, 41))
        self.pushButton3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.clicked.connect(self.close_application)
        
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(130, 260, 281, 27))
        self.comboBox3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItems(['','Corner', 'Corner, Garden View', 'Corner, Garden View, Pool View', 'Corner, Garden View, Pool View, Road View', 'Corner, Garden View, Road View', 'Corner, Pool View, Road View', 'Garden View', 'Garden View, Pool View, Road View', 'Pool View', 'Pool View, Corner', 'Pool View, Garden View', 'Road View', 'Road View, Corner', 'Road View, Garden View', 'Road View, Pool View', 'overlooking'])
        self.comboBox3.setItemText(0, "")
        self.comboBox3.currentIndexChanged.connect(self.overlooking_menu)
        
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(130, 210, 281, 27))
        self.comboBox2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItems(['','1','2','3','4','5'])
        self.comboBox2.setItemText(0, "")
        self.comboBox2.currentIndexChanged.connect(self.opensides_menu)
        
        self.comboBox0 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox0.setGeometry(QtCore.QRect(130, 110, 281, 27))
        self.comboBox0.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox0.setObjectName("comboBox0")
        self.comboBox0.addItems(['','0','1','2','3','4','5','6','7','8'])
        self.comboBox0.setItemText(0, "")
        self.comboBox0.currentIndexChanged.connect(self.balconies_menu)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Select Features:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Balconies:"))
        self.label_3.setText(_translate("MainWindow", "Bathroom:"))
        self.label_4.setText(_translate("MainWindow", "Open sides:"))
        self.label_7.setText(_translate("MainWindow", "Overlooking:"))
        self.label_8.setText(_translate("MainWindow", "Ownership:"))
        self.label_9.setText(_translate("MainWindow", "Road facing:"))
        self.label_10.setText(_translate("MainWindow", "Age:"))
        self.label_11.setText(_translate("MainWindow", "Total Floors:"))
        self.pushButton1.setText(_translate("MainWindow", "Next"))
        self.pushButton2.setText(_translate("MainWindow", "Predict"))
        self.pushButton3.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        

    def balconies_menu(self):
        global balconies1
        balconies1 = self.comboBox0.currentText() 
				
    def bathroom_menu(self):
        global bathroom1
        bathroom1 = self.comboBox1.currentText()

    def opensides_menu(self):
        global opensides1
        opensides1 = self.comboBox2.currentText()

    def overlooking_menu(self):
        global overlooking1
        overlooking1 = self.comboBox3.currentText()

    def ownership_menu(self):
        global ownership1
        ownership1 = self.comboBox4.currentText()

    def roadfaceing_menu(self):
        global roadfaceing1
        roadfaceing1 = self.comboBox5.currentText()

    def age_menu(self):
        global age1
        age1 = self.comboBox6.currentText()

    def totalfloor_text(self):
        global totalfloor1
        totalfloor1 = self.lineEdit1.text()

    def next_page(self):	
        print("opening next page")
        MainWindow.hide()
        global balconies1,bathroom1,opensides1,overlooking1,ownership1,projectname1,roadfaceing1,age1,totalfloor1
        print(balconies1)
        print(bathroom1)
        print(opensides1)
        print(overlooking1)
        print(ownership1)
        print(roadfaceing1)
        print(age1)
        print(totalfloor1)
        global output
        output = {"balconies1":str(balconies1),"bathroom1":str(bathroom1),\
        "opensides1":str(opensides1),"overlooking1":str(overlooking1),\
        "ownership1":str(ownership1),"roadfaceing1":str(roadfaceing1),\
        "age1":str(age1),"totalfloor1":str(totalfloor1)}
        print(output)
        
        with open('data3.json', 'w+') as outfile:
            json.dump(output, outfile)
        print(output)
        #MainWindow.hide()
        os.system("python3 fourth_page.py")
        
        sys.exit()

    def predict_page(self):	
        print("opening next page")
        MainWindow.hide()
        global output
        output = [str(balconies1),str(bathroom1),str(opensides1),str(overlooking1),str(ownership1),str(roadfaceing1),str(age1),str(totalfloor1)]
        print(output)
        #MainWindow.hide()
        os.system("python3 output_page.py")
        
        sys.exit()

    def close_application(self):
        #choice = QtGui.QMessageBox.question(self, 'Warning!!', "Do You Really Want To Close this App ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)		
        #if choice == QtGui.QMessageBox.Yes:
        print ("Babye!!!!")
        sys.exit()
        #else:
        #	pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

