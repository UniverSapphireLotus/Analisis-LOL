# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dasdh_bo.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1489, 883)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_barra_menu = QFrame(self.centralwidget)
        self.frame_barra_menu.setObjectName(u"frame_barra_menu")
        self.frame_barra_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_barra_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_13 = QFrame(self.frame_barra_menu)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_13)

        self.frame_5 = QFrame(self.frame_barra_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.boto_men1 = QPushButton(self.frame_5)
        self.boto_men1.setObjectName(u"boto_men1")

        self.verticalLayout_2.addWidget(self.boto_men1)

        self.boto_men2 = QPushButton(self.frame_5)
        self.boto_men2.setObjectName(u"boto_men2")

        self.verticalLayout_2.addWidget(self.boto_men2)

        self.boto_men3 = QPushButton(self.frame_5)
        self.boto_men3.setObjectName(u"boto_men3")

        self.verticalLayout_2.addWidget(self.boto_men3)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_barra_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon = QIcon()
        icon.addFile(u"icono/cait.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_barra_menu, 0, 0, 2, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame_2, 1, 2, 1, 1)

        self.frame_barra_tool = QFrame(self.centralwidget)
        self.frame_barra_tool.setObjectName(u"frame_barra_tool")
        self.frame_barra_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_tool.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_barra_tool)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.frame_barra_tool)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.combo_championName = QComboBox(self.frame_11)
        self.combo_championName.setObjectName(u"combo_championName")

        self.gridLayout_3.addWidget(self.combo_championName, 1, 1, 1, 1)

        self.lab_win_rate = QLabel(self.frame_11)
        self.lab_win_rate.setObjectName(u"lab_win_rate")

        self.gridLayout_3.addWidget(self.lab_win_rate, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.lab_vece_jugado = QLabel(self.frame_11)
        self.lab_vece_jugado.setObjectName(u"lab_vece_jugado")

        self.gridLayout_3.addWidget(self.lab_vece_jugado, 2, 1, 1, 1)

        self.combo_elo = QComboBox(self.frame_11)
        self.combo_elo.setObjectName(u"combo_elo")

        self.gridLayout_3.addWidget(self.combo_elo, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_barra_tool)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.boto_pred = QPushButton(self.frame_12)
        self.boto_pred.setObjectName(u"boto_pred")
        self.boto_pred.setMinimumSize(QSize(80, 80))
        self.boto_pred.setMaximumSize(QSize(16777215, 16777215))
        self.boto_pred.setSizeIncrement(QSize(80, 80))
        icon1 = QIcon()
        icon1.addFile(u"icono/vi.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.boto_pred.setIcon(icon1)
        self.boto_pred.setIconSize(QSize(120, 120))

        self.gridLayout_5.addWidget(self.boto_pred, 3, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.gridLayout.addWidget(self.frame_barra_tool, 1, 1, 1, 1)

        self.frame_tool = QFrame(self.centralwidget)
        self.frame_tool.setObjectName(u"frame_tool")
        self.frame_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_tool.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tool)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boto_menu = QToolButton(self.frame_tool)
        self.boto_menu.setObjectName(u"boto_menu")
        self.boto_menu.setMinimumSize(QSize(40, 40))
        self.boto_menu.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_menu)

        self.boto_tool = QToolButton(self.frame_tool)
        self.boto_tool.setObjectName(u"boto_tool")
        self.boto_tool.setMinimumSize(QSize(40, 40))
        self.boto_tool.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_tool)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.boto_min = QToolButton(self.frame_tool)
        self.boto_min.setObjectName(u"boto_min")
        self.boto_min.setMinimumSize(QSize(40, 40))
        self.boto_min.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_min)

        self.boto_restaurar = QToolButton(self.frame_tool)
        self.boto_restaurar.setObjectName(u"boto_restaurar")
        self.boto_restaurar.setMinimumSize(QSize(40, 40))
        self.boto_restaurar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_restaurar)

        self.boto_max = QToolButton(self.frame_tool)
        self.boto_max.setObjectName(u"boto_max")
        self.boto_max.setMinimumSize(QSize(40, 40))
        self.boto_max.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_max)

        self.boto_cerrar = QToolButton(self.frame_tool)
        self.boto_cerrar.setObjectName(u"boto_cerrar")
        self.boto_cerrar.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_cerrar)


        self.gridLayout.addWidget(self.frame_tool, 0, 1, 1, 2)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 19)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 8)
        self.gridLayout.setColumnStretch(2, 21)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boto_men1.setText(QCoreApplication.translate("MainWindow", u"Caja", None))
        self.boto_men2.setText(QCoreApplication.translate("MainWindow", u"Histograma y densidad", None))
        self.boto_men3.setText(QCoreApplication.translate("MainWindow", u"Correlacion", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PIN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Campeon", None))
        self.lab_win_rate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Porcentaje win", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Veces Jugado", None))
        self.lab_vece_jugado.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Elo", None))
        self.boto_pred.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.boto_menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_tool.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_min.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_restaurar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_max.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_cerrar.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

