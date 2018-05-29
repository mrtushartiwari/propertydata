import sys
import os
import main_page_rc
import json

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 651)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-image: url(:/bc/main_image.jpg);")
        
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(170, 270, 301, 27))
        self.lineEdit1.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.textChanged.connect(self.name_text)
        regex1 = QtCore.QRegExp("[a-z-A-Z_ ]+")
        validator1 = QtGui.QRegExpValidator(regex1)
        self.lineEdit1.setValidator(validator1)
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 330, 51, 17))
        self.label_2.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.label_2.setObjectName("label_2")
        
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(170, 330, 301, 27))
        self.lineEdit2.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.textChanged.connect(self.email_text)
        regex2 = QtCore.QRegExp("[a-z-A-Z_1-9-0.@a-z-A-Z_.]+")
        validator2 = QtGui.QRegExpValidator(regex2)
        self.lineEdit2.setValidator(validator2)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 270, 51, 17))
        self.label.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.label.setObjectName("label")
        
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(360, 390, 99, 27))
        self.exitButton.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.exit_page)
        
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(90, 140, 561, 51))
        self.textBrowser.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(110, 390, 99, 27))
        self.nextButton.setStyleSheet("background-image: url(:/bc/plane.jpg);")
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.next_page)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Email :"))
        self.label.setText(_translate("Form", "Name:"))
        self.exitButton.setText(_translate("Form", "Exit"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">The Real Estate Price Prediction System </span></p></body></html>"))
        self.nextButton.setText(_translate("Form", "Next"))
        
    def name_text(self):
        global nou
        nou = self.lineEdit1.text()

    def email_text(self):
        global eou
        eou = self.lineEdit2.text()

    def next_page(self):
        Form.hide()
        global nou
        global eou
        global output
        
        print ("name : ",str(nou))
        print ("email : ",str(eou))
        output={"name":nou,"email":eou}
        print(output)
        with open('data1.json', 'w+') as outfile:
            json.dump(output, outfile)
        os.system("python3 second_page.py")
        sys.exit()

    def exit_page(self):
        '''global nou
        global eou
        print "name : ",str(nou)
        print "email : ",str(eou)'''
        #choice = QtGui.QMessageBox.question(self, 'Warning!!', "Are You Really Want To Close this App ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)		
        #if choice == QtGui.QMessageBox.Yes:
        print ("Babye!!!!")
        sys.exit()
        #else:
        #    pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

