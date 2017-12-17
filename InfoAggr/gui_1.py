# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from manager import UpdateData, ReportMaker


class Ui_MainWindow(object):
    def __init__(self, report_path):
        super(Ui_MainWindow, self).__init__()
        self.update = UpdateData
        self.report = ReportMaker
        self.source = []
        self.model = []
        self.path = report_path

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("us.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(20, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(300, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(450, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 380, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 490, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 10, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(50, 400, 101, 41))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 11, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(170, 400, 71, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(250, 400, 110, 41))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 11, 7), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.onclick_report)
        self.pushButton_2.clicked.connect(self.onclick_download)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Info Aggr"))
        self.label.setText(_translate("MainWindow", "选择信息来源"))
        self.checkBox.setText(_translate("MainWindow", "汽车之家"))
        self.checkBox_2.setText(_translate("MainWindow", "搜狐汽车"))
        self.checkBox_3.setText(_translate("MainWindow", "腾讯汽车"))
        self.checkBox_4.setText(_translate("MainWindow", "新浪汽车"))
        self.label_3.setText(_translate("MainWindow", "选择模式"))
        self.checkBox_5.setText(_translate("MainWindow", "关键词统计"))
        self.pushButton.setText(_translate("MainWindow", "分析报告"))
        self.label_2.setText(_translate("MainWindow", "准备就绪......"))
        self.pushButton_2.setText(_translate("MainWindow", "更新数据"))
        self.label_4.setText(_translate("MainWindow", "等待下载......"))
        self.label_5.setText(_translate("MainWindow", "选择日期范围"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-M-d"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy-M-d"))

    def onclick_download(self):

        if self.checkBox.isChecked():
            self.source.append('autohome')
        if self.checkBox_2.isChecked():
            self.source.append('sohu')
        if self.checkBox_3.isChecked():
            self.source.append('tencent')
        if self.checkBox_4.isChecked():
            self.source.append('sina')

        _translate = QtCore.QCoreApplication.translate

        self.label_2.setText(_translate("MainWindow", "等待下载......\n正在下载数据......"))
        self.label_2.update()
        self.update(self.source)
        self.label_2.setText(_translate("MainWindow", "准备就绪......\n正在下载数据......\n更新完成......"))
        self.label_2.update()

    def onclick_report(self):
        start_date=str(self.dateEdit.date().toString('yyyy-MM-dd'))
        end_daet=str(self.dateEdit_2.date().toString('yyyy-MM-dd'))



        _translate = QtCore.QCoreApplication.translate

        self.label_4.setText(_translate("MainWindow", "就绪......\n分析......\n分析完成......"))
        self.report(start_date,end_daet)
