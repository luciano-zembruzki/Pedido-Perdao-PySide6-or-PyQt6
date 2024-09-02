# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetElJZQG.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(632, 520)
        Form.setStyleSheet(u"QWidget#Form{\n"
"	background-color: rgb(27, 26, 53);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#yes{\n"
"	background-color: rgb(50, 50, 88);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#no{\n"
"	background-color: rgb(50, 50, 88);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding-left: 40px;\n"
"	padding-right: 40px;\n"
"	padding-top: 15px;\n"
"	padding-bottom: 15px;\n"
"	border-radius: 5px;\n"
"	font: bold;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pic = QLabel(self.frame)
        self.pic.setObjectName(u"pic")
        self.pic.setPixmap(QPixmap(u"../../../../Downloads/ab67616d00001e026520c3ea51876f6e29db3f60 Background Removed.png"))
        self.pic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.pic)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hsl = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hsl)

        self.yes = QPushButton(self.frame_2)
        self.yes.setObjectName(u"yes")

        self.horizontalLayout.addWidget(self.yes)

        self.no = QPushButton(self.frame_2)
        self.no.setObjectName(u"no")

        self.horizontalLayout.addWidget(self.no)

        self.hsr = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hsr)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Me Perdoe?", None))
        self.label.setText(QCoreApplication.translate("Form", u"label", None))
        self.pic.setText("")
        self.yes.setText(QCoreApplication.translate("Form", u"Sim", None))
        self.no.setText(QCoreApplication.translate("Form", u"N\u00e3o", None))
    # retranslateUi

