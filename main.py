import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import pandas as pd
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.bt_checar.clicked.connect(self.consulta_base)

    def consulta_base(self):
        clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
        lista = clientes_df['CNPJ'].astype(str).str.zfill(14).tolist()
        tempo_extracao = (len(lista) / 3) - 1
        self.lbl_infos.setText(f'O arquivo possui {str(len(lista))} CNPJ(s)\n'
                               f'O processo vai demorar cerca de {tempo_extracao:,.0f} minuto(s)    ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


