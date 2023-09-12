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
        if (self.tb_clientes.columnCount() < 28):
            self.tb_clientes.setColumnCount(28)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        self.tb_clientes.setObjectName(u"tb_clientes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_clientes.sizePolicy().hasHeightForWidth())
        self.tb_clientes.setSizePolicy(sizePolicy)
        self.tb_clientes.setMaximumSize(QSize(16777215, 16777215))
        self.tb_clientes.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
" }\n"
"\n"
"QTableWidget{\n"
"	\n"
"	background-color: rgb(252, 252, 252);\n"
"\n"
"}")

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

        self.bt_excluir = QPushButton(self.fr_botoes)
        self.bt_excluir.setObjectName(u"bt_excluir")
        self.bt_excluir.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.bt_excluir)

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
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"abertura", None));
        ___qtablewidgetitem1 = self.tb_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"situacao", None));
        ___qtablewidgetitem2 = self.tb_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"tipo", None));
        ___qtablewidgetitem3 = self.tb_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"nome", None));
        ___qtablewidgetitem4 = self.tb_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"porte", None));
        ___qtablewidgetitem5 = self.tb_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"natureza_juridica", None));
        ___qtablewidgetitem6 = self.tb_clientes.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"atividade_principal_list", None));
        ___qtablewidgetitem7 = self.tb_clientes.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"atividades_secundarias_list", None));
        ___qtablewidgetitem8 = self.tb_clientes.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"qsa_list", None));
        ___qtablewidgetitem9 = self.tb_clientes.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"logradouro", None));
        ___qtablewidgetitem10 = self.tb_clientes.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"numero", None));
        ___qtablewidgetitem11 = self.tb_clientes.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"municipio", None));
        ___qtablewidgetitem12 = self.tb_clientes.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"bairro", None));
        ___qtablewidgetitem13 = self.tb_clientes.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"uf", None));
        ___qtablewidgetitem14 = self.tb_clientes.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"cep", None));
        ___qtablewidgetitem15 = self.tb_clientes.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"email", None));
        ___qtablewidgetitem16 = self.tb_clientes.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"telefone", None));
        ___qtablewidgetitem17 = self.tb_clientes.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"data_situacao", None));
        ___qtablewidgetitem18 = self.tb_clientes.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"cnpj", None));
        ___qtablewidgetitem19 = self.tb_clientes.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ultima_atualizacao", None));
        ___qtablewidgetitem20 = self.tb_clientes.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"status", None));
        ___qtablewidgetitem21 = self.tb_clientes.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"fantasia", None));
        ___qtablewidgetitem22 = self.tb_clientes.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"complemento", None));
        ___qtablewidgetitem23 = self.tb_clientes.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"efr", None));
        ___qtablewidgetitem24 = self.tb_clientes.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"motivo_situacao", None));
        ___qtablewidgetitem25 = self.tb_clientes.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"situacao_especial", None));
        ___qtablewidgetitem26 = self.tb_clientes.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"data_situacao_especial", None));
        ___qtablewidgetitem27 = self.tb_clientes.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"capital_social", None));
        self.bt_checar.setText(QCoreApplication.translate("MainWindow", u"CHECAR ARQUIVO", None))
        self.bt_extrair.setText(QCoreApplication.translate("MainWindow", u"EXTRAIR DADOS", None))
        self.bt_exportar.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR PARA EXCEL", None))
        self.bt_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR DADOS", None))
        self.lbl_infos.setText("")
    # retranslateUi

