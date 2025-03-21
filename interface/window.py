# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 723)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_b = QLabel(self.groupBox_2)
        self.label_b.setObjectName(u"label_b")

        self.horizontalLayout_6.addWidget(self.label_b)

        self.lineEdit_b = QLineEdit(self.groupBox_2)
        self.lineEdit_b.setObjectName(u"lineEdit_b")

        self.horizontalLayout_6.addWidget(self.lineEdit_b)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_a = QLabel(self.groupBox_2)
        self.label_a.setObjectName(u"label_a")

        self.horizontalLayout_5.addWidget(self.label_a)

        self.lineEdit_a = QLineEdit(self.groupBox_2)
        self.lineEdit_a.setObjectName(u"lineEdit_a")

        self.horizontalLayout_5.addWidget(self.lineEdit_a)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.pushButton_file = QPushButton(self.groupBox_3)
        self.pushButton_file.setObjectName(u"pushButton_file")

        self.verticalLayout_2.addWidget(self.pushButton_file)

        self.pushButton_filter = QPushButton(self.groupBox_3)
        self.pushButton_filter.setObjectName(u"pushButton_filter")

        self.verticalLayout_2.addWidget(self.pushButton_filter)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 2044, 504))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_input = QLabel(self.scrollAreaWidgetContents_2)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setMinimumSize(QSize(500, 0))

        self.verticalLayout_3.addWidget(self.label_input)

        self.verticalLayout_3.setStretch(0, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_input_spectrum = QLabel(self.scrollAreaWidgetContents_2)
        self.label_input_spectrum.setObjectName(u"label_input_spectrum")
        self.label_input_spectrum.setMinimumSize(QSize(500, 0))

        self.verticalLayout_4.addWidget(self.label_input_spectrum)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.label_output = QLabel(self.scrollAreaWidgetContents_2)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setMinimumSize(QSize(500, 0))

        self.verticalLayout_5.addWidget(self.label_output)

        self.verticalLayout_5.setStretch(0, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.label_output_spectrum = QLabel(self.scrollAreaWidgetContents_2)
        self.label_output_spectrum.setObjectName(u"label_output_spectrum")
        self.label_output_spectrum.setMinimumSize(QSize(500, 0))

        self.verticalLayout_6.addWidget(self.label_output_spectrum)

        self.verticalLayout_6.setStretch(0, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0438\u0444\u0440\u043e\u0432\u044b\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_b.setText(QCoreApplication.translate("MainWindow", u"b(i)", None))
        self.lineEdit_b.setText(QCoreApplication.translate("MainWindow", u"0.1, 0.5", None))
        self.label_a.setText(QCoreApplication.translate("MainWindow", u"a(i)", None))
        self.lineEdit_a.setText(QCoreApplication.translate("MainWindow", u"0.3, 0.5, 0.9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0438 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_file.setText(QCoreApplication.translate("MainWindow", u"Open signal file", None))
        self.pushButton_filter.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_input.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.label_input_spectrum.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0427\u0425 \u0432\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.label_output.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.label_output_spectrum.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0427\u0425 \u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
    # retranslateUi

