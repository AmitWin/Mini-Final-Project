# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='wamit112233',
    database='LoginSystem'
    )

mycursor = db.cursor()

#mycursor.execute('CREATE TABLE Users (ID int PRIMARY KEY NOT NULL AUTO_INCREMENT, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, birth_year int NOT NULL, email VARCHAR(50) NOT NULL)')

class Ui_MainWindow(QMainWindow):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.LogInPage.close()

    def openChess(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChessOptions()
        self.ui.setupUi(self.window)
        self.window.show()
        self.LogInPage.close()

    def setupUi(self, LogInPage):
        self.LogInPage = LogInPage
        LogInPage.setObjectName("LogInPage")
        LogInPage.setEnabled(True)
        LogInPage.resize(600, 400)
        LogInPage.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(LogInPage)
        self.centralwidget.setObjectName("centralwidget")
        self.UserName = QtWidgets.QLineEdit(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(150, 125, 300, 35))
        self.UserName.setStyleSheet("background-color:white;\n"
"color:grey;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"")
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(150, 170, 300, 35))
        self.Password.setStyleSheet("background-color:white;\n"
"color:grey;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"")
        self.Password.setObjectName("Password")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(200, 230, 200, 35))
        self.Submit.setStyleSheet("background-color:red;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"border-color:black;\n"
"")
        self.Submit.setObjectName("Submit")
        self.NewUser = QtWidgets.QPushButton(self.centralwidget)
        self.NewUser.setGeometry(QtCore.QRect(200, 270, 200, 35))
        self.NewUser.setStyleSheet("background-color:red;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"border-color:black;\n"
"")
        self.NewUser.setObjectName("NewUser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 141, 71))
        self.label.setStyleSheet("color:white;\n"
"font:bold 25px;\n"
"")
        self.label.setObjectName("label")
        self.Password.raise_()
        self.UserName.raise_()
        self.Submit.raise_()
        self.NewUser.raise_()
        self.label.raise_()
        LogInPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogInPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        LogInPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogInPage)
        self.statusbar.setObjectName("statusbar")
        LogInPage.setStatusBar(self.statusbar)
        self.Submit.clicked.connect(lambda x: self.log_in())
        self.NewUser.clicked.connect(lambda x: self.openWindow())
        self.retranslateUi(LogInPage)
        QtCore.QMetaObject.connectSlotsByName(LogInPage)

    def log_in(self):
        username = self.UserName.text()
        password = self.Password.text()
        if self.Is_User_Exists(username, password):
            self.openChess()

    def Is_User_Exists(self, user, passw):
        correct_info = 0
        mycursor.execute("SELECT username, password FROM Users")
        for (existUser, existPasssw) in mycursor:
            if existUser == user and existPasssw == passw:
                return True
        return False

    def retranslateUi(self, LogInPage):
        _translate = QtCore.QCoreApplication.translate
        LogInPage.setWindowTitle(_translate("LogInPage", "Log in Page"))
        self.UserName.setPlaceholderText(_translate("LogInPage", "Enter Username"))
        self.Password.setPlaceholderText(_translate("LogInPage", "Enter Password"))
        self.Submit.setText(_translate("LogInPage", "Submit"))
        self.NewUser.setText(_translate("LogInPage", "New User"))
        self.label.setText(_translate("LogInPage", "Login Page"))


class Ui_RegisterWindow(QMainWindow):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.Registration.close()

    def setupUi(self, Registration):
        self.Registration = Registration
        Registration.setObjectName("Registration")
        Registration.resize(600, 400)
        Registration.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")
        self.RegisterLabel = QtWidgets.QLabel(self.centralwidget)
        self.RegisterLabel.setGeometry(QtCore.QRect(215, 10, 170, 50))
        self.RegisterLabel.setStyleSheet("color:white;\n"
                                 "font:bold 35px;\n"
                                 "")
        self.RegisterLabel.setObjectName("RegisterLabel")
        self.FirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstName.setGeometry(QtCore.QRect(70, 80, 200, 40))
        self.FirstName.setStyleSheet("background-color:white;\n"
                                    "color:grey;\n"
                                    "border-style:outset;\n"
                                    "border-width:2px;\n"
                                    "border-radius:10px;\n"
                                    "border-color:white;\n"
                                    "font:bold 14px;")
        self.FirstName.setObjectName("FirstName")
        self.BirthYear = QtWidgets.QLineEdit(self.centralwidget)
        self.BirthYear.setGeometry(QtCore.QRect(70, 150, 200, 40))
        self.BirthYear.setStyleSheet("background-color:white;\n"
                                      "color:grey;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 14px;")
        self.BirthYear.setObjectName("BirthYear")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(70, 220, 200, 40))
        self.Username.setStyleSheet("background-color:white;\n"
                                      "color:grey;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 14px;")
        self.Username.setObjectName("Username")
        self.LastName = QtWidgets.QLineEdit(self.centralwidget)
        self.LastName.setGeometry(QtCore.QRect(340, 80, 200, 40))
        self.LastName.setStyleSheet("background-color:white;\n"
                                      "color:grey;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 14px;")
        self.LastName.setObjectName("LastName")
        self.EmailAdress = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailAdress.setGeometry(QtCore.QRect(340, 150, 200, 40))
        self.EmailAdress.setStyleSheet("background-color:white;\n"
                                      "color:grey;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 14px;")
        self.EmailAdress.setObjectName("EmailAdress")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(340, 220, 200, 40))
        self.Password.setStyleSheet("background-color:white;\n"
                                      "color:grey;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 14px;")
        self.Password.setObjectName("Password")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(200, 280, 200, 35))
        self.Register.setStyleSheet("background-color:red;\n"
                                   "color:white;\n"
                                   "border-style:outset;\n"
                                   "border-width:2px;\n"
                                   "border-radius:10px;\n"
                                   "border-color:white;\n"
                                   "font:bold 14px;\n"
                                   "border-color:black;\n"
                                   "")
        self.Register.setObjectName("Register")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(200, 330, 200, 35))
        self.Back.setStyleSheet("background-color:red;\n"
                                   "color:white;\n"
                                   "border-style:outset;\n"
                                   "border-width:2px;\n"
                                   "border-radius:10px;\n"
                                   "border-color:white;\n"
                                   "font:bold 14px;\n"
                                   "border-color:black;\n"
                                   "")
        self.Back.setObjectName("Back")
        Registration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Registration)
        self.statusbar.setObjectName("statusbar")
        Registration.setStatusBar(self.statusbar)
        self.retranslateUi(Registration)
        self.Back.clicked.connect(lambda x: self.openWindow())
        QtCore.QMetaObject.connectSlotsByName(Registration)
        self.Register.clicked.connect(lambda x: self.RegistrationToDB())

    def RegistrationToDB(self):
        exist = False
        firstName = self.FirstName.text()
        lastName = self.LastName.text()
        birthYear = self.BirthYear.text()
        email = self.EmailAdress.text()
        username = self.Username.text()
        password = self.Password.text()
        try:
            birthYear = int(birthYear)
        except:
            self.InvalidBirthYearPopUp()
            exist = True
        if not exist:
            mycursor.execute("SELECT username, password, first_name, last_name, birth_year, email FROM Users")
            for (exist_user, exist_passw, exist_first_name, exist_last_name, exist_birth_year, exist_email) in mycursor:
                if exist_user == username:
                    self.UsernameExistPopUp()
                    exist = True
                elif exist_email == email:
                    self.EmailExistPopUp()
                    exist = True
                elif exist_first_name == "" or exist_user == "" or exist_passw == "" or exist_last_name == "" or exist_email == "":
                    exist = True
        if not exist:
            mycursor.execute("INSERT INTO Users (username, password, first_name, last_name, birth_year, email) VALUES (%s,%s,%s,%s,%s,%s)", (username, password, firstName, lastName, birthYear, email))
            db.commit()
            self.openWindow()

    def UsernameExistPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Username Exists")
        msg.setText("This username is already exists.")

        x = msg.exec_()

    def EmailExistPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Email Exists")
        msg.setText("This email address is already exists.")

        x = msg.exec_()

    def InvalidBirthYearPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid Birth Year")
        msg.setText("The birth year is not valid.")

        x = msg.exec_()

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration Page"))
        self.RegisterLabel.setText(_translate("Registration", "Register"))
        self.FirstName.setPlaceholderText(_translate("Registration", "Enter your First Name"))
        self.BirthYear.setPlaceholderText(_translate("Registration", "Enter your Birth Year"))
        self.Username.setPlaceholderText(_translate("Registration", "Enter Username"))
        self.LastName.setPlaceholderText(_translate("Registration", "Enter your Last Name"))
        self.EmailAdress.setPlaceholderText(_translate("Registration", "Enter your Email Adress"))
        self.Password.setPlaceholderText(_translate("Registration", "Enter Password"))
        self.Back.setText(_translate("Registration", "Back"))
        self.Register.setText(_translate("Registration", "Register"))

class Ui_ChessOptions(object):
    def setupUi(self, ChessOptions):
        ChessOptions.setObjectName("ChessOptions")
        ChessOptions.resize(600, 400)
        ChessOptions.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(ChessOptions)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(207, 30, 185, 71))
        self.MainLabel.setStyleSheet("color:white;\n"
"font:bold 25px;\n"
"")
        self.MainLabel.setObjectName("MainLabel")
        self.PlayVSComputer = QtWidgets.QLabel(self.centralwidget)
        self.PlayVSComputer.setGeometry(QtCore.QRect(100, 120, 300, 50))
        self.PlayVSComputer.setStyleSheet("background-color:grey;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"border-color:black;")
        self.PlayVSComputer.setObjectName("PlayVSComputer")
        self.PlayVSFriend = QtWidgets.QLabel(self.centralwidget)
        self.PlayVSFriend.setGeometry(QtCore.QRect(100, 190, 300, 50))
        self.PlayVSFriend.setStyleSheet("background-color:grey;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"border-color:black;")
        self.PlayVSFriend.setObjectName("PlayVSFriend")
        self.PlayVSYourself = QtWidgets.QLabel(self.centralwidget)
        self.PlayVSYourself.setGeometry(QtCore.QRect(100, 260, 300, 50))
        self.PlayVSYourself.setStyleSheet("background-color:grey;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 14px;\n"
"border-color:black;")
        self.PlayVSYourself.setObjectName("PlayVSYourself")
        ChessOptions.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChessOptions)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        ChessOptions.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChessOptions)
        self.statusbar.setObjectName("statusbar")
        ChessOptions.setStatusBar(self.statusbar)
        self.retranslateUi(ChessOptions)
        QtCore.QMetaObject.connectSlotsByName(ChessOptions)
        

    def retranslateUi(self, ChessOptions):
        _translate = QtCore.QCoreApplication.translate
        ChessOptions.setWindowTitle(_translate("ChessOptions", "Chess Options"))
        self.MainLabel.setText(_translate("ChessOptions", "Chess Options"))
        self.PlayVSComputer.setText(_translate("ChessOptions", "Play VS. computer"))
        self.PlayVSFriend.setText(_translate("ChessOptions", "Play VS. a friend"))
        self.PlayVSYourself.setText(_translate("ChessOptions", "Play VS. yourself"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    mycursor.execute("SELECT * FROM Users")
    for x in mycursor:
        print(x)
    MainWindow.show()
    sys.exit(app.exec_())
