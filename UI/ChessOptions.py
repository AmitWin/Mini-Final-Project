# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChessOptions.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
    ChessOptions = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(ChessOptions)
    ChessOptions.show()
    sys.exit(app.exec_())
