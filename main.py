from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_main import Ui_MainWindow
from utils import calcula_tempo, consulta_planilha, atualiza_planilha, tempo_espera, atualiza_jucesp
from jucesp import consulta_jucesp
from database import DataBase
from ui_functions import extrair_clientes
from time import sleep
import pandas as pd
import sys
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.bt_checar.clicked.connect(self.consulta_base)
        self.bt_extrair.clicked.connect(self.extracao)
        self.bt_exportar.clicked.connect(self.gerar_excel)
        self.bt_excluir.clicked.connect(self.deletar_base)
        self.btn_consultar.clicked.connect(self.jucesp)
        self.buscar_empresas()

        data_atual = datetime.datetime.now()
        data_limite = datetime.datetime(2023, 9, 30)
        if data_atual <= data_limite:
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('PROGRAMA EXPIRADO')
            msg.setText('O perído de testes expirou, faça contato com o desenvolvedor!')
            msg.exec()
            exit(0)

    def jucesp(self):
        data_inicio = self.txt_data_inicio.text()
        data_final = self.txt_data_fim.text()
        cidade = self.txt_cidade.toPlainText()
        capital_min = self.txt_capital_min.toPlainText()
        capital_max = self.txt_capital_max.toPlainText()
        retorno_jucesp = consulta_jucesp(data_inicio, data_final, cidade, capital_min, capital_max)
        if len(retorno_jucesp) > 0:
            atualiza_jucesp(retorno_jucesp)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("CONSULTA JUCESP")
            msg.setText(f'Foram extraídas {len(retorno_jucesp)} empresas!')
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("CONSULTA JUCESP")
            msg.setText('A consulta não retornou empresas!')
            msg.exec()

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
        self.tb_clientes.resizeColumnsToContents()

    def cadastrar_empresas(self, lista_cadastro):
        self.statusbar.showMessage('Conectando ao banco de dados...')
        QApplication.processEvents()
        db = DataBase()
        db.connect()

        # CADASTRAR NO BANCO DE DADOS
        self.statusbar.showMessage('Gravando no banco de dados...')
        QApplication.processEvents()
        db.register_company(lista_cadastro)

        db.close_connection()
        self.buscar_empresas()

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
        lista_clientes, list_ja_processado = consulta_planilha()
        if lista_clientes == 'sem_coluna':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('PLANILHA')
            msg.setText('Não foi encontrada a coluna com nome de "CNPJ" na planilha "base_cnpj.xlsx" !')
            msg.exec()
            return
        if len(lista_clientes) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('PLANILHA')
            msg.setText('Não foram encontrados novos CNPJs para consultar na planilha "base_cnpj.xlsx" !')
            msg.exec()
            return
        tempo_extracao = (len(lista_clientes) / 3) - 1
        self.lbl_infos.setText(f'-> O arquivo possui {str(len(lista_clientes))} CNPJ(s)\n'
                               f'-> O processo vai demorar cerca de {tempo_extracao:,.0f} minuto(s)\n'
                               f'-> A previsão de término começando agora é para às '
                               f'{calcula_tempo(lista_clientes)}hs')

    def extracao(self):
        self.tab_principal.setCurrentIndex(0)
        lista_cnpj, resultado_final = consulta_planilha()
        if lista_cnpj == 'sem_coluna':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('PLANILHA')
            msg.setText('Não foi encontrada a coluna com nome de "CNPJ" na planilha "base_cnpj.xlsx" !')
            msg.exec()
            return
        if len(lista_cnpj) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('PLANILHA')
            msg.setText('Não foram encontrados novos CNPJs para consultar na planilha "base_cnpj.xlsx" !')
            msg.exec()
            return

        min_totais = (len(lista_cnpj) / 3) - 1
        qtde_cnpjs = len(lista_cnpj)

        envio = []
        contador = 0
        lista_final = []
        # resultado_final = []

        for item in lista_cnpj:
            envio.append(item)
            contador += 1
            if contador % 3 == 0 or contador == qtde_cnpjs:
                self.lbl_infos.setText(f'Iniciado o processo de extração de {qtde_cnpjs} clientes.\n\n'
                                       f'O processo deve demorar cerca de {round(min_totais)} minutos.\n\n'
                                       f'Solicitando consulta dos clientes de\n'
                                       f'{contador - 3 if contador % 3 == 0 else contador - contador % 3} à {contador} '
                                       f'de um total de {qtde_cnpjs}!\n\n'
                                       f'Previsão de término: {calcula_tempo(lista_cnpj, contador)}hs')
                self.statusbar.showMessage('Consultando Base da Receita..')
                QApplication.processEvents()
                retorno_extracao = extrair_clientes(envio)
                tempo_inicio = datetime.datetime.now()
                if type(retorno_extracao) == int:  # verifica se o retorno da API é um erro (time out ou + de 3 consultas)
                    self.tb_clientes.clearContents()
                    self.statusbar.showMessage('Não se passou ao menos 1 minuto desde a última consulta!')
                    QApplication.processEvents()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Aguardar")
                    msg.setText("Aguarde 1 minuto para efetuar uma nova consulta!")
                    msg.exec()
                    return
                elif retorno_extracao == 'internet':  # verifica se o retorno foi erro com a conexão
                    self.tb_clientes.clearContents()
                    self.statusbar.showMessage('Não foi possível efetuar a consulta por problemas com a internet!')
                    QApplication.processEvents()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("SEM CONEXÃO")
                    msg.setText("Verifique sua conexão com a intenet. Sem comunicação com o servidor!")
                    msg.exec()
                else:  # se o retorno for o resultado da consulta
                    lista_extraida, resultado_extracao = retorno_extracao
                    lista_final = lista_final + lista_extraida
                    resultado_final = resultado_final + resultado_extracao
                    for empresa in lista_extraida:
                        self.cadastrar_empresas(empresa)
                    atualiza_planilha(resultado_final)

                    if contador < qtde_cnpjs:
                        self.statusbar.showMessage(f'Aguardando {tempo_espera(tempo_inicio)} segundos até a '
                                                   f'próxima consulta')
                        QApplication.processEvents()
                        sleep(tempo_espera(tempo_inicio))
                        envio = []
        qtde_erros = 0
        for sublista in resultado_final:
            qtde_erros += sublista.count('CNPJ inválido')

        self.lbl_infos.setText(f'Extração finalizada com sucesso\n{qtde_erros} CNPJ(s) deram erro na extração')
        self.statusbar.showMessage('Pronto!')

    def deletar_base(self):
        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Exclusão de TODA A BASE de dados já extraída!")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            result = db.delete_companies()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUSÃO DA BASE")
            msg.setText(result)
            msg.exec()

        self.buscar_empresas()

        db.close_connection()


if __name__ == '__main__':
    db = DataBase()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
