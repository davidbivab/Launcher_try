# -*- coding: utf-8 -*-
import PySide6.QtCore

import downloader
import stats
import re
################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from downloader import mod_pack_get
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QThread, Signal,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget, QProgressBar,QSlider)
import background_rc


class Launch_game(QThread):
    def __init__(self, progress_bar, progress_label,function1,main, parent=None):
        super().__init__(parent)
        self.progress_bar = progress_bar
        self.progress_bar.setVisible(False)
        self.progress_bar.setValue(10)
        self.progress_label = progress_label
        self.function1 = function1
        self.main = main

    def run(self):
        try:
            self.progress_bar.setValue(20)
            self.progress_bar.setVisible(True)
            self.progress_label.setText('Качаем')
            downloader.get_jsons()
        finally:
            self.progress_bar.setValue(30)
            downloader.game_get()
            self.progress_bar.setValue(60)
            downloader.modpack_download(downloader.get_modpack_version())
            self.progress_bar.setValue(70)
            downloader.mod_pack_get()
            self.progress_bar.setValue(100)
            self.progress_label.setText('Играем')
            downloader.game_start()
            self.progress_bar.setVisible(False)
            self.progress_label.setText('')
            self.function1()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        id = QFontDatabase.addApplicationFont('fonts/minecraft.ttf')
        if id == -1:
            print('Шрифт minecraft не установлен')
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QSize(300, 400))
        MainWindow.setMaximumSize(QSize(300, 400))
        MainWindow.setStyleSheet(u"QPushButton{\n"
                                 "color:rgb(128,128,128);\n"
                                 "background-color:rgb(1,1,1);\n"
                                 "}\n"
                                 "QFrame{background-image:url(:/images/images/Sprite-0002.jpg);}\n"
                                 "QPushButton#pushButton:hover {\n"
                                 "    color: rgb(249, 255, 184);\n"
                                 "	icon: url(:/images/images/playbutton_lite_on.jpg);\n"
                                 "}\n"
                                 "QPushButton#pushButton_2:hover {\n"
                                 "    color: rgb(249, 255, 184);\n"
                                 "	icon:url(:/images/images/settings_button_light_on.jpg);\n"
                                 "\n"
                                 "}\n"
                                 "QLabel{\n"
                                 "color:rgb(128,128,128);\n"
                                 "background-color:rgb(1,1,1);\n"
                                 "background-image:url();\n"
                                 "}\n"
                                 "QLineEdit{\n"
                                 "	color:rgb(128,128,128);\n"
                                 "	background-color:rgb(1,1,1);\n"
                                 "	border-width: 1px; border-style: solid; border-color: rgb(128,128,128);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover{\n"
                                 "	color:rgb(249, 255, 184);\n"
                                 "	background-color:rgb(1,1,1);\n"
                                 "	border-width: 1px; border-style: solid; border-color: rgb(249, 255, 184);\n"
                                 "}\n"
                                 "QProgressBar{\n"
                                 "	color:rgb(1,1,1);\n"
                                 "	background-color:rgb(1,1,1);\n"
                                 "	border-width: 1px; border-style: solid; border-color: rgb(249, 255, 184);\n"
                                 "}\n"
                                 "QProgressBar:chunk {\n"
                                 "background-color: rgb(249, 255, 184);\n"
                                 "}"
                                 "QSlider::handle:horizontal {\n"
                                 "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                 "    border: 1px solid ;\n"
                                 "	background-color:rgb(128,128,128);\n"
                                 "   /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
                                 "\n"
                                 "}\n"
                                 "QSlider::handle:horizontal:hover {\n"
                                 "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                 "    border: 1px solid ;\n"
                                 "	background-color:rgb(249, 255, 184);\n"
                                 "   /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
                                 "\n"
                                 "}\n"
                                 )
        font_base = QFontDatabase.addApplicationFont(u":/fonts/fonts/minecraft.ttf")
        m_font = QFontDatabase.applicationFontFamilies(font_base)
        font = QFont()
        font.setFamilies(m_font)
        font.setPointSize(14)
        font.setWeight(QFont.Thin)
        font.setKerning(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -2, 311, 411))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(5, 120, 111, 21))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"font: 9pt;")
        icon = QIcon()
        icon.addFile(u":/images/images/playbutton_lite_off.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        # Вот тут ввод никнейма
        self.lineEdit = QLineEdit(self.frame)
        with open('client_options.json') as json_client:
            self.lineEdit.setText(json.load(json_client)['username'])
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(150, 120, 113, 22))
        self.lineEdit.setMaxLength(32)
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit.setStyleSheet(u"font: 6pt;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 30, 121, 51))
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(6)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 360, 61, 21))
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setLineWidth(0)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(6)
        self.label_2.setIndent(-1)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(125, 95, 161, 21))
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setTabletTracking(False)
        self.label_3.setAcceptDrops(False)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(0)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setMargin(6)
        self.label_3.setIndent(-1)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 150, 111, 16))
        self.label_4.setFont(font)
        self.label_2.setStyleSheet(u"font: 6pt ")
        self.label_3.setStyleSheet(u"font: 6pt ")
        self.label_4.setStyleSheet(u"font: 6pt ")
        # progress bar

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(24, 120, 101, 21))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_clickk)
        self.pushButton.clicked.connect(self.on_imput)
        self.launch_potok = Launch_game(progress_bar=self.progressBar, progress_label=self.label_4,function1=self.full_hide,main = self)

    # Кнопка настроек
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(17, 140, 111, 21))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"font: 9pt;\n")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/settings_button_light_off.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setText('Настройки')
        self.pushButton_2.clicked.connect(self.show_settings)

        self.Slider = QSlider(self.frame)
        self.Slider.setObjectName(u"Slider")
        self.Slider.setGeometry(QRect(75, 180, 150, 22))
        self.Slider.setFont(font)
        self.Slider.setCursor(QCursor(Qt.ArrowCursor))
        self.Slider.setMouseTracking(True)
        self.Slider.setOrientation(Qt.Horizontal)
        self.Slider.setTickPosition(QSlider.TicksAbove)
        self.Slider.setTickInterval(2)
        self.Slider.setMinimum(1)
        with open('client_options.json') as file:
            file_d = json.load(file)
            to_set = (int(re.search(r'\d+',file_d['jvmArguments'][0]).group()))
        self.Slider.setValue(to_set)
        self.Slider.setMaximum(stats.get_mem())
        self.Slider.valueChanged.connect(self.update)
        self.Slider.valueChanged.connect(self.slider_mem)
        self.Slider.setHidden(True)


        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 180, 51, 22))
        self.lineEdit_2.setText(str(self.Slider.value()))
        self.lineEdit_2.setInputMask('99')
        self.lineEdit_2.textChanged.connect(self.slider_update)
        self.lineEdit_2.setHidden(True)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 184, 24, 16))
        self.label_5.setFont(font)
        self.label_5.setText('ОЗУ')
        self.label_5.setStyleSheet(u"font: 8pt ")
        self.label_5.setHidden(True)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.lineEdit.setInputMask("")
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0443\u043d\u0447\u0435\u0440", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v 0.1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410 \u0441\u044e\u0434\u0430 \u0442\u0438\u043f\u043e \u043d\u0438\u043a\u043d\u0435\u0439\u043c \u043f\u0438\u0441\u0430\u0442\u044c",None))

    def on_imput(self):
        print(self.lineEdit.text())
        with open("client_options.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            data["username"] = str(self.lineEdit.text())
            jsonFile.seek(0)  # курсор к нулю
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def on_clickk(self):
        self.launch_potok.start()
        self.full_hide()
    def update(self):
        self.lineEdit_2.setText(str(self.Slider.value()))
    def slider_update(self):
        if self.lineEdit_2.text() == '':
            self.Slider.setValue(6)
        else:
            self.Slider.setValue(int(self.lineEdit_2.text()))
    def slider_mem(self):
        with open('client_options.json', 'r+') as file:
            file_data = json.load(file)
            file_data['jvmArguments'][0] = re.sub(r'(-Xms)(\d+)([GgMmKk]?)', '-Xms' + str(self.Slider.value())+'G', file_data['jvmArguments'][0])
            file_data['jvmArguments'][1] = re.sub(r'(-Xmx)(\d+)([GgMmKk]?)', '-Xmx' + str(self.Slider.value())+'G', file_data['jvmArguments'][1])
            file.seek(0)
            json.dump(file_data, file)
            file.truncate()
    def show_settings(self):
        if self.Slider.isHidden():
            self.label_5.setHidden(False)
            self.Slider.setHidden(False)
            self.lineEdit_2.setHidden(False)
        else:
            self.label_5.setHidden(True)
            self.Slider.setHidden(True)
            self.lineEdit_2.setHidden(True)
    def full_hide(self):
        if self.pushButton_2.isHidden():
            self.pushButton_2.setHidden(False)
        else:
            self.pushButton_2.setHidden(True)
        if not self.Slider.isHidden():
            self.label_5.setHidden(True)
            self.Slider.setHidden(True)
            self.lineEdit_2.setHidden(True)

# retranslateUi
