from time import sleep
import datetime
import pandas as pd


def calcula_tempo(lista_clientes, consultados=0):
    hora_atual = datetime.datetime.now()
    min_totais = ((len(lista_clientes) - consultados) / 3) - 1
    hora_final = hora_atual + datetime.timedelta(minutes=min_totais)
    return hora_final.strftime("%H:%M")


def consulta_planilha():
    try:
        clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
        if 'CNPJ' not in clientes_df.columns:
            return f'sem_coluna', []
        if 'STATUS' not in clientes_df.columns:
            clientes_df.insert(clientes_df.columns.get_loc('CNPJ') + 1, 'STATUS', None)
            clientes_df['STATUS'].astype(str)
            clientes_df['CNPJ'].astype(str)
        clientes_df['CNPJ'] = clientes_df['CNPJ'].apply(manter_numeros)
        clientes_df['CNPJ'] = clientes_df['CNPJ'].astype(str).str.zfill(14)
        lista_clientes = clientes_df.loc[clientes_df['STATUS'].isnull(), 'CNPJ'].astype(str).str.zfill(14).tolist()
        ja_processado = clientes_df.loc[clientes_df['STATUS'].notnull()].to_dict(orient='records')
        ja_processado_list = []
        with pd.ExcelWriter('base_cnpj.xlsx', mode='a', if_sheet_exists='replace') as writer:
            clientes_df.to_excel(writer, sheet_name='cnpjs', index=False)
        for item in ja_processado:
            ja_processado_list.append([str(item['CNPJ']), item['STATUS']])

        return lista_clientes, ja_processado_list
    except ValueError:
        return False


def atualiza_planilha(lista_cnpj):
    clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
    clientes_df['CNPJ'] = clientes_df['CNPJ'].astype(str).str.zfill(14)
    if 'STATUS' not in clientes_df.columns:
        clientes_df.insert(clientes_df.columns.get_loc('CNPJ') + 1, 'STATUS', None)
    # for item in lista_cnpj:
    #     if clientes_df.loc[clientes_df['CNPJ'] == item[0]]:
    #         print('Achou')
    #     clientes_df.loc[clientes_df['CNPJ'] == item[0], 'STATUS'] = item[1]

    # clientes_df['CNPJ'] = clientes_df['CNPJ'].apply(numero_para_texto_cnpj)
    dict_clientes = dict(lista_cnpj)
    dict_clientes = {chave.zfill(14): valor for chave, valor in dict_clientes.items()}

    clientes_df['STATUS'] = clientes_df['CNPJ'].map(dict_clientes)

    with pd.ExcelWriter('base_cnpj.xlsx', mode='a', if_sheet_exists='replace') as writer:
        clientes_df.to_excel(writer, sheet_name='cnpjs', index=False)


def numero_para_texto_cnpj(numero):
    return f'{numero:014d}'


def tempo_espera(tempo_inicio):
    tempo_passado = datetime.datetime.now() - tempo_inicio
    segundos_aguardar = datetime.timedelta(seconds=60)
    if tempo_passado > segundos_aguardar:
        return 0
    else:
        return (segundos_aguardar - tempo_passado).seconds


def manter_numeros(texto):
    if type(texto) == str:
        return ''.join(filter(str.isdigit, texto))
    else:
        return texto
