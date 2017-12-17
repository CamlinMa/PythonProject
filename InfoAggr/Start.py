# -*- coding:utf-8 -*

import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui_1 import Ui_MainWindow

if __name__=='__main__':
    work_dir = (str(os.getcwd()).replace('\\', '/') + '/').replace('InfoAggr/download/', 'InfoAggr/')


    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow(work_dir)
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())