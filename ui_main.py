# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestor_mailing.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 532)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.centralwidget.setPalette(palette)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fr_titulo = QFrame(self.centralwidget)
        self.fr_titulo.setObjectName(u"fr_titulo")
        self.fr_titulo.setMaximumSize(QSize(16777215, 80))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        self.fr_titulo.setPalette(palette1)
        self.fr_titulo.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.fr_titulo.setFrameShape(QFrame.StyledPanel)
        self.fr_titulo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_titulo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(self.fr_titulo)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.lbl_titulo.setPalette(palette2)

        self.verticalLayout.addWidget(self.lbl_titulo)


        self.verticalLayout_2.addWidget(self.fr_titulo)

        self.fr_principal = QFrame(self.centralwidget)
        self.fr_principal.setObjectName(u"fr_principal")
        self.fr_principal.setStyleSheet(u"")
        self.fr_principal.setFrameShape(QFrame.StyledPanel)
        self.fr_principal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_principal)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_clientes = QTableWidget(self.fr_principal)
        if (self.tb_clientes.columnCount() < 2):
            self.tb_clientes.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_clientes.setObjectName(u"tb_clientes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_clientes.sizePolicy().hasHeightForWidth())
        self.tb_clientes.setSizePolicy(sizePolicy)
        self.tb_clientes.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.tb_clientes)

        self.fr_botoes = QFrame(self.fr_principal)
        self.fr_botoes.setObjectName(u"fr_botoes")
        self.fr_botoes.setMinimumSize(QSize(250, 0))
        self.fr_botoes.setMaximumSize(QSize(200, 16777215))
        self.fr_botoes.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.fr_botoes.setFrameShape(QFrame.StyledPanel)
        self.fr_botoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_botoes)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bt_checar = QPushButton(self.fr_botoes)
        self.bt_checar.setObjectName(u"bt_checar")
        self.bt_checar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.bt_checar)

        self.bt_extrair = QPushButton(self.fr_botoes)
        self.bt_extrair.setObjectName(u"bt_extrair")
        self.bt_extrair.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.bt_extrair)

        self.bt_exportar = QPushButton(self.fr_botoes)
        self.bt_exportar.setObjectName(u"bt_exportar")
        self.bt_exportar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.bt_exportar)

        self.fr_info_tabela = QFrame(self.fr_botoes)
        self.fr_info_tabela.setObjectName(u"fr_info_tabela")
        self.fr_info_tabela.setFrameShape(QFrame.StyledPanel)
        self.fr_info_tabela.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_info_tabela)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_infos = QLabel(self.fr_info_tabela)
        self.lbl_infos.setObjectName(u"lbl_infos")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.lbl_infos.setPalette(palette3)
        self.lbl_infos.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.lbl_infos)


        self.verticalLayout_3.addWidget(self.fr_info_tabela)


        self.horizontalLayout.addWidget(self.fr_botoes)

        self.fr_botoes.raise_()
        self.tb_clientes.raise_()

        self.verticalLayout_2.addWidget(self.fr_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setInputMethodHints(Qt.ImhNone)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de Mailing", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Gestor de Mailing</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        self.bt_checar.setText(QCoreApplication.translate("MainWindow", u"CHECAR ARQUIVO", None))
        self.bt_extrair.setText(QCoreApplication.translate("MainWindow", u"EXTRAIR DADOS", None))
        self.bt_exportar.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR PARA EXCEL", None))
        self.lbl_infos.setText("")
    # retranslateUi

