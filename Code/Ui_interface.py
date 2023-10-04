# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Guojunrong\学习资料\人工智能\深度学习\深度学习实践\第一次大作业\PDF2Bib\GUI\interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenPDFFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenPDFFile.setGeometry(QtCore.QRect(80, 170, 180, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.OpenPDFFile.setFont(font)
        self.OpenPDFFile.setStyleSheet("background-color: rgba(255, 255, 255, .7)")
        self.OpenPDFFile.setObjectName("OpenPDFFile")
        self.Profile = QtWidgets.QTextBrowser(self.centralwidget)
        self.Profile.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.Profile.setStyleSheet("background-color: rgba(255, 255, 255, .7)")
        self.Profile.setObjectName("Profile")
        self.OutPrint = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutPrint.setGeometry(QtCore.QRect(0, 300, 800, 300))
        self.OutPrint.setStyleSheet("background-color: rgba(255, 255, 255, .7)")
        self.OutPrint.setObjectName("OutPrint")
        self.DownloadBIB = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadBIB.setGeometry(QtCore.QRect(540, 170, 180, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DownloadBIB.setFont(font)
        self.DownloadBIB.setStyleSheet("background-color: rgba(255, 255, 255, .7)")
        self.DownloadBIB.setObjectName("DownloadBIB")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.listView.setStyleSheet("background-image:url(:/background.jpg)url(:/background.jpg)")
        self.listView.setObjectName("listView")
        self.Doing = QtWidgets.QTextBrowser(self.centralwidget)
        self.Doing.setGeometry(QtCore.QRect(0, 267, 800, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Doing.setFont(font)
        self.Doing.setStyleSheet("background-color: rgba(255, 255, 255, .7)")
        self.Doing.setObjectName("Doing")
        self.listView.raise_()
        self.OpenPDFFile.raise_()
        self.Profile.raise_()
        self.OutPrint.raise_()
        self.DownloadBIB.raise_()
        self.Doing.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenPDFFile.setText(_translate("MainWindow", "Select PDF"))
        self.Profile.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    Enter a PDF file of a computer/electronic article (e.g., a CVPR article, only one type of article is sufficient).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">parse out all references, display them, and download all of their BIB file</span></p></body></html>"))
        self.DownloadBIB.setText(_translate("MainWindow", "Download BIB"))
import background_rc
