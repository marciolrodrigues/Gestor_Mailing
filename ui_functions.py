import requests
import json


def extrair_clientes(lista_cnpj):
    campos = ('abertura', 'situacao', 'tipo', 'nome', 'porte', 'natureza_juridica', 'atividade_principal',
              'atividades_secundarias', 'qsa', 'logradouro', 'numero', 'municipio', 'bairro', 'uf',
              'cep', 'email', 'telefone', 'data_situacao', 'cnpj', 'ultima_atualizacao', 'status', 'fantasia',
              'complemento', 'efr', 'motivo_situacao', 'situacao_especial', 'data_situacao_especial',
              'capital_social')
    campos_variaveis = ('atividade_principal', 'atividades_secundarias', 'qsa')

    resultado = []
    lista_retorno = []
    lista_final = []

    for cliente in lista_cnpj:
        try:
            url = f"https://www.receitaws.com.br/v1/cnpj/{cliente}"
            querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
            response = requests.request("GET", url, params=querystring)
        except requests.exceptions.ConnectionError:
            return 'internet'

        if response.status_code == 429:
            return response.status_code

        resp = json.loads(response.text)

        if resp['status'] != 'OK':
            resultado.append([cliente, resp['message']])
        else:
            resultado.append([cliente, resp['status']])

            for item in campos:
                if item in campos_variaveis:
                    agrupador = ''
                    contagem = 0
                    for retorno in resp[f'{item}']:
                        if contagem == 0:
                            chaves = list(retorno.keys())
                            agrupador = retorno[f'{chaves[0]}'] + ' -> ' + retorno[f'{chaves[1]}']
                        else:
                            agrupador = agrupador + ' + ' + retorno[f'{chaves[0]}'] + ' -> ' + retorno[f'{chaves[1]}']
                        contagem += 1
                    lista_retorno.append(agrupador)
                else:
                    lista_retorno.append(resp[f'{item}'])

            lista_final.append(lista_retorno)
            lista_retorno = []

    return lista_final, resultado
