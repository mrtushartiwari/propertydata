# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourth_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import Second_page_rc
import json

from PyQt5 import QtCore, QtGui, QtWidgets

Lift_Available1 = Car_Parking1 = Power_Backup1 = Security1 = Childrens_play_area1 = Club_House1 = Gymnasium1 = Swimming_Pool1 = Sports_Facility1 = ""
Indoor_Games1 = Jogging_Track1 = Maintenance_Staff1 = Rain_Water_Harvesting1 = Intercom1 = Golf_Course1 = Cafeteria1 = Staff_Quarter1 = Multipurpose_Room1 = ""
Landscaped_Gardens1 = Shopping_Mall1 = School1 = Hospital1 = ATM1 = AC1 = Wardrobe1 = TV1 = Refrigerator1 = Sofa1 = Washing_Machine1 = wifi1 = Microwave1 = ""
Dining_Table1 = Gas_connection1 = BED1 = ""
output = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 862)
        MainWindow.setStyleSheet("background-image: url(:/Bc/2.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 191, 41))
        self.textBrowser.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 101, 17))
        self.label.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label.setObjectName("label")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(120, 750, 101, 41))
        self.pushButton1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.predict_page)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(460, 750, 101, 41))
        self.pushButton2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton1.clicked.connect(self.close_application)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 91, 17))
        self.label_2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 101, 17))
        self.label_3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 101, 17))
        self.label_4.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 141, 21))
        self.label_5.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 370, 91, 17))
        self.label_6.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 91, 17))
        self.label_7.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 470, 111, 17))
        self.label_8.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 520, 101, 17))
        self.label_9.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 570, 101, 17))
        self.label_10.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(19, 619, 101, 17))
        self.label_11.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(18, 669, 131, 17))
        self.label_12.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(358, 369, 141, 17))
        self.label_13.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(358, 219, 71, 17))
        self.label_14.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(358, 469, 111, 17))
        self.label_15.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(358, 569, 81, 17))
        self.label_16.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(358, 169, 101, 17))
        self.label_17.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(358, 269, 161, 17))
        self.label_18.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(358, 319, 101, 21))
        self.label_19.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(358, 119, 101, 17))
        self.label_20.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(358, 419, 151, 17))
        self.label_21.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(357, 618, 111, 17))
        self.label_22.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(358, 519, 131, 17))
        self.label_23.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(356, 668, 91, 17))
        self.label_24.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(720, 419, 41, 17))
        self.label_25.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(720, 269, 41, 17))
        self.label_26.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(720, 319, 91, 21))
        self.label_27.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(720, 169, 31, 17))
        self.label_28.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(720, 369, 91, 17))
        self.label_29.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(720, 219, 31, 17))
        self.label_30.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(720, 119, 41, 17))
        self.label_31.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_31.setObjectName("label_31") 

        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(720, 530, 101, 21))
        self.label_33.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(720, 580, 51, 17))
        self.label_34.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(720, 630, 61, 17))
        self.label_35.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_35.setObjectName("label_35")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(720, 670, 41, 17))
        self.label_32.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_32.setObjectName("label_32")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(750, 470, 141, 31))
        self.textBrowser_2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(169, 120, 114, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton1 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton1.setObjectName("radioButton1")
        self.horizontalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout.addWidget(self.radioButton2)
        self.radioButton1.setCheckable(True)
        self.radioButton1.toggled.connect(self.Lift_Available_menu)
        self.radioButton2.setCheckable(True)
        self.radioButton2.toggled.connect(self.Lift_Available_menu)
        

        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(170, 171, 114, 24))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton3 = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton3.setObjectName("radioButton3")
        self.horizontalLayout_2.addWidget(self.radioButton3)
        self.radioButton4 = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton4.setObjectName("radioButton4")
        self.horizontalLayout_2.addWidget(self.radioButton4)
        self.radioButton3.setCheckable(True)
        self.radioButton3.toggled.connect(self.Car_Parking_menu)
        self.radioButton4.setCheckable(True)
        self.radioButton4.toggled.connect(self.Car_Parking_menu)

        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(170, 221, 114, 24))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton5 = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton5.setObjectName("radioButton5")
        self.horizontalLayout_3.addWidget(self.radioButton5)
        self.radioButton6 = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton6.setObjectName("radioButton6")
        self.horizontalLayout_3.addWidget(self.radioButton6)
        self.radioButton5.setCheckable(True)
        self.radioButton5.toggled.connect(self.Power_Backup_menu)
        self.radioButton6.setCheckable(True)
        self.radioButton6.toggled.connect(self.Power_Backup_menu)

        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(170, 271, 114, 24))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton7 = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton7.setObjectName("radioButton7")
        self.horizontalLayout_4.addWidget(self.radioButton7)
        self.radioButton8 = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton8.setObjectName("radioButton8")
        self.horizontalLayout_4.addWidget(self.radioButton8)
        self.radioButton7.setCheckable(True)
        self.radioButton7.toggled.connect(self.Security_menu)
        self.radioButton8.setCheckable(True)
        self.radioButton8.toggled.connect(self.Security_menu)        

        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(170, 321, 114, 24))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton9 = QtWidgets.QRadioButton(self.layoutWidget6)
        self.radioButton9.setObjectName("radioButton9")
        self.horizontalLayout_5.addWidget(self.radioButton9)
        self.radioButton10 = QtWidgets.QRadioButton(self.layoutWidget6)
        self.radioButton10.setObjectName("radioButton10")
        self.horizontalLayout_5.addWidget(self.radioButton10)
        self.radioButton9.setCheckable(True)
        self.radioButton9.toggled.connect(self.Childrens_play_area_menu)
        self.radioButton10.setCheckable(True)
        self.radioButton10.toggled.connect(self.Childrens_play_area_menu)
        

        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(170, 371, 114, 24))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton11 = QtWidgets.QRadioButton(self.layoutWidget7)
        self.radioButton11.setObjectName("radioButton11")
        self.horizontalLayout_6.addWidget(self.radioButton11)
        self.radioButton12 = QtWidgets.QRadioButton(self.layoutWidget7)
        self.radioButton12.setObjectName("radioButton12")
        self.horizontalLayout_6.addWidget(self.radioButton12)
        self.radioButton11.setCheckable(True)
        self.radioButton11.toggled.connect(self.Club_House_menu)
        self.radioButton12.setCheckable(True)
        self.radioButton12.toggled.connect(self.Club_House_menu)

        self.layoutWidget8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(170, 421, 114, 24))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton13 = QtWidgets.QRadioButton(self.layoutWidget8)
        self.radioButton13.setObjectName("radioButton13")
        self.horizontalLayout_7.addWidget(self.radioButton13)
        self.radioButton14 = QtWidgets.QRadioButton(self.layoutWidget8)
        self.radioButton14.setObjectName("radioButton14")
        self.horizontalLayout_7.addWidget(self.radioButton14)
        self.radioButton13.setCheckable(True)
        self.radioButton13.toggled.connect(self.Gymnasium_menu)
        self.radioButton14.setCheckable(True)
        self.radioButton14.toggled.connect(self.Gymnasium_menu)
        

        self.layoutWidget9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget9.setGeometry(QtCore.QRect(170, 471, 114, 24))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButton15 = QtWidgets.QRadioButton(self.layoutWidget9)
        self.radioButton15.setObjectName("radioButton15")
        self.horizontalLayout_8.addWidget(self.radioButton15)
        self.radioButton16 = QtWidgets.QRadioButton(self.layoutWidget9)
        self.radioButton16.setObjectName("radioButton16")
        self.horizontalLayout_8.addWidget(self.radioButton16)
        self.radioButton15.setCheckable(True)
        self.radioButton15.toggled.connect(self.Swimming_Pool_menu)
        self.radioButton16.setCheckable(True)
        self.radioButton16.toggled.connect(self.Swimming_Pool_menu)

        self.layoutWidget10 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget10.setGeometry(QtCore.QRect(170, 521, 114, 24))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.radioButton17 = QtWidgets.QRadioButton(self.layoutWidget10)
        self.radioButton17.setObjectName("radioButton17")
        self.horizontalLayout_9.addWidget(self.radioButton17)
        self.radioButton18 = QtWidgets.QRadioButton(self.layoutWidget10)
        self.radioButton18.setObjectName("radioButton18")
        self.horizontalLayout_9.addWidget(self.radioButton18)
        self.radioButton17.setCheckable(True)
        self.radioButton17.toggled.connect(self.Sports_Facility_menu)
        self.radioButton18.setCheckable(True)
        self.radioButton18.toggled.connect(self.Sports_Facility_menu)

        self.layoutWidget11 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget11.setGeometry(QtCore.QRect(170, 571, 114, 24))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.radioButton19 = QtWidgets.QRadioButton(self.layoutWidget11)
        self.radioButton19.setObjectName("radioButton19")
        self.horizontalLayout_10.addWidget(self.radioButton19)
        self.radioButton20 = QtWidgets.QRadioButton(self.layoutWidget11)
        self.radioButton20.setObjectName("radioButton20")
        self.horizontalLayout_10.addWidget(self.radioButton20)
        self.radioButton19.setCheckable(True)
        self.radioButton19.toggled.connect(self.Indoor_Games_menu)
        self.radioButton20.setCheckable(True)
        self.radioButton20.toggled.connect(self.Indoor_Games_menu)
        

        self.layoutWidget12 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget12.setGeometry(QtCore.QRect(169, 620, 114, 24))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.radioButton21 = QtWidgets.QRadioButton(self.layoutWidget12)
        self.radioButton21.setObjectName("radioButton21")
        self.horizontalLayout_11.addWidget(self.radioButton21)
        self.radioButton22 = QtWidgets.QRadioButton(self.layoutWidget12)
        self.radioButton22.setObjectName("radioButton22")
        self.horizontalLayout_11.addWidget(self.radioButton22)
        self.radioButton21.setCheckable(True)
        self.radioButton21.toggled.connect(self.Jogging_Track_menu)
        self.radioButton22.setCheckable(True)
        self.radioButton22.toggled.connect(self.Jogging_Track_menu)

        self.layoutWidget13 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget13.setGeometry(QtCore.QRect(168, 670, 114, 24))
        self.layoutWidget13.setObjectName("layoutWidget13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.radioButton23 = QtWidgets.QRadioButton(self.layoutWidget13)
        self.radioButton23.setObjectName("radioButton23")
        self.horizontalLayout_12.addWidget(self.radioButton23)
        self.radioButton24 = QtWidgets.QRadioButton(self.layoutWidget13)
        self.radioButton24.setObjectName("radioButton24")
        self.horizontalLayout_12.addWidget(self.radioButton24)
        self.radioButton23.setCheckable(True)
        self.radioButton23.toggled.connect(self.Maintenance_Staff_menu)
        self.radioButton24.setCheckable(True)
        self.radioButton24.toggled.connect(self.Maintenance_Staff_menu)

        self.layoutWidget14 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget14.setGeometry(QtCore.QRect(529, 119, 114, 24))
        self.layoutWidget14.setObjectName("layoutWidget14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.radioButton25 = QtWidgets.QRadioButton(self.layoutWidget14)
        self.radioButton25.setObjectName("radioButton25")
        self.horizontalLayout_13.addWidget(self.radioButton25)
        self.radioButton26 = QtWidgets.QRadioButton(self.layoutWidget14)
        self.radioButton26.setObjectName("radioButton26")
        self.horizontalLayout_13.addWidget(self.radioButton26)
        self.radioButton25.setCheckable(True)
        self.radioButton25.toggled.connect(self.Intercom_menu)
        self.radioButton26.setCheckable(True)
        self.radioButton26.toggled.connect(self.Intercom_menu)

        self.layoutWidget15 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget15.setGeometry(QtCore.QRect(530, 170, 114, 24))
        self.layoutWidget15.setObjectName("layoutWidget15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.radioButton27 = QtWidgets.QRadioButton(self.layoutWidget15)
        self.radioButton27.setObjectName("radioButton27")
        self.horizontalLayout_14.addWidget(self.radioButton27)
        self.radioButton28 = QtWidgets.QRadioButton(self.layoutWidget15)
        self.radioButton28.setObjectName("radioButton28")
        self.horizontalLayout_14.addWidget(self.radioButton28)
        self.radioButton27.setCheckable(True)
        self.radioButton27.toggled.connect(self.Golf_Course_menu)
        self.radioButton28.setCheckable(True)
        self.radioButton28.toggled.connect(self.Golf_Course_menu)

        self.layoutWidget16 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget16.setGeometry(QtCore.QRect(530, 220, 114, 24))
        self.layoutWidget16.setObjectName("layoutWidget16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget16)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.radioButton29 = QtWidgets.QRadioButton(self.layoutWidget16)
        self.radioButton29.setObjectName("radioButton29")
        self.horizontalLayout_15.addWidget(self.radioButton29)
        self.radioButton30 = QtWidgets.QRadioButton(self.layoutWidget16)
        self.radioButton30.setObjectName("radioButton30")
        self.horizontalLayout_15.addWidget(self.radioButton30)
        self.radioButton29.setCheckable(True)
        self.radioButton29.toggled.connect(self.Cafeteria_menu)
        self.radioButton30.setCheckable(True)
        self.radioButton30.toggled.connect(self.Cafeteria_menu)

        self.layoutWidget17 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget17.setGeometry(QtCore.QRect(530, 270, 114, 24))
        self.layoutWidget17.setObjectName("layoutWidget17")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.layoutWidget17)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton31 = QtWidgets.QRadioButton(self.layoutWidget17)
        self.radioButton31.setObjectName("radioButton31")
        self.horizontalLayout_16.addWidget(self.radioButton31)
        self.radioButton32 = QtWidgets.QRadioButton(self.layoutWidget17)
        self.radioButton32.setObjectName("radioButton32")
        self.horizontalLayout_16.addWidget(self.radioButton32)
        self.radioButton31.setCheckable(True)
        self.radioButton31.toggled.connect(self.Rain_Water_Harvesting_menu)
        self.radioButton32.setCheckable(True)
        self.radioButton32.toggled.connect(self.Rain_Water_Harvesting_menu)

        self.layoutWidget18 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget18.setGeometry(QtCore.QRect(530, 320, 114, 24))
        self.layoutWidget18.setObjectName("layoutWidget18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.layoutWidget18)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.radioButton33 = QtWidgets.QRadioButton(self.layoutWidget18)
        self.radioButton33.setObjectName("radioButton33")
        self.horizontalLayout_17.addWidget(self.radioButton33)
        self.radioButton34 = QtWidgets.QRadioButton(self.layoutWidget18)
        self.radioButton34.setObjectName("radioButton34")
        self.horizontalLayout_17.addWidget(self.radioButton34)
        self.radioButton33.setCheckable(True)
        self.radioButton33.toggled.connect(self.Staff_Quarter_menu)
        self.radioButton34.setCheckable(True)
        self.radioButton34.toggled.connect(self.Staff_Quarter_menu)

        self.layoutWidget19 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget19.setGeometry(QtCore.QRect(530, 370, 114, 24))
        self.layoutWidget19.setObjectName("layoutWidget19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.layoutWidget19)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.radioButton35 = QtWidgets.QRadioButton(self.layoutWidget19)
        self.radioButton35.setObjectName("radioButton35")
        self.horizontalLayout_18.addWidget(self.radioButton35)
        self.radioButton36 = QtWidgets.QRadioButton(self.layoutWidget19)
        self.radioButton36.setObjectName("radioButton36")
        self.horizontalLayout_18.addWidget(self.radioButton36)
        self.radioButton35.setCheckable(True)
        self.radioButton35.toggled.connect(self.Multipurpose_Room_menu)
        self.radioButton36.setCheckable(True)
        self.radioButton36.toggled.connect(self.Multipurpose_Room_menu)

        self.layoutWidget20 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget20.setGeometry(QtCore.QRect(530, 420, 114, 24))
        self.layoutWidget20.setObjectName("layoutWidget20")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.layoutWidget20)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.radioButton37 = QtWidgets.QRadioButton(self.layoutWidget20)
        self.radioButton37.setObjectName("radioButton37")
        self.horizontalLayout_19.addWidget(self.radioButton37)
        self.radioButton38 = QtWidgets.QRadioButton(self.layoutWidget20)
        self.radioButton38.setObjectName("radioButton38")
        self.horizontalLayout_19.addWidget(self.radioButton38)
        self.radioButton37.setCheckable(True)
        self.radioButton37.toggled.connect(self.Landscaped_Gardens_menu)
        self.radioButton38.setCheckable(True)
        self.radioButton38.toggled.connect(self.Landscaped_Gardens_menu)

        self.layoutWidget21 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget21.setGeometry(QtCore.QRect(530, 470, 114, 24))
        self.layoutWidget21.setObjectName("layoutWidget21")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.layoutWidget21)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.radioButton39 = QtWidgets.QRadioButton(self.layoutWidget21)
        self.radioButton39.setObjectName("radioButton39")
        self.horizontalLayout_20.addWidget(self.radioButton39)
        self.radioButton40 = QtWidgets.QRadioButton(self.layoutWidget21)
        self.radioButton40.setObjectName("radioButton40")
        self.horizontalLayout_20.addWidget(self.radioButton40)
        self.radioButton39.setCheckable(True)
        self.radioButton39.toggled.connect(self.Shopping_Mall_menu)
        self.radioButton40.setCheckable(True)
        self.radioButton40.toggled.connect(self.Shopping_Mall_menu)

        self.layoutWidget22 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget22.setGeometry(QtCore.QRect(530, 520, 114, 24))
        self.layoutWidget22.setObjectName("layoutWidget22")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.layoutWidget22)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.radioButton41 = QtWidgets.QRadioButton(self.layoutWidget22)
        self.radioButton41.setObjectName("radioButton41")
        self.horizontalLayout_21.addWidget(self.radioButton41)
        self.radioButton42 = QtWidgets.QRadioButton(self.layoutWidget22)
        self.radioButton42.setObjectName("radioButton42")
        self.horizontalLayout_21.addWidget(self.radioButton42)
        self.radioButton41.setCheckable(True)
        self.radioButton41.toggled.connect(self.Washing_Machine_menu)
        self.radioButton42.setCheckable(True)
        self.radioButton42.toggled.connect(self.Washing_Machine_menu)

        self.layoutWidget23 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget23.setGeometry(QtCore.QRect(530, 570, 114, 24))
        self.layoutWidget23.setObjectName("layoutWidget23")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.layoutWidget23)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.radioButton43 = QtWidgets.QRadioButton(self.layoutWidget23)
        self.radioButton43.setObjectName("radioButton43")
        self.horizontalLayout_22.addWidget(self.radioButton43)
        self.radioButton44 = QtWidgets.QRadioButton(self.layoutWidget23)
        self.radioButton44.setObjectName("radioButton44")
        self.horizontalLayout_22.addWidget(self.radioButton44)
        self.radioButton43.setCheckable(True)
        self.radioButton43.toggled.connect(self.Wardrobe_menu)
        self.radioButton44.setCheckable(True)
        self.radioButton44.toggled.connect(self.Wardrobe_menu)

        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(529, 619, 114, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.radioButton45 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton45.setObjectName("radioButton45")
        self.horizontalLayout_23.addWidget(self.radioButton45)
        self.radioButton46 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton46.setObjectName("radioButton46")
        self.horizontalLayout_23.addWidget(self.radioButton46)
        self.radioButton45.setCheckable(True)
        self.radioButton45.toggled.connect(self.Gas_connection_menu)
        self.radioButton46.setCheckable(True)
        self.radioButton46.toggled.connect(self.Gas_connection_menu)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(528, 669, 114, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.radioButton47 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton47.setObjectName("radioButton47")
        self.horizontalLayout_24.addWidget(self.radioButton47)
        self.radioButton48 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton48.setObjectName("radioButton48")
        self.horizontalLayout_24.addWidget(self.radioButton48)
        self.radioButton47.setCheckable(True)
        self.radioButton47.toggled.connect(self.Refrigerator_menu)
        self.radioButton48.setCheckable(True)
        self.radioButton48.toggled.connect(self.Refrigerator_menu)

        self.layoutWidget24 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget24.setGeometry(QtCore.QRect(819, 119, 114, 24))
        self.layoutWidget24.setObjectName("layoutWidget24")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.layoutWidget24)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.radioButton49 = QtWidgets.QRadioButton(self.layoutWidget24)
        self.radioButton49.setObjectName("radioButton49")
        self.horizontalLayout_25.addWidget(self.radioButton49)
        self.radioButton50 = QtWidgets.QRadioButton(self.layoutWidget24)
        self.radioButton50.setObjectName("radioButton50")
        self.horizontalLayout_25.addWidget(self.radioButton50)
        self.radioButton49.setCheckable(True)
        self.radioButton49.toggled.connect(self.Sofa_menu)
        self.radioButton50.setCheckable(True)
        self.radioButton50.toggled.connect(self.Sofa_menu)

        self.layoutWidget25 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget25.setGeometry(QtCore.QRect(820, 170, 114, 24))
        self.layoutWidget25.setObjectName("layoutWidget25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.layoutWidget25)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.radioButton51 = QtWidgets.QRadioButton(self.layoutWidget25)
        self.radioButton51.setObjectName("radioButton51")
        self.horizontalLayout_26.addWidget(self.radioButton51)
        self.radioButton52 = QtWidgets.QRadioButton(self.layoutWidget25)
        self.radioButton52.setObjectName("radioButton52")
        self.horizontalLayout_26.addWidget(self.radioButton52)
        self.radioButton51.setCheckable(True)
        self.radioButton51.toggled.connect(self.AC_menu)
        self.radioButton52.setCheckable(True)
        self.radioButton52.toggled.connect(self.AC_menu)

        self.layoutWidget26 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget26.setGeometry(QtCore.QRect(820, 220, 114, 24))
        self.layoutWidget26.setObjectName("layoutWidget26")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.layoutWidget26)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.radioButton53 = QtWidgets.QRadioButton(self.layoutWidget26)
        self.radioButton53.setObjectName("radioButton53")
        self.horizontalLayout_27.addWidget(self.radioButton53)
        self.radioButton54 = QtWidgets.QRadioButton(self.layoutWidget26)
        self.radioButton54.setObjectName("radioButton54")
        self.horizontalLayout_27.addWidget(self.radioButton54)
        self.radioButton53.setCheckable(True)
        self.radioButton53.toggled.connect(self.TV_menu)
        self.radioButton54.setCheckable(True)
        self.radioButton54.toggled.connect(self.TV_menu)

        self.layoutWidget27 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget27.setGeometry(QtCore.QRect(820, 270, 114, 24))
        self.layoutWidget27.setObjectName("layoutWidget27")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.layoutWidget27)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.radioButton55 = QtWidgets.QRadioButton(self.layoutWidget27)
        self.radioButton55.setObjectName("radioButton55")
        self.horizontalLayout_28.addWidget(self.radioButton55)
        self.radioButton56 = QtWidgets.QRadioButton(self.layoutWidget27)
        self.radioButton56.setObjectName("radioButton56")
        self.horizontalLayout_28.addWidget(self.radioButton56)
        self.radioButton55.setCheckable(True)
        self.radioButton55.toggled.connect(self.Wifi_menu)
        self.radioButton56.setCheckable(True)
        self.radioButton56.toggled.connect(self.Wifi_menu)

        self.layoutWidget28 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget28.setGeometry(QtCore.QRect(820, 320, 114, 24))
        self.layoutWidget28.setObjectName("layoutWidget28")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.layoutWidget28)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.radioButton57 = QtWidgets.QRadioButton(self.layoutWidget28)
        self.radioButton57.setObjectName("radioButton57")
        self.horizontalLayout_29.addWidget(self.radioButton57)
        self.radioButton58 = QtWidgets.QRadioButton(self.layoutWidget28)
        self.radioButton58.setObjectName("radioButton58")
        self.horizontalLayout_29.addWidget(self.radioButton58)
        self.radioButton57.setCheckable(True)
        self.radioButton57.toggled.connect(self.Microwave_menu)
        self.radioButton58.setCheckable(True)
        self.radioButton58.toggled.connect(self.Microwave_menu)

        self.layoutWidget29 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget29.setGeometry(QtCore.QRect(820, 370, 114, 24))
        self.layoutWidget29.setObjectName("layoutWidget29")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.layoutWidget29)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.radioButton59 = QtWidgets.QRadioButton(self.layoutWidget29)
        self.radioButton59.setObjectName("radioButton59")
        self.horizontalLayout_30.addWidget(self.radioButton59)
        self.radioButton60 = QtWidgets.QRadioButton(self.layoutWidget29)
        self.radioButton60.setObjectName("radioButton60")
        self.horizontalLayout_30.addWidget(self.radioButton60)
        self.radioButton59.setCheckable(True)
        self.radioButton59.toggled.connect(self.Dining_Table_menu)
        self.radioButton60.setCheckable(True)
        self.radioButton60.toggled.connect(self.Dining_Table_menu)

        self.layoutWidget30 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget30.setGeometry(QtCore.QRect(821, 421, 114, 24))
        self.layoutWidget30.setObjectName("layoutWidget30")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.layoutWidget30)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.radioButton61 = QtWidgets.QRadioButton(self.layoutWidget30)
        self.radioButton61.setObjectName("radioButton61")
        self.horizontalLayout_31.addWidget(self.radioButton61)
        self.radioButton62 = QtWidgets.QRadioButton(self.layoutWidget30)
        self.radioButton62.setObjectName("radioButton62")
        self.horizontalLayout_31.addWidget(self.radioButton62)
        self.radioButton61.setCheckable(True)
        self.radioButton61.toggled.connect(self.BED_menu)
        self.radioButton62.setCheckable(True)
        self.radioButton62.toggled.connect(self.BED_menu)

        self.layoutWidget31 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget31.setGeometry(QtCore.QRect(829, 530, 114, 24))
        self.layoutWidget31.setObjectName("layoutWidget31")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.layoutWidget31)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.radioButton63 = QtWidgets.QRadioButton(self.layoutWidget31)
        self.radioButton63.setObjectName("radioButton63")
        self.horizontalLayout_32.addWidget(self.radioButton63)
        self.radioButton64 = QtWidgets.QRadioButton(self.layoutWidget31)
        self.radioButton64.setObjectName("radioButton64")
        self.horizontalLayout_32.addWidget(self.radioButton64)
        self.radioButton63.setCheckable(True)
        self.radioButton63.toggled.connect(self.Shopping_Mall_menu)
        self.radioButton64.setCheckable(True)
        self.radioButton64.toggled.connect(self.Shopping_Mall_menu)

        self.layoutWidget32 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget32.setGeometry(QtCore.QRect(829, 580, 114, 24))
        self.layoutWidget32.setObjectName("layoutWidget32")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.layoutWidget32)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.radioButton65 = QtWidgets.QRadioButton(self.layoutWidget32)
        self.radioButton65.setObjectName("radioButton65")
        self.horizontalLayout_33.addWidget(self.radioButton65)
        self.radioButton66 = QtWidgets.QRadioButton(self.layoutWidget32)
        self.radioButton66.setObjectName("radioButton66")
        self.horizontalLayout_33.addWidget(self.radioButton66)
        self.radioButton65.setCheckable(True)
        self.radioButton65.toggled.connect(self.School_menu)
        self.radioButton66.setCheckable(True)
        self.radioButton66.toggled.connect(self.School_menu)

        self.layoutWidget33 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget33.setGeometry(QtCore.QRect(829, 630, 114, 24))
        self.layoutWidget33.setObjectName("layoutWidget33")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.layoutWidget33)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.radioButton67 = QtWidgets.QRadioButton(self.layoutWidget33)
        self.radioButton67.setObjectName("radioButton67")
        self.horizontalLayout_34.addWidget(self.radioButton67)
        self.radioButton68 = QtWidgets.QRadioButton(self.layoutWidget33)
        self.radioButton68.setObjectName("radioButton68")
        self.horizontalLayout_34.addWidget(self.radioButton68)
        self.radioButton67.setCheckable(True)
        self.radioButton67.toggled.connect(self.Hospital_menu)
        self.radioButton68.setCheckable(True)
        self.radioButton68.toggled.connect(self.Hospital_menu)

        self.layoutWidget34 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget34.setGeometry(QtCore.QRect(829, 670, 114, 24))
        self.layoutWidget34.setObjectName("layoutWidget34")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.layoutWidget34)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.radioButton69 = QtWidgets.QRadioButton(self.layoutWidget34)
        self.radioButton69.setObjectName("radioButton69")
        self.horizontalLayout_35.addWidget(self.radioButton69)
        self.radioButton70 = QtWidgets.QRadioButton(self.layoutWidget34)
        self.radioButton70.setObjectName("radioButton70")
        self.horizontalLayout_35.addWidget(self.radioButton70)
        self.radioButton69.setCheckable(True)
        self.radioButton69.toggled.connect(self.ATM_menu)
        self.radioButton70.setCheckable(True)
        self.radioButton70.toggled.connect(self.ATM_menu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 25))
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
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Select Amenities:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Lift Available:"))
        self.pushButton1.setText(_translate("MainWindow", "Predict"))
        self.pushButton2.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Car Parking:"))
        self.label_3.setText(_translate("MainWindow", "Power Backup:"))
        self.label_4.setText(_translate("MainWindow", "24*7 Security:"))
        self.label_5.setText(_translate("MainWindow", "Children\'s play area:"))
        self.label_6.setText(_translate("MainWindow", "Club House:"))
        self.label_7.setText(_translate("MainWindow", "Gymnasium: "))
        self.label_8.setText(_translate("MainWindow", "Swimming Pool:"))
        self.label_9.setText(_translate("MainWindow", "Sports Facility:"))
        self.label_10.setText(_translate("MainWindow", "Indoor Games:"))
        self.label_11.setText(_translate("MainWindow", "Jogging Track:"))
        self.label_12.setText(_translate("MainWindow", "Maintenance Staff:"))
        self.label_13.setText(_translate("MainWindow", "Multipurpose Room:"))
        self.label_14.setText(_translate("MainWindow", "Cafeteria:"))
        self.label_15.setText(_translate("MainWindow", "Shopping Mall:"))
        self.label_16.setText(_translate("MainWindow", "Wardrobe:"))
        self.label_17.setText(_translate("MainWindow", "Golf Course:"))
        self.label_18.setText(_translate("MainWindow", "Rain Water Harvesting:"))
        self.label_19.setText(_translate("MainWindow", "Staff Quarter:"))
        self.label_20.setText(_translate("MainWindow", "Intercom:"))
        self.label_21.setText(_translate("MainWindow", "Landscaped Gardens:"))
        self.label_22.setText(_translate("MainWindow", "Gas connection:"))
        self.label_23.setText(_translate("MainWindow", "Washing Machine:"))
        self.label_24.setText(_translate("MainWindow", "Refrigerator:"))
        self.label_25.setText(_translate("MainWindow", "BED: "))
        self.label_26.setText(_translate("MainWindow", "Wifi:"))
        self.label_27.setText(_translate("MainWindow", "Microwave:"))
        self.label_28.setText(_translate("MainWindow", "AC:"))
        self.label_29.setText(_translate("MainWindow", "Dining Table:"))
        self.label_30.setText(_translate("MainWindow", "TV:"))
        self.label_31.setText(_translate("MainWindow", "Sofa: "))
        self.radioButton47.setText(_translate("MainWindow", "Yes"))
        self.radioButton48.setText(_translate("MainWindow", "No"))
        self.radioButton45.setText(_translate("MainWindow", "Yes"))
        self.radioButton46.setText(_translate("MainWindow", "No"))
        self.label_33.setText(_translate("MainWindow", "Shopping Mall:"))
        self.label_34.setText(_translate("MainWindow", "School:"))
        self.label_35.setText(_translate("MainWindow", "Hospital:"))
        self.label_32.setText(_translate("MainWindow", "ATM:"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Nearby Section:</span></p></body></html>"))
        self.radioButton1.setText(_translate("MainWindow", "Yes"))
        self.radioButton2.setText(_translate("MainWindow", "No"))
        self.radioButton3.setText(_translate("MainWindow", "Yes"))
        self.radioButton4.setText(_translate("MainWindow", "No"))
        self.radioButton5.setText(_translate("MainWindow", "Yes"))
        self.radioButton6.setText(_translate("MainWindow", "No"))
        self.radioButton7.setText(_translate("MainWindow", "Yes"))
        self.radioButton8.setText(_translate("MainWindow", "No"))
        self.radioButton9.setText(_translate("MainWindow", "Yes"))
        self.radioButton10.setText(_translate("MainWindow", "No"))
        self.radioButton11.setText(_translate("MainWindow", "Yes"))
        self.radioButton12.setText(_translate("MainWindow", "No"))
        self.radioButton13.setText(_translate("MainWindow", "Yes"))
        self.radioButton14.setText(_translate("MainWindow", "No"))
        self.radioButton15.setText(_translate("MainWindow", "Yes"))
        self.radioButton16.setText(_translate("MainWindow", "No"))
        self.radioButton17.setText(_translate("MainWindow", "Yes"))
        self.radioButton18.setText(_translate("MainWindow", "No"))
        self.radioButton19.setText(_translate("MainWindow", "Yes"))
        self.radioButton20.setText(_translate("MainWindow", "No"))
        self.radioButton21.setText(_translate("MainWindow", "Yes"))
        self.radioButton22.setText(_translate("MainWindow", "No"))
        self.radioButton23.setText(_translate("MainWindow", "Yes"))
        self.radioButton24.setText(_translate("MainWindow", "No"))
        self.radioButton25.setText(_translate("MainWindow", "Yes"))
        self.radioButton26.setText(_translate("MainWindow", "No"))
        self.radioButton27.setText(_translate("MainWindow", "Yes"))
        self.radioButton28.setText(_translate("MainWindow", "No"))
        self.radioButton29.setText(_translate("MainWindow", "Yes"))
        self.radioButton30.setText(_translate("MainWindow", "No"))
        self.radioButton31.setText(_translate("MainWindow", "Yes"))
        self.radioButton32.setText(_translate("MainWindow", "No"))
        self.radioButton33.setText(_translate("MainWindow", "Yes"))
        self.radioButton34.setText(_translate("MainWindow", "No"))
        self.radioButton35.setText(_translate("MainWindow", "Yes"))
        self.radioButton36.setText(_translate("MainWindow", "No"))
        self.radioButton37.setText(_translate("MainWindow", "Yes"))
        self.radioButton38.setText(_translate("MainWindow", "No"))
        self.radioButton39.setText(_translate("MainWindow", "Yes"))
        self.radioButton40.setText(_translate("MainWindow", "No"))
        self.radioButton41.setText(_translate("MainWindow", "Yes"))
        self.radioButton42.setText(_translate("MainWindow", "No"))
        self.radioButton43.setText(_translate("MainWindow", "Yes"))
        self.radioButton44.setText(_translate("MainWindow", "No"))
        self.radioButton49.setText(_translate("MainWindow", "Yes"))
        self.radioButton50.setText(_translate("MainWindow", "No"))
        self.radioButton51.setText(_translate("MainWindow", "Yes"))
        self.radioButton52.setText(_translate("MainWindow", "No"))
        self.radioButton53.setText(_translate("MainWindow", "Yes"))
        self.radioButton54.setText(_translate("MainWindow", "No"))
        self.radioButton55.setText(_translate("MainWindow", "Yes"))
        self.radioButton56.setText(_translate("MainWindow", "No"))
        self.radioButton57.setText(_translate("MainWindow", "Yes"))
        self.radioButton58.setText(_translate("MainWindow", "No"))
        self.radioButton59.setText(_translate("MainWindow", "Yes"))
        self.radioButton60.setText(_translate("MainWindow", "No"))
        self.radioButton61.setText(_translate("MainWindow", "Yes"))
        self.radioButton62.setText(_translate("MainWindow", "No"))
        self.radioButton63.setText(_translate("MainWindow", "Yes"))
        self.radioButton64.setText(_translate("MainWindow", "No"))
        self.radioButton65.setText(_translate("MainWindow", "Yes"))
        self.radioButton66.setText(_translate("MainWindow", "No"))
        self.radioButton67.setText(_translate("MainWindow", "Yes"))
        self.radioButton68.setText(_translate("MainWindow", "No"))
        self.radioButton69.setText(_translate("MainWindow", "Yes"))
        self.radioButton70.setText(_translate("MainWindow", "No"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        
    def Lift_Available_menu(self):
        global Lift_Available1
        if self.radioButton1.isChecked() == True:
            #print ("Yes")
            Lift_Available1="Yes"
        elif self.radioButton2.isChecked() == True:
            #print ("No")
            Lift_Available1="No"
        else:
            #print ("No")
            Lift_Available1="No"

	
    def Car_Parking_menu(self):
        global Car_Parking1
        if self.radioButton3.isChecked() == True:
            #print ("Yes")
            Car_Parking1="Yes"
        elif self.radioButton4.isChecked() == True:
            #print ("No")
            Car_Parking1="No"
        else:
            #print ("No")
            Car_Parking1="No"
        

    def Power_Backup_menu(self):
        global Power_Backup1
        if self.radioButton5.isChecked() == True:
            #print ("Yes")
            Power_Backup1="Yes"
        elif self.radioButton6.isChecked() == True:
            #print ("No")
            Power_Backup1="No"
        else:
            #print ("No")
            Power_Backup1="No"
        

    def Security_menu(self):
        global Security1
        if self.radioButton7.isChecked() == True:
            #print ("Yes")
            Security1="Yes"
        elif self.radioButton8.isChecked() == True:
            #print ("No")
            Security1="No"
        else:
            #print ("No")
            Security1="No"
        

    def Childrens_play_area_menu(self):
        global Childrens_play_area1
        if self.radioButton9.isChecked() == True:
            #print ("Yes")
            Childrens_play_area1="Yes"
        elif self.radioButton10.isChecked() == True:
            #print ("No")
            Childrens_play_area1="No"
        else:
            #print ("No")
            Childrens_play_area1="No"
        

    def Club_House_menu(self):
        global Club_House1
        if self.radioButton11.isChecked() == True:
            #print ("Yes")
            Club_House1="Yes"
        elif self.radioButton12.isChecked() == True:
            #print ("No")
            Club_House1="No"
        else:
            #print ("No")
            Club_House1="No"
        

    def Gymnasium_menu(self):
        global Gymnasium1
        if self.radioButton13.isChecked() == True:
            #print ("Yes")
            Gymnasium1="Yes"
        elif self.radioButton14.isChecked() == True:
            #print ("No")
            Gymnasium1="No"
        else:
            #print ("No")
            Gymnasium1="No"
        

    def Swimming_Pool_menu(self):
        global Swimming_Pool1
        if self.radioButton15.isChecked() == True:
            #print ("Yes")
            Swimming_Pool1="Yes"
        elif self.radioButton16.isChecked() == True:
            #print ("No")
            Swimming_Pool1="No"
        else:
            #print ("No")
            Swimming_Pool1="No"
        

    def Sports_Facility_menu(self):
        global Sports_Facility1
        if self.radioButton17.isChecked() == True:
            #print ("Yes")
            Sports_Facility1="Yes"
        elif self.radioButton18.isChecked() == True:
            #print ("No")
            Sports_Facility1="No"
        else:
            #print ("No")
            Sports_Facility1="No"
        

    def Indoor_Games_menu(self):
        global Indoor_Games1
        if self.radioButton19.isChecked() == True:
            #print ("Yes")
            Indoor_Games1="Yes"
        elif self.radioButton20.isChecked() == True:
            #print ("No")
            Indoor_Games1="No"
        else:
            #print ("No")
            Indoor_Games1="No"
        

    def Jogging_Track_menu(self):
        global Jogging_Track1
        if self.radioButton21.isChecked() == True:
            #print ("Yes")
            Jogging_Track1="Yes"
        elif self.radioButton22.isChecked() == True:
            #print ("No")
            Jogging_Track1="No"
        else:
            #print ("No")
            Jogging_Track1="No"
        

    def Maintenance_Staff_menu(self):
        global Maintenance_Staff1
        if self.radioButton23.isChecked() == True:
            #print ("Yes")
            Maintenance_Staff1="Yes"
        elif self.radioButton24.isChecked() == True:
            #print ("No")
            Maintenance_Staff1="No"
        else:
            #print ("No")
            Maintenance_Staff1="No"
        

    def Intercom_menu(self):
        global Intercom1
        if self.radioButton25.isChecked() == True:
            #print ("Yes")
            Intercom1="Yes"
        elif self.radioButton26.isChecked() == True:
            #print ("No")
            Intercom1="No"
        else:
            #print ("No")
            Intercom1="No"
        

    def Golf_Course_menu(self):
        global Golf_Course1
        if self.radioButton27.isChecked() == True:
            #print ("Yes")
            Golf_Course1="Yes"
        elif self.radioButton28.isChecked() == True:
            #print ("No")
            Golf_Course1="No"
        else:
            #print ("No")
            Golf_Course1="No"
        

    def Cafeteria_menu(self):
        global Cafeteria1
        if self.radioButton29.isChecked() == True:
            #print ("Yes")
            Cafeteria1="Yes"
        elif self.radioButton30.isChecked() == True:
            #print ("No")
            Cafeteria1="No"
        else:
            #print ("No")
            Cafeteria1="No"
        

    def Rain_Water_Harvesting_menu(self):
        global Rain_Water_Harvesting1
        if self.radioButton31.isChecked() == True:
            #print ("Yes")
            Rain_Water_Harvesting1="Yes"
        elif self.radioButton32.isChecked() == True:
            #print ("No")
            Rain_Water_Harvesting1="No"
        else:
            #print ("No")
            Rain_Water_Harvesting1="No"
        

    def Staff_Quarter_menu(self):
        global Staff_Quarter1
        if self.radioButton33.isChecked() == True:
            #print ("Yes")
            Staff_Quarter1="Yes"
        elif self.radioButton34.isChecked() == True:
            #print ("No")
            Staff_Quarter1="No"
        else:
            #print ("No")
            Staff_Quarter1="No"
        

    def Multipurpose_Room_menu(self):
        global Multipurpose_Room1
        if self.radioButton35.isChecked() == True:
            #print ("Yes")
            Multipurpose_Room1="Yes"
        elif self.radioButton36.isChecked() == True:
            #print ("No")
            Multipurpose_Room1="No"
        else:
            #print ("No")
            Multipurpose_Room1="No"
        

    def Landscaped_Gardens_menu(self):
        global Landscaped_Gardens1
        if self.radioButton37.isChecked() == True:
            #print ("Yes")
            Landscaped_Gardens1="Yes"
        elif self.radioButton38.isChecked() == True:
            #print ("No")
            Landscaped_Gardens1="No"
        else:
            #print ("No")
            Landscaped_Gardens1="No"
        

    def Shopping_Mall_menu(self):
        global Shopping_Mall1
        if self.radioButton39.isChecked() == True:
            #print ("Yes")
            Shopping_Mall1="Yes"
        elif self.radioButton40.isChecked() == True:
            #print ("No")
            Shopping_Mall1="No"
        else:
            #print ("No")
            Shopping_Mall1="No"
        if self.radioButton63.isChecked() == True:
            #print ("Yes")
            Shopping_Mall1="Yes"
        elif self.radioButton64.isChecked() == True:
            #print ("No")
            Shopping_Mall1="No"
        else:
            #print ("No")
            Shopping_Mall1="No"
        

    def School_menu(self):
        global School1
        if self.radioButton65.isChecked() == True:
            #print ("Yes")
            School1="Yes"
        elif self.radioButton66.isChecked() == True:
            #print ("No")
            School1="No"
        else:
            #print ("No")
            School1="No"
        

    def Hospital_menu(self):
        global Hospital1
        if self.radioButton67.isChecked() == True:
            #print ("Yes")
            Hospital1="Yes"
        elif self.radioButton68.isChecked() == True:
            #print ("No")
            Hospital1="No"
        else:
            #print ("No")
            Hospital1="No"
        

    def ATM_menu(self):
        global ATM1
        if self.radioButton69.isChecked() == True:
            #print ("Yes")
            ATM1="Yes"
        elif self.radioButton70.isChecked() == True:
            #print ("No")
            ATM1="No"
        else:
            #print ("No")
            ATM1="No"
        

    def AC_menu(self):
        global AC1
        if self.radioButton51.isChecked() == True:
            #print ("Yes")
            AC1="Yes"
        elif self.radioButton52.isChecked() == True:
            #print ("No")
            AC1="No"
        else:
            #print ("No")
            AC1="No"
        
    def Wardrobe_menu(self):
        global Wardrobe1
        if self.radioButton43.isChecked() == True:
            #print ("Yes")
            Wardrobe1="Yes"
        elif self.radioButton44.isChecked() == True:
            #print ("No")
            Wardrobe1="No"
        else:
            #print ("No")
            Wardrobe1="No"
            

    def TV_menu(self):
        global TV1
        if self.radioButton53.isChecked() == True:
            #print ("Yes")
            TV1="Yes"
        elif self.radioButton54.isChecked() == True:
            #print ("No")
            TV1="No"
        else:
            #print ("No")
            TV1="No"
           

    def Refrigerator_menu(self):
        global Refrigerator1
        if self.radioButton47.isChecked() == True:
            #print ("Yes")
            Refrigerator1="Yes"
        elif self.radioButton48.isChecked() == True:
            #print ("No")
            Refrigerator1="No"
        else:
            #print ("No")
            Refrigerator1="No"
        

    def Sofa_menu(self):
        global Sofa1
        if self.radioButton49.isChecked() == True:
            #print ("Yes")
            Sofa1="Yes"
        elif self.radioButton50.isChecked() == True:
            #print ("No")
            Sofa1="No"
        else:
            #print ("No")
            Sofa1="No"
        

    def Washing_Machine_menu(self):
        global Washing_Machine1
        if self.radioButton41.isChecked() == True:
            #print ("Yes")
            Washing_Machine1="Yes"
        elif self.radioButton42.isChecked() == True:
            #print ("No")
            Washing_Machine1="No"
        else:
            #print ("No")
            Washing_Machine1="No"
        

    def Wifi_menu(self):
        global wifi1
        if self.radioButton55.isChecked() == True:
            #print ("Yes")
            wifi1="Yes"
        elif self.radioButton56.isChecked() == True:
            #print ("No")
            wifi1="No"
        else:
            #print ("No")
            wifi1="No"
        

    def Microwave_menu(self):
        global Microwave1
        if self.radioButton57.isChecked() == True:
            #print ("Yes")
            Microwave1="Yes"
        elif self.radioButton58.isChecked() == True:
            #print ("No")
            Microwave1="No"
        else:
            #print ("No")
            Microwave1="No"
        

    def Dining_Table_menu(self):
        global Dining_Table1
        if self.radioButton59.isChecked() == True:
            #print ("Yes")
            Dining_Table1="Yes"
        elif self.radioButton60.isChecked() == True:
            #print ("No")
            Dining_Table1="No"
        else:
            #print ("No")
            Dining_Table1="No"
        
        
    def Gas_connection_menu(self):
        global Gas_connection1
        if self.radioButton45.isChecked() == True:
            #print ("Yes")
            Gas_connection1="Yes"
        elif self.radioButton46.isChecked() == True:
            #print ("No")
            Gas_connection1="No"
        else:
            #print ("No")
            Gas_connection1="No"
        
    
    def BED_menu(self):
        global BED1
        if self.radioButton61.isChecked() == True:
            #print ("Yes")
            BED1="Yes"
        elif self.radioButton62.isChecked() == True:
            #print ("No")
            BED1="No"
        else:
            #print ("No")
            BED1="No"
        

    def predict_page(self):	
        print("opening output page")
        MainWindow.hide()
        global Lift_Available1, Car_Parking1, Power_Backup1, Security1, Childrens_play_area1, Club_House1, Gymnasium1, Swimming_Pool1, Sports_Facility1, Indoor_Games1
        global Golf_Course1, Cafeteria1, Rain_Water_Harvesting1, Staff_Quarter1, Multipurpose_Room1 , Intercom1, Landscaped_Gardens1, Shopping_Mall1, School1, Hospital1
        global ATM1,  AC1, Wardrobe1, TV1, Refrigerator1, Sofa1, Washing_Machine1, wifi1, Microwave1, Dining_Table1, Gas_connection1, BED1, ATM1
        '''print(Lift_Available1)
        print(Car_Parking1)
        print(Power_Backup1)
        print(Security1)
        print(Childrens_play_area1)
        print(Club_House1)
        print(Gymnasium1)
        print(Swimming_Pool1)
        print(Sports_Facility1)
        print(Indoor_Games1)
        print(Jogging_Track1)
        print(Maintenance_Staff1)
        print(Intercom1)
        print(Golf_Course1)
        print(Cafeteria1)
        print(Rain_Water_Harvesting1)
        print(Staff_Quarter1)
        print(Multipurpose_Room1)
        print(Landscaped_Gardens1)
        print(Shopping_Mall1)
        print(School1)
        print(Hospital1)
        print(AC1)
        print(Wardrobe1)
        print(TV1)
        print(Refrigerator1)
        print(Sofa1)
        print(Washing_Machine1)
        print(wifi1)
        print(Microwave1)
        print(Dining_Table1)
        print(Gas_connection1)
        print(BED1)'''
        global output
        output = {"Lift_Available1":str(Lift_Available1),"Car_Parking1":str(Car_Parking1),\
        "Power_Backup1":str(Power_Backup1),"Security1":str(Security1),\
        "Childrens_play_area1":str(Childrens_play_area1),"Club_House1":str(Club_House1),\
        "Gymnasium1":str(Gymnasium1),"Swimming_Pool1":str(Swimming_Pool1),"Sports_Facility1":str(Sports_Facility1),\
        "Indoor_Games1":str(Indoor_Games1),"Jogging_Track1":str(Jogging_Track1),"Maintenance_Staff1":str(Maintenance_Staff1),\
        "Intercom1":str(Intercom1),"Golf_Course1":str(Golf_Course1),"Cafeteria1":str(Cafeteria1),\
        "Rain_Water_Harvesting1":str(Rain_Water_Harvesting1),"Staff_Quarter1":str(Staff_Quarter1),\
        "Multipurpose_Room1":str(Multipurpose_Room1),"Landscaped_Gardens1":str(Landscaped_Gardens1),\
        "Shopping_Mall1":str(Shopping_Mall1),"Washing_Machine1":str(Washing_Machine1),\
        "Wardrobe1":str(Wardrobe1),"Gas_connection1":str(Gas_connection1),"Refrigerator1":str(Refrigerator1),\
        "Sofa1":str(Sofa1),"AC1":str(AC1),"TV1":str(TV1),"wifi1":str(wifi1),"Microwave1":str(Microwave1),\
        "Dining_Table1":str(Dining_Table1),"BED1":str(BED1),"Shopping_Mall1":str(Shopping_Mall1),\
        "School1":str(School1),"Hospital1":str(Hospital1),"ATM1":str(ATM1)}
        with open('data4.json', 'w+') as outfile:
            json.dump(output, outfile)
        

        print(output)
        os.system("python3 output_page.py")
        sys.exit()

    def close_application(self):
        #choice = QtGui.QMessageBox.question(self, 'Warning!!', "Do You Really Want To Close this App ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)		
        #if choice == QtGui.QMessageBox.Yes:
        print ("Babye!!!!")
        sys.exit()
        #else:
        #pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

