import sys
import os
import Second_page_rc
import json


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 842)
        MainWindow.setStyleSheet("background-image: url(:/Bc/2.jpg);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 181, 41))
        self.textBrowser.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 41, 17))
        self.label.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label.setObjectName("label")
        
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(150, 110, 191, 27))
        self.lineEdit1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.textChanged.connect(self.Area_text)
        regex1 = QtCore.QRegExp("[1-9-0]+")
        validator1 = QtGui.QRegExpValidator(regex1)
        self.lineEdit1.setValidator(validator1)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 110, 68, 17))
        self.label_2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 17))
        self.label_3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_3.setObjectName("label_3")
        
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(150, 150, 281, 27))
        self.comboBox1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItems(['',' Residential Plot ', '0 BHK Villa ', '1 BHK Apartment ', '1 BHK Independent Floor ', '1 BHK Independent House ', '1 BHK Villa ', '1 BHK studio apartment ', '1 RK Apartment ', '1 RK Independent Floor ', '1 RK Independent House ', '2 BHK Apartment ', '2 BHK Independent Floor ', '2 BHK Independent House ', '2 BHK Villa ', '2 BHK penthouse ', '3 BHK Apartment ', '3 BHK Independent Floor ', '3 BHK Independent House ', '3 BHK Other Residential ', '3 BHK Villa ', '3 BHK penthouse ', '4 BHK Apartment ', '4 BHK Independent Floor ', '4 BHK Independent House ', '4 BHK Other Residential ', '4 BHK Villa ', '4 BHK penthouse ', '5 BHK Apartment ', '5 BHK Independent Floor ', '5 BHK Independent House ', '5 BHK Villa ', '5 BHK penthouse ', '6 BHK Apartment ', '6 BHK Independent Floor ', '6 BHK Villa ', '6 BHK penthouse ', '7 BHK Apartment ', '7 BHK Independent House ', '8 BHK Villa '])
        self.comboBox1.setItemText(0, "")
        self.comboBox1.currentIndexChanged.connect(self.bhk)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 91, 17))
        self.label_4.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_4.setObjectName("label_4")
        
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(150, 190, 191, 27))
        self.lineEdit2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.textChanged.connect(self.carpetarea_text)
        self.lineEdit2.setValidator(validator1)
        
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(150, 230, 191, 27))
        self.lineEdit3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit3.textChanged.connect(self.pricepersquare_text)
        self.lineEdit3.setValidator(validator1)
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 91, 17))
        self.label_7.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 270, 121, 17))
        self.label_8.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_8.setObjectName("label_8")
        
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(150, 270, 281, 27))
        self.comboBox2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItems(['','yes','no'])
        self.comboBox2.setItemText(0, "")
        self.comboBox2.currentIndexChanged.connect(self.Vaastu_Compliant_menu)
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 310, 81, 17))
        self.label_9.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_9.setObjectName("label_9")
        
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(150, 310, 281, 27))
        self.comboBox3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItems(['','yes','no'])
        self.comboBox3.setItemText(0, "")
        self.comboBox3.currentIndexChanged.connect(self.new_old)
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 350, 68, 17))
        self.label_10.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_10.setObjectName("label_10")
        
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(150, 350, 281, 27))
        self.comboBox4.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItems(['','Aditya Birla Hospital Marg', 'Airport Road', 'Ajmera colony', 'Akurdi', 'Alandi', 'Alandi Road', 'Amanora Park Town', 'Ambe Gaon', 'Ambedkar Nagar', 'Ambegaon Bk', 'Ambegaon Budruk', 'Ambegaon Khurd', 'Ambegaon Pathar', 'Ambegaon Road', 'Anand Nagar', 'Anand Park', 'Ashok Nagar', 'Askarwadi', 'Aundh', 'Aundh Annexe', 'Aundh Baner Link Road', 'Aundh Gaon', 'Aundh Road', 'BT Kawade Road', 'BT Kawde', 'Badhan Nagar', 'Baif Road', 'Bakhori', 'Bakori Road', 'Balaji Nagar', 'Balewadi', 'Balewadi High Street', 'Balewadi Road', 'Baner', 'Baner Balewadi road', 'Baner Gaon', 'Baner Highway Side Road', 'Baner Pashan Link Road', 'Baner Road', 'Baramati', 'Bavdhan', 'Bavdhan Khurd', 'Bebadohal', 'Benkar Nagar', 'Bhairav Nagar', 'Bhandarkar Road', 'Bharati Vidyapeeth', 'Bhatewara Nagar Chinchwad', 'Bhau Patil Road', 'Bhavani Peth', 'Bhawani Peth', 'Bhor', 'Bhosari', 'Bhosle Nagar', 'Bhoslenagar', 'Bhugaon', 'Bhujbal Vasti', 'Bhukum', 'Bhumkar Bridge', 'Bhumkar Nagar', 'Bhusari colony left', 'Bhusari colony right', 'Bibwewadi', 'Bibwewadi Kondhwa Road', 'Bijali Nagar PimpriChinchwad', 'Boat Club Road', 'Bopkhel', 'Bopodi', 'Bund Garden', 'Bund Garden Road', 'Burhani Colony Road', 'Camp', 'Chakan', 'Chakan Talegaon Road', 'Chandkhed', 'Charholi Budruk', 'Chikali Road', 'Chikhali', 'Chikhali Pimpri Chinchwad New Town Development Authority', 'Chikhali Road', 'Chincholi Dehu Road', 'Chinchwad', 'Chinchwad Gaon Road', 'Chinchwad Station Road', 'Chintamani nagar', 'DSK Road', 'DSK Vishwa Road', 'DY Patil Road', 'Dange Chowk Road', 'Dapodi', 'Dattanagar', 'Dattavadi', 'Daund', 'Deccan Gymkhana', 'Deep Bunglow chawk', 'Dehu', 'Dehu Road', 'Devachi Urli', 'Dhanakwadi', 'Dhankawadi Road', 'Dhanori', 'Dhanori Road', 'DhanoriLohegaon Road', 'Dhanukar Colony', 'Dhayari', 'Dhayari Ganesh Nagar', 'Dhayari Phata', 'Dhole Patil Road', 'Dighi', 'Dombewadi Road', 'EON Free Zone', 'Erandwane', 'Fatima Nagar', 'Fergusson College Road', 'Gadital', 'Gahunje', 'Gajanan Nagar', 'Ganesh Nagar', 'Ganeshkhind Road', 'Gera Emerald City Road', 'Ghodegaon', 'Ghole Road', 'Ghorpadi', 'Giridhar Nagar', 'Gokul Nagar', 'Gujarat Colony Road', 'Gulab Nagar Pune', 'Gultekdi', 'Guru Nanak Nagar', 'Guruwar Peth', 'Hadapsar', 'Hadapsar Fursungi Road', 'Hadapsar Gaon', 'Hadapsar Handewadi road', 'Hadapsar Saswad Jejuri Road', 'Hadapsar Tukai Nagar', 'Handewadi', 'Handewadi Road', 'Hanuman Nagar', 'Happy Colony Lane', 'Hinjawadi Phase 3', 'Hinjewadi', 'Hinjewadi Marunji Road', 'Hinjewadi Phase 1', 'Hinjewadi Phase 2', 'Hinjewadi Phase 2 Road', 'ITI road', 'Indira Nagar', 'Indrayani Nagar Sector 2', 'Ingawale Nagar', 'JM Road', 'Jambhul', 'Jambhulwadi', 'Jambhulwadi Road', 'Jejuri', 'Jejuri Saswad Hadapsar Road', 'Kad Nagar', 'Kalas', 'Kale Padal', 'Kalewadi', 'Kalewadi Main', 'Kalwad Area', 'Kalyani Nagar', 'Kalyani Nagar Annexe', 'Kambre Kd Deshmukhwadi Road', 'Kamgar Nagar PimpriChinchwad', 'Kamshet', 'Kanhe', 'Kanhephata', 'Karjat Kashele Khandas Road', 'Karve Nagar', 'Karve Road', 'Kasar Amboli', 'Kasarsai', 'Kasarwadi', 'Kaspate Vasti', 'Katarkhadak', 'Katraj', 'Kedagaon', 'Kedari Nagar', 'Kedgaon Station Road', 'Kendriya Vihar Road PimpriChinchwad', 'Keshav Nagar', 'Keshav Nagar Road', 'Khandala', 'Khandve Nagar', 'Kharabwadi', 'Kharadi', 'Khed Shivapur', 'Kirkatwadi', 'Kirti Nagar', 'Kiwale', 'Kolhewadi', 'Kolwadi', 'Kondhawe Dhawade', 'Kondhwa', 'Kondhwa Bk', 'Kondhwa Budruk', 'Kondhwa Khurd', 'Kondwa khurd road', 'Koregaon Bhima', 'Koregaon Park', 'Koregaon Park Annexe', 'Kothrud', 'Kothrud Bus Stand Road', 'Kothrud Depot Road', 'Krishnanagar Road', 'Kudale Baug', 'Kumar aangan society opposite shah hospital Yerwada Pune 411006', 'Kunal Icon Road', 'Kurkum MIDC', 'Lavasa', 'Law College Rd', 'Law collage Road', 'Laxman Nagar', 'Laxmi Nagar', 'Lohegaon', 'Lohegaon Road', 'Lokmanya Nagar', 'Lonavala Road', 'Loni', 'Loni Kalbhor', 'Loni Raiway Station Road', 'Lonikand', 'Lulla Nagar', 'MIT College Road', 'Madhav Nagar', 'Magarpatta', 'Magarpatta City', 'Magarpatta Road', 'Mahabaleshwar', 'Mahadev Nagar', 'Mahalunge', 'Mahatma Society', 'Malwadi', 'Malwadi Hadapsar', 'Mamurdi', 'Manchar', 'Mangal Nagar', 'Mangaldas Road', 'Mangaon', 'Mangdewadi', 'Manik Bagh', 'Manik Baug', 'Manjari', 'Manjari Budruk', 'Manjari Khurd', 'Manjri Village Road', 'Manohar Nagar', 'Market yard', 'Marunji', 'Marunji Road', 'Maval', 'Mayur Colony', 'Mayureshwar', 'Medankarwadi', 'Meeta Nagar', 'Model Colony', 'Mohamadwadi', 'Mohammed wadi', 'Mohan Nagar', 'Moraya Ganapati Mandir Road', 'Morewadi', 'Moshi', 'Moshi Pradhikaran PimpriChinchwad', 'Mukund Nagar', 'Mulshi', 'MulshiPaud Road', 'Mumbai Pune Highway', 'Mundhwa', 'Mundhwa Manjari Road', 'NDA Pashan Road', 'NIBM', 'NIBM Annex Mohammadwadi', 'NIBM Annexe', 'NIBM Junction', 'NIBM Post Office Road', 'NIBM Road', 'Nagpur Chal', 'Naigaon Peth Road', 'Nana Peth', 'Nanded', 'Nanded City Sinhgad Road', 'Nanded Phata', 'Nandel Fata Pune', 'Narhe', 'Narhe Gaon', 'Narhe Road', 'Nasrapur', 'National Highway 48', 'Navi Peth', 'Nehru Nagar', 'Nere', 'New DP Road', 'New Sangavi', 'New Sanghvi', 'Nigdi', 'Nigdi Sector 21', 'Nighoje', 'Nilanjali Society', 'Nilgiri Lane', 'Old Mumbai Pune Highway', 'Old Mumbai Road', 'Old Sanghvi', 'Omkar Colony Road', 'Padmavati', 'Pan Card Road', 'Pancard Club Road', 'Panchgani Wai Road', 'Panshet', 'Panshet Ghol Road', 'Papde Wasti', 'Parandwadi Road', 'Pargaon', 'Parihar Chowk', 'Parkhe Vasti', 'Parvati', 'Parvati Darshan', 'Parvati Gaon', 'Pashan', 'Pashan Sus Road', 'Pathare Vasti Road', 'Patwardhan Baug Road', 'Paud Rd', 'Perugate', 'Phaltan', 'Phase 3 Pune', 'Phursungi', 'Pimple Gurav', 'Pimple Nilakh', 'Pimple Nilakh Road', 'Pimple Saudagar', 'Pimpri', 'Pimpri Chinchwad', 'Pimpri Kalewadi Link Road', 'Pingale Wasti', 'Pirangut', 'Pisoli', 'Porwal Road', 'Prabhat Road', 'Pradhikaran Nigdi', 'Pragati Nagar', 'Pratik Nagar', 'Punawale', 'Pune Bengaluru Highway', 'Pune Link Road', 'Pune Mumbai Expressway', 'Pune Mumbai Highway', 'Pune Mumbai Road', 'Pune Nagar Road', 'Pune Pandharpur Road', 'Pune Satara Road', 'Pune Solapur Road', 'Pune Station', 'PuneSatara Road', 'PuneSolapur Highway', 'Purnanagar', 'Rahatani', 'Rahatani Rajgad Colony', 'Raigad District', 'Raikar Mala Road', 'Raje Shivaji Nagar PimpriChinchwad', 'Ram Nagar', 'Ranjangaon', 'Rasikwadi', 'Rasta Peth', 'Ravet', 'Rihe', 'SHIVAJI HSG SOC', 'Sadashiv Peth', 'Sahakar Nagar', 'Sahakar Nagar II', 'Sakore Nagar', 'Salisbury Park', 'Salunke Vihar', 'Samarth Colony', 'Sanaswadi', 'Sanewadi', 'Sangamvadi', 'Sanjay Park', 'Sant Nagar Lohegoan', 'Sasane Nagar', 'Saswad', 'Saswad Road', 'Satar Nagar', 'Satara road', 'Satavwadi', 'Sathe Wasti', 'Sector No1 Bhosari', 'Senapati Bapat Road', 'Shahunagar', 'Shankar Kalat Nagar', 'Shankar Sheth Road', 'Shankarseth Road', 'Shastri Nagar', 'Shedge Vasti PimpriChinchwad', 'Shewalewadi', 'Shikrapur', 'Shirur', 'Shirwal', 'Shiv Colony', 'Shivaji Nagar', 'Shivane', 'Shivapur', 'Sholapur Road', 'Shukrawar Peth', 'Siddharth nagar', 'Sinhagad Fort', 'Sinhgad Road', 'Somatane Phata', 'Someshwarwadi', 'Somwar Peth', 'Sopan Baug', 'Sukhsagar Nagar', 'Sun City', 'Sun City Road', 'Sunita Nagar', 'Sus', 'Sus Gaon', 'Sus Road', 'Swaraj Nagari', 'Swargate', 'Tadiwala Road', 'Talegaon', 'Talegaon Dabhade', 'Talegaon Dhamdhere', 'Talwade', 'Tanaji Nagar', 'Tathawade', 'Thergaon', 'Theur', 'Thite Nagar', 'Tingre Nagar', 'Trimurti Vihar', 'Tukai Darshan', 'Tukaram Nagar', 'Tulaja Bhawani Nagar', 'Tungarli', 'Ubale Nagar', 'Uday Baug', 'Undri', 'Undri Hadapsar Road', 'Upper Indira Nagar', 'Urbangram Kirkatwadi Road', 'Uruli Devachi', 'Uruli Kanchan', 'VIT College Road', 'Vadgaon Budruk', 'Vadgaon Maval', 'Vadgaon Sheri', 'Varale', 'Varanasi Society Internal Road', 'Vastu Udyog Road', 'Veerbhadra Nagar', 'Vighnaharta Nagar', 'Vijay Nagar', 'Viman Nagar', 'Vishal Nagar', 'Vishrantwadi', 'Wadagaon Road', 'Wadgaon Budruk', 'Wadgaon Sheri', 'Wadgaon Shinde Road', 'Wadki', 'Wagholi', 'Wakad', 'Wakad Chowk Road', 'Wakad Hinjewadi Road', 'Wakad road', 'Wakadkar Wasti', 'Walha Railway StationSukalwadi Road', 'Walvekar Nagar', 'Wanowrie', 'Wanwadi', 'Warje', 'Warje Malwadi', 'Yashwant nagar', 'Yavat', 'Yerawada', 'Yewalewadi', 'bavdhan patil nagar', 'bhekarai nagar', 'bhusari colony', 'bibvewadi', 'charholi Khurd', 'hingne Khurd', 'hinjawadi', 'karvenagar', 'katraj kondhwa road', 'kesnand', 'khamboli', 'khese park', 'konark avenue 9', 'north hadapsar', 'panchwati', 'paud', 'pimprigaon', 'pune saswad road', 'shahu nagar', 'sinhagad road', 'wadebolhai', 'wanwari'])
        self.comboBox4.setItemText(0, "")
        self.comboBox4.currentIndexChanged.connect(self.locality_menu)
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 400, 68, 17))
        self.label_11.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_11.setObjectName("label_11")
        
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(150, 390, 281, 27))
        self.lineEdit4.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.lineEdit4.setText("")
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit4.textChanged.connect(self.floor_text)
        self.lineEdit4.setValidator(validator1)
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 440, 131, 17))
        self.label_12.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_12.setObjectName("label_12")
        
        self.comboBox5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox5.setGeometry(QtCore.QRect(150, 430, 281, 27))
        self.comboBox5.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox5.setObjectName("comboBox5")
        self.comboBox5.addItems(['','1 rooms( pooja room )', '1 rooms( servant room )', '1 rooms( study room )', '2 rooms( servant room, pooja room )', '2 rooms( study room, pooja room )', '2 rooms( study room, servant room )', '3 rooms( study room, servant room, pooja room )'])
        self.comboBox5.setItemText(0, "")
        self.comboBox5.currentIndexChanged.connect(self.additionalrooms_menu)
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 480, 121, 17))
        self.label_13.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_13.setObjectName("label_13")
        
        self.comboBox6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox6.setGeometry(QtCore.QRect(150, 470, 281, 27))
        self.comboBox6.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox6.setObjectName("comboBox6")
        self.comboBox6.addItems(['','Apr 2018', 'Apr 2019', 'Aug 2018', 'Aug 2019', 'Aug 2020', 'Aug 2021', 'Dec 2018', 'Dec 2019', 'Dec 2020', 'Dec 2021', 'Dec 2022', 'Dec 2023', 'Dec 2025', 'Feb 2018', 'Feb 2019', 'Feb 2020', 'Feb 2021', 'Feb 2022', 'Jan 2018', 'Jan 2019', 'Jan 2020', 'Jul 2018', 'Jul 2019', 'Jul 2020', 'Jul 2021', 'Jun 2018', 'Jun 2019', 'Jun 2020', 'Jun 2021', 'Mar 2018', 'Mar 2019', 'Mar 2020', 'Mar 2021', 'Mar 2022', 'May 2018', 'May 2019', 'May 2020', 'May 2021', 'Nov 2018', 'Nov 2019', 'Nov 2020', 'Nov 2021', 'Oct 2018', 'Oct 2019', 'Oct 2021', 'Oct 2022', 'Sep 2018', 'Sep 2019', 'Sep 2020', 'Sep 2021', 'Sep 2022'])
        self.comboBox6.setItemText(0, "")
        self.comboBox6.currentIndexChanged.connect(self.month_menu)
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 520, 61, 17))
        self.label_14.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_14.setObjectName("label_14")
        
        self.comboBox7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox7.setGeometry(QtCore.QRect(150, 510, 281, 27))
        self.comboBox7.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox7.setObjectName("comboBox7")
        self.comboBox7.addItems(['','Furnished', 'Ready to move', 'Ready to move,Furnished', 'Ready to move,Semi-Furnished', 'Ready to move,Unfurnished', 'Semi-Furnished', 'Under Construction', 'Under Construction,Furnished', 'Under Construction,Semi-Furnished', 'Under Construction,Unfurnished', 'Unfurnished'])
        self.comboBox7.setItemText(0, "")
        self.comboBox7.currentIndexChanged.connect(self.status_menu)
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 560, 111, 17))
        self.label_15.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_15.setObjectName("label_15")
        
        self.comboBox8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox8.setGeometry(QtCore.QRect(150, 550, 281, 27))
        self.comboBox8.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.comboBox8.setObjectName("comboBox8")
        self.comboBox8.addItems(['','East', 'North', 'NorthEast', 'NorthWest', 'South', 'SouthEast', 'SouthWest', 'West'])
        self.comboBox8.setItemText(0, "")
        self.comboBox8.currentIndexChanged.connect(self.facing)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(20, 610, 111, 41))
        self.pushButton1.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.next_page)
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(180, 610, 101, 41))
        self.pushButton2.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.predict_page)
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(320, 610, 101, 41))
        self.pushButton3.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.clicked.connect(self.close_application)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 190, 68, 17))
        self.label_5.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 230, 68, 17))
        self.label_6.setStyleSheet("background-image: url(:/Bc/3.jpg);")
        self.label_6.setObjectName("label_6")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 25))
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
        self.label.setText(_translate("MainWindow", "Area :"))
        self.label_2.setText(_translate("MainWindow", "in sq.ft"))
        self.label_3.setText(_translate("MainWindow", "No of BHK:"))
        self.label_4.setText(_translate("MainWindow", "Carpet Area:"))
        self.label_7.setText(_translate("MainWindow", "Price / Sq.ft"))
        self.label_8.setText(_translate("MainWindow", "Vastu Compliant:"))
        self.label_9.setText(_translate("MainWindow", "New / Old:"))
        self.label_10.setText(_translate("MainWindow", "Locality :"))
        self.label_11.setText(_translate("MainWindow", "Floor No:"))
        self.label_12.setText(_translate("MainWindow", "Additional Rooms:"))
        self.label_13.setText(_translate("MainWindow", "Possession Date:"))
        self.label_14.setText(_translate("MainWindow", "Status :"))
        self.label_15.setText(_translate("MainWindow", "Facing Towards:"))
        self.pushButton1.setText(_translate("MainWindow", "Next"))
        self.pushButton2.setText(_translate("MainWindow", "Predict"))
        self.pushButton3.setText(_translate("MainWindow", "Exit"))
        self.label_5.setText(_translate("MainWindow", "in sq.ft"))
        self.label_6.setText(_translate("MainWindow", "in sq.ft"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        
    def Area_text(self):
        global area1
        area1 = self.lineEdit1.text()

    def bhk(self):
        global bhk1
        bhk1 = self.comboBox1.currentText()

    def facing(self):
        global facing1
        facing1 = self.comboBox8.currentText()

    def carpetarea_text(self):
        global carpetarea1
        carpetarea1 = self.lineEdit2.text()

    def pricepersquare_text(self):
        global pricepersquare1
        pricepersquare1 = self.lineEdit3.text()

    def Vaastu_Compliant_menu(self):
        global Vaastu_Compliant1
        Vaastu_Compliant1 = self.comboBox2.currentText()

    def new_old(self):
        global neworold1
        neworold1 = self.comboBox3.currentText()

    def locality_menu(self):
        global locality1
        locality1 = self.comboBox4.currentText()

    def floor_text(self):
        global floor1
        floor1 = self.lineEdit4.text()

    def month_menu(self):
        global possesiondate1
        possesiondate1 = self.comboBox6.currentText()


    def additionalrooms_menu(self):
        global additionalrooms1
        additionalrooms1 = self.comboBox5.currentText()

    def status_menu(self):
        global status1
        status1 = self.comboBox7.currentText()

    def next_page(self):	
        print("opening next page")
        MainWindow.hide()
        
        global area1,bhk1,facing1,carpetarea1,pricepersquare1,Vaastu_Compliant1,neworold1,locality1,floor1,additionalrooms1,possesiondate1,status1
        print(area1)
        print(bhk1)
        print(facing1)
        print(carpetarea1)
        print(pricepersquare1)
        print(Vaastu_Compliant1)
        print(neworold1)
        print(locality1)
        print(floor1)
        print(additionalrooms1)
        print(possesiondate1)
        print(status1)
        global output
        
        output = {"area1":str(area1),"bhk1":str(bhk1),"facing1":str(facing1),\
        "carpetarea1":str(carpetarea1),"pricepersquare1":str(pricepersquare1),\
        "Vaastu_Compliant1":str(Vaastu_Compliant1),"neworold1":str(neworold1),\
        "locality1":str(locality1),"floor1":str(floor1),"additionalrooms1":str(additionalrooms1),\
        "possesiondate1":str(possesiondate1),"status1":str(status1)}
        with open('data2.json', 'w+') as outfile:
            json.dump(output, outfile)
        print(output)

        os.system("python3 third_page.py")
        sys.exit()

    def predict_page(self):	
        
        print("opening output page")
        MainWindow.hide()
        
        output = [str(area1),str(bhk1),str(facing1),str(carpetarea1),str(pricepersquare1),str(Vaastu_Compliant1),str(neworold1),str(locality1),str(floor1),str(additionalrooms1),str(possesiondate1),str(status1)]
        with open('data2.json', 'w+') as outfile:
            json.dump(output, outfile)
        print(output)
        os.system("python3 output_page.py")
        #print("opening Encoding_df_pickel.py file..")
        #os.system("python Encoding_df_pickel.py")
        #print("closing Encoding_df_pickel.py file")
        sys.exit()

    def close_application(self):
        #choice = QtGui.QMessageBox.question(self, 'Warning!!', "Do You Really Want To Close this App ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)		
        #if choice == QtGui.QMessageBox.Yes:
        print ("Babye!!!!")
        sys.exit()
        #else:
        #    pass        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

