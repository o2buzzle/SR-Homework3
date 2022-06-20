# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerSwvpdu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from PyQt5.QtCore import pyqtSignal, QObject

from multiprocessing import Process, Queue
import GUI.sr_main


class Ui_MainWindow(object):
    service_process = None
    stdout_queue = Queue()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 781, 561))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QPushButton(self.verticalLayoutWidget)
        self.startButton.setObjectName("startButton")

        self.horizontalLayout.addWidget(self.startButton)

        self.statusCheck = QCheckBox(self.verticalLayoutWidget)
        self.statusCheck.setObjectName("statusCheck")
        self.statusCheck.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.statusCheck, 0, Qt.AlignHCenter)

        self.endButton = QPushButton(self.verticalLayoutWidget)
        self.endButton.setObjectName("endButton")

        self.horizontalLayout.addWidget(self.endButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.Console = QPlainTextEdit(self.verticalLayoutWidget)
        self.Console.setObjectName("Console")
        self.Console.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.Console)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.startButton.clicked.connect(self.startButton_onclick)
        self.endButton.clicked.connect(self.quit_application)

        self.timer = QTimer(self.centralwidget)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.startButton.setText(
            QCoreApplication.translate("MainWindow", "Start", None)
        )
        self.statusCheck.setText(
            QCoreApplication.translate("MainWindow", "Status", None)
        )
        self.endButton.setText(QCoreApplication.translate("MainWindow", "End", None))

    # retranslateUi

    def startButton_onclick(self):
        if not self.statusCheck.isChecked():
            self.startButton.setText("Stop")
            self.statusCheck.setChecked(True)
            self.start_service()

        else:
            self.startButton.setText("Start")
            self.statusCheck.setChecked(False)
            self.stop_service()

    def start_service(self):
        self.service_process = Process(
            target=GUI.sr_main.main, args=(self.stdout_queue,)
        )
        self.service_process.start()
        pass

    def stop_service(self):
        self.service_process.terminate()
        pass

    def update_status(self):
        if self.service_process:
            if not self.service_process.is_alive() and self.statusCheck.isChecked():
                # Restart the service
                self.stop_service()
                self.start_service()

        if not self.stdout_queue.empty():
            self.Console.appendPlainText(self.stdout_queue.get())

    def quit_application(self):
        sys.exit()
