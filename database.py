import sqlite3


class DataBase:

    def __init__(self, name='system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresas(

            ABERTURA TEXT,
            SITUACAO TEXT,
            TIPO TEXT,
            NOME TEXT,
            PORTE TEXT,
            NATUREZA_JURIDICA TEXT,
            ATIVIDADE_PRINCIPAL TEXT,
            ATIVIDADES_SECUNDARIAS TEXT,
            QSA TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            MUNICIPIO TEXT,
            BAIRRO TEXT,
            UF TEXT,
            CEP TEXT,
            EMAIL TEXT,
            TELEFONE TEXT,
            DATA_SITUACAO TEXT,
            CNPJ TEXT,
            ULTIMA_ATUALIZACAO TEXT,
            STATUS TEXT,
            FANTASIA TEXT,
            COMPLEMENTO TEXT,
            EFR TEXT,
            MOTIVO_SITUACAO TEXT,
            SITUACAO_ESPECIAL,
            DATA_SITUACAO_ESPECIAL TEXT,
            CAPITAL_SOCIAL TEXT,

            PRIMARY KEY(CNPJ)
            );




        """)

    def register_company(self, fulldataset):

        campos_tabela = ('ABERTURA', 'SITUACAO', 'TIPO', 'NOME', 'PORTE', 'NATUREZA_JURIDICA', 'ATIVIDADE_PRINCIPAL',
                         'ATIVIDADES_SECUNDARIAS', 'QSA', 'LOGRADOURO', 'NUMERO', 'MUNICIPIO', 'BAIRRO', 'UF', 'CEP',
                         'EMAIL', 'TELEFONE', 'DATA_SITUACAO', 'CNPJ', 'ULTIMA_ATUALIZACAO', 'STATUS', 'FANTASIA',
                         'COMPLEMENTO', 'EFR', 'MOTIVO_SITUACAO', 'SITUACAO_ESPECIAL', 'DATA_SITUACAO_ESPECIAL',
                         'CAPITAL_SOCIAL')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela}
            VALUES({qntd})""", fulldataset)
            self.connection.commit()
            return "OK"
        except:
            return "Erro"

    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_companies(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{id}' ")

            self.connection.commit()

            return "Cadastro de empresa excluido com sucesso!"
        except:
            return "Erro ao Excluir registro!"

    # def update_company(self, fulldataset):
    #
    #     cursor = self.connection.cursor()
    #     cursor.execute(f""" UPDATE Empresas set
    #
    #         CNPJ = '{fulldataset[0]}',
    #         NOME = '{fulldataset[1]}',
    #         LOGRADOURO = '{fulldataset[2]}',
    #         NUMERO = '{fulldataset[3]}',
    #         COMPLEMENTO = '{fulldataset[4]}',
    #         BAIRRO = '{fulldataset[5]}',
    #         MUNICIPIO = '{fulldataset[6]}',
    #         UF = '{fulldataset[7]}',
    #         CEP = '{fulldataset[8]}',
    #         TELEFONE = '{fulldataset[9]}',
    #         EMAIL = '{fulldataset[10]}'
    #
    #         WHERE CNPJ = '{fulldataset[0]}'""")
    #
    #     self.connection.commit()