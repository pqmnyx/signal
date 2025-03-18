# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1403, 634)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_file = QPushButton(self.centralwidget)
        self.pushButton_file.setObjectName(u"pushButton_file")
        self.pushButton_file.setGeometry(QRect(30, 10, 211, 51))
        self.label_a = QLabel(self.centralwidget)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setGeometry(QRect(30, 100, 49, 16))
        self.label_b = QLabel(self.centralwidget)
        self.label_b.setObjectName(u"label_b")
        self.label_b.setGeometry(QRect(30, 140, 49, 16))
        self.lineEdit_a = QLineEdit(self.centralwidget)
        self.lineEdit_a.setObjectName(u"lineEdit_a")
        self.lineEdit_a.setGeometry(QRect(140, 100, 113, 21))
        self.lineEdit_b = QLineEdit(self.centralwidget)
        self.lineEdit_b.setObjectName(u"lineEdit_b")
        self.lineEdit_b.setGeometry(QRect(140, 140, 113, 21))
        self.pushButton_filter = QPushButton(self.centralwidget)
        self.pushButton_filter.setObjectName(u"pushButton_filter")
        self.pushButton_filter.setGeometry(QRect(30, 220, 101, 41))
        self.label_input = QLabel(self.centralwidget)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setGeometry(QRect(20, 490, 121, 16))
        self.label_input_spectrum = QLabel(self.centralwidget)
        self.label_input_spectrum.setObjectName(u"label_input_spectrum")
        self.label_input_spectrum.setGeometry(QRect(300, 490, 231, 16))
        self.label_output = QLabel(self.centralwidget)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setGeometry(QRect(580, 490, 211, 16))
        self.label_output_spectrum = QLabel(self.centralwidget)
        self.label_output_spectrum.setObjectName(u"label_output_spectrum")
        self.label_output_spectrum.setGeometry(QRect(860, 490, 201, 16))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 280, 271, 201))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(300, 280, 271, 201))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(580, 280, 271, 201))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(860, 280, 271, 201))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1403, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_file.setText(QCoreApplication.translate("MainWindow", u"Open signal file", None))
        self.label_a.setText(QCoreApplication.translate("MainWindow", u"a(i)", None))
        self.label_b.setText(QCoreApplication.translate("MainWindow", u"b(i)", None))
        self.pushButton_filter.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 ", None))
        self.label_input.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.label_input_spectrum.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0427\u0425 \u0432\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.label_output.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.label_output_spectrum.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0427\u0425 \u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
    # retranslateUi

