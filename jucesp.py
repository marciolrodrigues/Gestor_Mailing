from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from winotify import Notification


notificacao = Notification(app_id='Gestor de Mailing', title='Digitação do CAPTCHA',
                           msg='Digite o CAPTCHA no navegador para continuar a extração')


def consulta_jucesp(driver, lista_nires):
    lista_cnpjs = []
    driver.find_element(By.XPATH, '//*[@id="row"]/div/div/div/ul/li[1]/a').click()

    for nire in lista_nires:
        campo_digitar = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmBuscaSimples_txtPalavraChave"]')
        campo_digitar.send_keys(nire)

        driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmBuscaSimples_btPesquisar"]').click()

        # confirma se já abriu a página com os dados da empresa através do campo CNPJ
        while True:
            try:
                cnpj = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmPreVisualiza_lblCnpj"]')
                cnpj = cnpj.text
                break
            except:
                sleep(1)
        lista_cnpjs.append(cnpj)

        driver.find_element(By.XPATH, '//*[@id="row"]/div/div/div/ul/li[1]/a').click()

        while True:
            try:
                campo_digitar = driver.find_element(By.XPATH,
                                                    '//*[@id="ctl00_cphContent_frmBuscaSimples_txtPalavraChave"]')
                break
            except:
                driver.find_element(By.XPATH, '//*[@id="row"]/div/div/div/ul/li[1]/a').click()
    driver.close()
    return lista_cnpjs


def extrair_nires(data_inicio, data_final, cidade, capital_min, capital_max):

    # entrar em https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx?IDProduto=
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx?IDProduto=')

    lista_nires = []

    # preencher a data inicial, data final e cidade

    if data_inicio:
        campo_inicio = driver.find_element(By.XPATH,
                                           '//input[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaInicio"]')
        campo_inicio.send_keys(data_inicio)
    if data_final:
        campo_final = driver.find_element(By.XPATH,
                                          '//input[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaFim"]')
        campo_final.send_keys(data_final)
    if cidade:
        campo_cidade = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtMunicipio"]')
        campo_cidade.send_keys(cidade)
    if capital_min != '':
        campo_capital_min = driver.find_element(By.XPATH,
                                                '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtCapitalMin"]')
        campo_capital_min.send_keys(capital_min)
    if capital_max != '':
        campo_capital_max = driver.find_element(By.XPATH,
                                                '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtCapitalMax"]')
        campo_capital_max.send_keys(capital_max)

    botao_pesquisar = driver.find_element(By.XPATH, '//input[@id="ctl00_cphContent_frmBuscaAvancada_btPesquisar"]')
    botao_pesquisar.click()

    notificacao.show()

    # resgatando a quantidade total de registros da consulta
    while True:
        try:
            registros_totais = driver.find_element(By.XPATH,
                                                   '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblDocCount"]')
            break
        except:
            sleep(1)
    registros_totais = registros_totais.text

    # resgatando a lista de itens da página atual e número do último item da página atual
    while True:
        try:
            nires = driver.find_elements(By.XPATH,
                                         '//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]//td[contains(@class, "item01")]')
            ultimo_pagina_atual = driver.find_element(By.XPATH,
                                                      '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
            break
        except:
            sleep(1)

    # se tiver pelo menos 1 item listado na página, recupera os itens na lista
    if len(nires) > 0:
        for item in nires:
            lista_nires.append(item.text)

    # recupera a lista de nires de cada página até que chegue na última
    while True:
        # confirma se existe um botão próximo, se não existir, é porque já está na última pagina
        tem_proxima_pagina = False
        try:
            botao_proxima_pagina = driver.find_element(By.XPATH,
                                                       '//*[@id="ctl00_cphContent_gdvResultadoBusca_pgrGridView_btrNext_lbtText"]')
            tem_proxima_pagina = True
        except:
            break

        while True:
            try:
                pagina_antes = driver.find_element(By.XPATH,
                                           '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
                break
            except:
                sleep(1)

        # se tem outra página, clica no próximo e recupera a lista de intens
        if tem_proxima_pagina: #TODO tem que rever isso aqui
            while True:
                try:
                    botao_proxima_pagina.click()
                    while True:
                        try:
                            pagina_depois = driver.find_element(By.XPATH,
                                                                '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
                            break
                        except:
                            sleep(1)
                    while pagina_antes == pagina_depois:
                        sleep(1)
                        pagina_depois = driver.find_element(By.XPATH,
                                                            '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
                    break
                except:
                    sleep(1)
            nires = pega_nires(driver)
            for item in nires:
                lista_nires.append(item.text)

    return consulta_jucesp(driver, lista_nires)


def pega_nires(driver):
    while True:
        try:
            nires = driver.find_elements(By.XPATH,
                                         '//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]//td[contains(@class, "item01")]')
            break
        except:
            sleep(1)
    return nires

if __name__ == '__main__':
    inicio = '21/09/2023'
    fim = '21/09/2023'
    cid = 'campinas'
    cap_ini = ''
    cap_fin = ''
    extrair_nires(inicio, fim, cid, cap_ini, cap_fin)