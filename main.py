from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_main import Ui_MainWindow
from utils import calcula_tempo
from database import DataBase
from ui_functions import extrair_clientes
from time import sleep
import pandas as pd
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.bt_checar.clicked.connect(self.consulta_base)
        self.bt_extrair.clicked.connect(self.extracao)
        self.bt_exportar.clicked.connect(self.gerar_excel)
        self.buscar_empresas()

    def buscar_empresas(self):
        db = DataBase()
        db.connect()
        result = db.select_all_companies()

        self.tb_clientes.clearContents()
        self.tb_clientes.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_clientes.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()

    def cadastrar_empresas(self, lista_cadastro):
        self.statusbar.showMessage('Conectando ao banco de dados...')
        QApplication.processEvents()
        db = DataBase()
        db.connect()

        # CADASTRAR NO BANCO DE DADOS
        self.statusbar.showMessage('Gravando no banco de dados...')
        QApplication.processEvents()
        resp = db.register_company(lista_cadastro)

        db.close_connection()

        # if resp == "OK":
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Information)
        #     msg.setWindowTitle("Casdastro Realizado")
        #     msg.setText("Cadastro Realizado com sucesso")
        #     msg.exec()
        #     db.close_connection()
        #     return
        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setWindowTitle("Erro")
        #     msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
        #     msg.exec()
        #     db.close_connection()
        #     return

    def gerar_excel(self):

        dados = []
        all_dados = []

        for row in range(self.tb_clientes.rowCount()):
            for column in range(self.tb_clientes.columnCount()):
                dados.append(self.tb_clientes.item(row, column).text())

            all_dados.append(dados)
            dados = []

        columns = ['ABERTURA', 'SITUACAO', 'TIPO', 'NOME', 'PORTE', 'NATUREZA_JURIDICA', 'ATIVIDADE_PRINCIPAL',
                   'ATIVIDADES_SECUNDARIAS', 'QSA', 'LOGRADOURO', 'NUMERO', 'MUNICIPIO', 'BAIRRO', 'UF', 'CEP',
                   'EMAIL', 'TELEFONE', 'DATA_SITUACAO', 'CNPJ', 'ULTIMA_ATUALIZACAO', 'STATUS', 'FANTASIA',
                   'COMPLEMENTO', 'EFR', 'MOTIVO_SITUACAO', 'SITUACAO_ESPECIAL', 'DATA_SITUACAO_ESPECIAL',
                   'CAPITAL_SOCIAL']
        empresas = pd.DataFrame(all_dados, columns=columns)
        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def consulta_base(self):
        clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
        lista_clientes = clientes_df['CNPJ'].astype(str).str.zfill(14).tolist()
        tempo_extracao = (len(lista_clientes) / 3) - 1
        self.lbl_infos.setText(f'-> O arquivo possui {str(len(lista_clientes))} CNPJ(s)\n'
                               f'-> O processo vai demorar cerca de {tempo_extracao:,.0f} minuto(s)\n'
                               f'-> A previsão de término começando agora é para às '
                               f'{calcula_tempo(lista_clientes)}hs')

    def extracao(self):
        clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
        lista_cnpj = clientes_df['CNPJ'].astype(str).str.zfill(14).tolist()
        min_totais = (len(lista_cnpj) / 3) - 1
        qtde_cnpjs = len(lista_cnpj)

        self.lbl_infos.setText(f'Iniciando o processo de extração de {qtde_cnpjs} clientes.\n'
                               f'O processo deve demorar cerca de {min_totais} minutos.\n'
                               f'Previsão de término: {calcula_tempo(lista_cnpj)}hs')
        QApplication.processEvents()

        envio = []
        contador = 0
        lista_final = []
        resultado_final = []

        for item in lista_cnpj:
            envio.append(item)
            contador += 1
            if contador % 3 == 0 or contador == qtde_cnpjs:
                self.lbl_infos.setText(f'Solicitando consulta dos clientes de '
                                       f'{contador - 3 if contador % 3 == 0 else contador - contador % 3} à {contador} '
                                       f'de um total de {qtde_cnpjs}!')
                self.statusbar.showMessage('Consultando Base da Receita..')
                QApplication.processEvents()
                retorno_extracao = extrair_clientes(envio)
                if type(retorno_extracao) == int:  # verifica se o retorno da API é um erro (time out ou + de 3 consultas)
                    self.tb_clientes.clearContents()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Aguardar")
                    msg.setText("Aguarde 1 minuto para efetuar uma nova consulta!")
                    msg.exec()
                    self.statusbar.showMessage('Não se passou ao menos 1 minuto desde a última consulta!')
                    return
                else:  # se o retorno for o resultado da consulta
                    lista_extraida, resultado_extracao = retorno_extracao
                    lista_final = lista_final + lista_extraida
                    resultado_final = resultado_final + resultado_extracao

                    if contador < qtde_cnpjs:
                        self.statusbar.showMessage('Aguardando 1 minuto até a próxima consulta')
                        QApplication.processEvents()
                        sleep(60)
                        envio = []
        qtde_erros = 0
        for sublista in resultado_final:
            qtde_erros += sublista.count('CNPJ inválido')

        for item in lista_final:
            self.cadastrar_empresas(item)

        self.buscar_empresas()

        self.lbl_infos.setText(f'Extração finalizada com sucesso\n{qtde_erros} CNPJ(s) deram erro na extração')
        self.statusbar.showMessage('Pronto!')


if __name__ == '__main__':
    db = DataBase()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
