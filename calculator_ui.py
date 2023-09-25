# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(335, 551)
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        font.setBold(True)
        Calculator.setFont(font)
        icon = QIcon()
        icon.addFile(u"../calculator-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Calculator.setWindowIcon(icon)
        Calculator.setLayoutDirection(Qt.LeftToRight)
        Calculator.setStyleSheet(u"background: #000000; border: 0;")
        Calculator.setIconSize(QSize(0, 0))
        Calculator.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Calculator.setAnimated(True)
        Calculator.setDocumentMode(False)
        Calculator.setTabShape(QTabWidget.Rounded)
        Calculator.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(10, 150, 75, 71))
        self.btnClear.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnDivide = QPushButton(self.centralwidget)
        self.btnDivide.setObjectName(u"btnDivide")
        self.btnDivide.setGeometry(QRect(90, 150, 75, 71))
        self.btnDivide.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnDivide.setIconSize(QSize(100, 100))
        self.btnMultiply = QPushButton(self.centralwidget)
        self.btnMultiply.setObjectName(u"btnMultiply")
        self.btnMultiply.setGeometry(QRect(170, 150, 75, 71))
        self.btnMultiply.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 150, 75, 71))
        self.pushButton_4.setStyleSheet(u"QPushButton {background: green;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6AB56A\n"
"}")
        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setGeometry(QRect(10, 230, 75, 71))
        self.btn7.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setGeometry(QRect(170, 230, 75, 71))
        self.btn9.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setGeometry(QRect(90, 230, 75, 71))
        self.btn8.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnMinus = QPushButton(self.centralwidget)
        self.btnMinus.setObjectName(u"btnMinus")
        self.btnMinus.setGeometry(QRect(250, 230, 75, 71))
        self.btnMinus.setStyleSheet(u"QPushButton {\n"
"background: green;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6AB56A\n"
"}")
        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setGeometry(QRect(10, 310, 75, 71))
        self.btn4.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setGeometry(QRect(90, 310, 75, 71))
        self.btn5.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setGeometry(QRect(170, 310, 75, 71))
        self.btn6.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnPlus = QPushButton(self.centralwidget)
        self.btnPlus.setObjectName(u"btnPlus")
        self.btnPlus.setGeometry(QRect(250, 310, 75, 71))
        self.btnPlus.setStyleSheet(u"QPushButton {\n"
"background: green;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6AB56A\n"
"}")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(10, 390, 75, 71))
        self.btn1.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(90, 390, 75, 71))
        self.btn2.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(170, 390, 75, 71))
        self.btn3.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnPercent = QPushButton(self.centralwidget)
        self.btnPercent.setObjectName(u"btnPercent")
        self.btnPercent.setGeometry(QRect(170, 470, 75, 71))
        self.btnPercent.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btn0 = QPushButton(self.centralwidget)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setGeometry(QRect(90, 470, 75, 71))
        self.btn0.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnComma = QPushButton(self.centralwidget)
        self.btnComma.setObjectName(u"btnComma")
        self.btnComma.setGeometry(QRect(10, 470, 75, 71))
        self.btnComma.setStyleSheet(u"QPushButton {background: #131313;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6F6F6F\n"
"}\n"
"")
        self.btnEqual = QPushButton(self.centralwidget)
        self.btnEqual.setObjectName(u"btnEqual")
        self.btnEqual.setGeometry(QRect(250, 390, 75, 151))
        self.btnEqual.setFocusPolicy(Qt.NoFocus)
        self.btnEqual.setContextMenuPolicy(Qt.PreventContextMenu)
        self.btnEqual.setAutoFillBackground(False)
        self.btnEqual.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
"border: 0;\n"
"color: white;\n"
"font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #6AB56A\n"
"}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 0, 311, 141))
        self.lineEdit.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit.setStyleSheet(u"color: white;\n"
"font-size: 50px")
        self.lineEdit.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.btnClear.setText(QCoreApplication.translate("Calculator", u"AC", None))
        self.btnDivide.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.btnMultiply.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.pushButton_4.setText(QCoreApplication.translate("Calculator", u"Delete", None))
        self.btn7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.btn9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.btn8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.btnMinus.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btn4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.btn5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.btn6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.btnPlus.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.btn1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.btn3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.btnPercent.setText(QCoreApplication.translate("Calculator", u"%", None))
        self.btn0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btnComma.setText(QCoreApplication.translate("Calculator", u",", None))
        self.btnEqual.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.lineEdit.setText("")
    # retranslateUi

