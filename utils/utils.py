import datetime
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def formatar_moeda_data(lista_cadastro):
    lista_cadastro[27] = locale.currency(float(lista_cadastro[27]), grouping=True)
    dataiso = datetime.datetime.fromisoformat(lista_cadastro[19])
    lista_cadastro[19] = dataiso.strftime('%d/%m/%Y')
    return lista_cadastro


def calcula_tempo(lista_clientes, consultados=0):
    hora_atual = datetime.datetime.now()
    min_totais = ((len(lista_clientes) - consultados) / 3) - 1
    hora_final = hora_atual + datetime.timedelta(minutes=min_totais)
    return hora_final.strftime("%H:%M")


def consulta_planilha(consulta_pendentes):
    try:
        clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
        if 'CNPJ' not in clientes_df.columns:
            return f'sem_coluna', []
        if 'STATUS' not in clientes_df.columns:
            clientes_df.insert(clientes_df.columns.get_loc('CNPJ') + 1, 'STATUS', None)
            clientes_df['STATUS'].astype(str)
            clientes_df['CNPJ'].astype(str)
        try:
            notincache_df = pd.read_excel('base_cnpj.xlsx', sheet_name='notincache')
            notincache_list = notincache_df.loc[notincache_df['STATUS'].notnull(), 'CNPJ'].astype(str).str.zfill(14).tolist()
        except:
            nome_aba = 'notincache'
            nova_aba = pd.DataFrame([{'CNPJ': '', 'STATUS': ''}])
            with pd.ExcelWriter('../base_cnpj.xlsx', engine='openpyxl', mode='a') as writer:
                nova_aba.to_excel(writer, sheet_name=nome_aba, index=False)
            notincache_list = []

        clientes_df['CNPJ'] = clientes_df['CNPJ'].apply(manter_numeros)
        clientes_df['CNPJ'] = clientes_df['CNPJ'].astype(str).str.zfill(14)
        lista_clientes = clientes_df.loc[clientes_df['STATUS'].isnull(), 'CNPJ'].astype(str).str.zfill(14).tolist()
        ja_processado = clientes_df.loc[clientes_df['STATUS'].notnull()].to_dict(orient='records')
        ja_processado_list = []
        clientes_df = clientes_df[clientes_df['STATUS'] != 'not in cache']

        notincache_df['CNPJ'] = notincache_df['CNPJ'].astype(str).str.zfill(14)

        clientes_df = clientes_df.drop_duplicates()
        notincache_df = notincache_df.drop_duplicates()

        with pd.ExcelWriter('./base_cnpj.xlsx', mode='a', if_sheet_exists='replace') as writer:
            clientes_df.to_excel(writer, sheet_name='cnpjs', index=False)
            notincache_df.to_excel(writer, sheet_name='notincache', index=False)
        for item in ja_processado:
            ja_processado_list.append([str(item['CNPJ']), item['STATUS']])
        if consulta_pendentes:
            return lista_clientes + notincache_list, ja_processado_list
        else:
            return lista_clientes, ja_processado_list
    except ValueError:
        return False, False


def atualiza_jucesp(lista_cnpj):
    clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
    lista_clientes = clientes_df.to_dict('records')
    for item in lista_cnpj:
        lista_clientes.append({'CNPJ': item})

    clientes_df = pd.DataFrame(lista_clientes)

    clientes_df['CNPJ'] = clientes_df['CNPJ'].astype(str).str.zfill(14)

    with pd.ExcelWriter('./base_cnpj.xlsx', mode='a', if_sheet_exists='replace') as writer:
        clientes_df.to_excel(writer, sheet_name='cnpjs', index=False)


def atualiza_planilha(lista_cnpj, consulta_pendentes):
    notincache_existente = pd.read_excel('base_cnpj.xlsx', sheet_name='notincache')
    clientes_df = pd.read_excel('base_cnpj.xlsx', sheet_name='cnpjs')
    clientes_df['CNPJ'] = clientes_df['CNPJ'].astype(str).str.zfill(14)
    if 'STATUS' not in clientes_df.columns:
        clientes_df.insert(clientes_df.columns.get_loc('CNPJ') + 1, 'STATUS', None)
    # dict_clientes = dict(lista_cnpj)
    # dict_clientes = {chave.zfill(14): valor for chave, valor in dict_clientes.items()}

    # Converta a nova lista em um novo DataFrame
    novos_dados = pd.DataFrame(lista_cnpj, columns=['CNPJ', 'STATUS'])

    # # Defina o CNPJ como índice no novo DataFrame, se necessário
    # novos_dados.set_index('CNPJ', inplace=True)

    # Use a função update para substituir os valores no DataFrame original com base no novo DataFrame
    clientes_df = novos_dados

    # clientes_df['STATUS'] = clientes_df['CNPJ'].map(dict_clientes)
    notincache_df = clientes_df[clientes_df['STATUS'] == 'not in cache']

    if not consulta_pendentes:
        notincache_df = pd.concat([notincache_df, notincache_existente], ignore_index=True)

    notincache_df['CNPJ'] = notincache_df['CNPJ'].astype(str).str.zfill(14)

    clientes_df = clientes_df.drop_duplicates()
    notincache_df = notincache_df.drop_duplicates()

    with pd.ExcelWriter('./base_cnpj.xlsx', mode='a', if_sheet_exists='replace') as writer:
        clientes_df.to_excel(writer, sheet_name='cnpjs', index=False)
        notincache_df.to_excel(writer, sheet_name='notincache', index=False)


def manter_numeros(texto):
    if type(texto) == str:
        return ''.join(filter(str.isdigit, texto))
    else:
        return texto


if __name__ == '__main__':
    print(consulta_planilha())
