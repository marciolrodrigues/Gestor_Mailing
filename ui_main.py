# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestor_mailing_jucesp.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1627, 777)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.tab_principal = QTabWidget(self.fr_principal)
        self.tab_principal.setObjectName(u"tab_principal")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.tab_principal.setFont(font)
        self.tab_principal.setStyleSheet(u"")
        self.tabwid_extraidos = QWidget()
        self.tabwid_extraidos.setObjectName(u"tabwid_extraidos")
        self.tabwid_extraidos.setStyleSheet(u"selection-color: rgb(0, 0, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.tabwid_extraidos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tb_clientes = QTableWidget(self.tabwid_extraidos)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_clientes.sizePolicy().hasHeightForWidth())
        self.tb_clientes.setSizePolicy(sizePolicy1)
        self.tb_clientes.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.tb_clientes.setFont(font1)
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

        self.verticalLayout_5.addWidget(self.tb_clientes)

        self.tab_principal.addTab(self.tabwid_extraidos, "")
        self.tabwid_jucesp = QWidget()
        self.tabwid_jucesp.setObjectName(u"tabwid_jucesp")
        self.verticalLayout_6 = QVBoxLayout(self.tabwid_jucesp)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fr_jucesp = QFrame(self.tabwid_jucesp)
        self.fr_jucesp.setObjectName(u"fr_jucesp")
        self.fr_jucesp.setFrameShape(QFrame.StyledPanel)
        self.fr_jucesp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.fr_jucesp)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.fr_titulo_jucesp = QFrame(self.fr_jucesp)
        self.fr_titulo_jucesp.setObjectName(u"fr_titulo_jucesp")
        sizePolicy1.setHeightForWidth(self.fr_titulo_jucesp.sizePolicy().hasHeightForWidth())
        self.fr_titulo_jucesp.setSizePolicy(sizePolicy1)
        self.fr_titulo_jucesp.setMinimumSize(QSize(0, 0))
        self.fr_titulo_jucesp.setFrameShape(QFrame.StyledPanel)
        self.fr_titulo_jucesp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_titulo_jucesp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_titulo_jucesp = QLabel(self.fr_titulo_jucesp)
        self.lbl_titulo_jucesp.setObjectName(u"lbl_titulo_jucesp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_titulo_jucesp.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_jucesp.setSizePolicy(sizePolicy2)
        self.lbl_titulo_jucesp.setMaximumSize(QSize(16777215, 50))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        self.lbl_titulo_jucesp.setPalette(palette3)

        self.horizontalLayout_2.addWidget(self.lbl_titulo_jucesp)


        self.verticalLayout_7.addWidget(self.fr_titulo_jucesp)

        self.fr_dados_jucesp = QFrame(self.fr_jucesp)
        self.fr_dados_jucesp.setObjectName(u"fr_dados_jucesp")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.fr_dados_jucesp.setFont(font2)
        self.fr_dados_jucesp.setFrameShape(QFrame.StyledPanel)
        self.fr_dados_jucesp.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fr_dados_jucesp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.fr_dados_jucesp)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.txt_capital_min = QTextEdit(self.fr_dados_jucesp)
        self.txt_capital_min.setObjectName(u"txt_capital_min")
        self.txt_capital_min.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.txt_capital_min, 2, 1, 1, 1)

        self.label = QLabel(self.fr_dados_jucesp)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.txt_data_inicio = QDateEdit(self.fr_dados_jucesp)
        self.txt_data_inicio.setObjectName(u"txt_data_inicio")
        self.txt_data_inicio.setMinimumSize(QSize(0, 40))
        self.txt_data_inicio.setFont(font)
        self.txt_data_inicio.setLayoutDirection(Qt.LeftToRight)
        self.txt_data_inicio.setCalendarPopup(True)
        self.txt_data_inicio.setCurrentSectionIndex(0)
        self.txt_data_inicio.setDate(QDate(2023, 9, 1))

        self.gridLayout.addWidget(self.txt_data_inicio, 1, 1, 1, 1)

        self.txt_cidade = QTextEdit(self.fr_dados_jucesp)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.txt_cidade, 1, 5, 1, 1)

        self.txt_data_fim = QDateEdit(self.fr_dados_jucesp)
        self.txt_data_fim.setObjectName(u"txt_data_fim")
        self.txt_data_fim.setMinimumSize(QSize(0, 40))
        self.txt_data_fim.setFont(font)
        self.txt_data_fim.setLayoutDirection(Qt.LeftToRight)
        self.txt_data_fim.setCalendarPopup(True)
        self.txt_data_fim.setCurrentSectionIndex(0)
        self.txt_data_fim.setDate(QDate(2023, 9, 1))

        self.gridLayout.addWidget(self.txt_data_fim, 1, 3, 1, 1)

        self.label_2 = QLabel(self.fr_dados_jucesp)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.fr_dados_jucesp)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)

        self.label_5 = QLabel(self.fr_dados_jucesp)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.btn_consultar = QPushButton(self.fr_dados_jucesp)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setMinimumSize(QSize(0, 60))
        self.btn_consultar.setFont(font)

        self.gridLayout.addWidget(self.btn_consultar, 3, 3, 1, 1)

        self.ch_box_pendentes = QCheckBox(self.fr_dados_jucesp)
        self.ch_box_pendentes.setObjectName(u"ch_box_pendentes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ch_box_pendentes.sizePolicy().hasHeightForWidth())
        self.ch_box_pendentes.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.ch_box_pendentes, 2, 4, 1, 2, Qt.AlignHCenter)

        self.txt_capital_max = QTextEdit(self.fr_dados_jucesp)
        self.txt_capital_max.setObjectName(u"txt_capital_max")
        self.txt_capital_max.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.txt_capital_max, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 800, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.fr_dados_jucesp)


        self.verticalLayout_6.addWidget(self.fr_jucesp)

        self.tab_principal.addTab(self.tabwid_jucesp, "")

        self.horizontalLayout.addWidget(self.tab_principal)

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
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.lbl_infos.setPalette(palette4)
        self.lbl_infos.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.lbl_infos)

        self.txt_tempo = QLabel(self.fr_info_tabela)
        self.txt_tempo.setObjectName(u"txt_tempo")
        self.txt_tempo.setMaximumSize(QSize(16777215, 50))
        self.txt_tempo.setStyleSheet(u"")
        self.txt_tempo.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.txt_tempo)


        self.verticalLayout_3.addWidget(self.fr_info_tabela)


        self.horizontalLayout.addWidget(self.fr_botoes)


        self.verticalLayout_2.addWidget(self.fr_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setInputMethodHints(Qt.ImhNone)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_principal.setCurrentIndex(0)


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
        self.tab_principal.setTabText(self.tab_principal.indexOf(self.tabwid_extraidos), QCoreApplication.translate("MainWindow", u"Extra\u00eddos", None))
        self.lbl_titulo_jucesp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Informa\u00e7\u00f5es para consulta na JUCESP</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CAPITAL MINIMO", None))
        self.txt_capital_min.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DATA INCIAL:", None))
        self.txt_cidade.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Campinas</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DATA FINAL", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CAPITAL M\u00c1XIMO", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.ch_box_pendentes.setText(QCoreApplication.translate("MainWindow", u"Validar pendentes?", None))
        self.txt_capital_max.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.tab_principal.setTabText(self.tab_principal.indexOf(self.tabwid_jucesp), QCoreApplication.translate("MainWindow", u"JUCESP", None))
        self.bt_checar.setText(QCoreApplication.translate("MainWindow", u"CHECAR ARQUIVO", None))
        self.bt_extrair.setText(QCoreApplication.translate("MainWindow", u"EXTRAIR DADOS", None))
        self.bt_exportar.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR PARA EXCEL", None))
        self.bt_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR DADOS", None))
        self.lbl_infos.setText("")
        self.txt_tempo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

