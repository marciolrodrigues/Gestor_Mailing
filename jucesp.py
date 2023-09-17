from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


def consulta_jucesp(data_inicio, data_final, cidade, capital_min, capital_max):

    # entrar em https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx?IDProduto=
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx?IDProduto=')

    # preencher a data inicial, data final e cidade

    lista_cnpjs = []
    if data_inicio:
        campo_inicio = driver.find_element(By.XPATH,
                                           '//input[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaInicio"]')
        campo_inicio.send_keys(data_inicio)
    if data_final:
        campo_final = driver.find_element(By.XPATH, '//input[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaFim"]')
        campo_final.send_keys(data_final)
    if cidade:
        campo_cidade = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtMunicipio"]')
        campo_cidade.send_keys(cidade)
    if capital_min != '':
        campo_capital_min = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtCapitalMin"]')
        campo_capital_min.send_keys(capital_min)
    if capital_max != '':
        campo_capital_max = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtCapitalMax"]')
        campo_capital_max.send_keys(capital_max)

    botao_pesquisar = driver.find_element(By.XPATH, '//input[@id="ctl00_cphContent_frmBuscaAvancada_btPesquisar"]')
    botao_pesquisar.click()
    achou_registros_totais = True
    while achou_registros_totais:
        try:
            registros_totais = driver.find_element(By.XPATH,
                                                   '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblDocCount"]')
            registros_totais = registros_totais.text
            achou_registros_totais = False
        except:
            sleep(5)
    conta_pagina = 0
    lista_nires = driver.find_elements(By.XPATH,
                                       '//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]//td[contains(@class, "item01")]')
    ultimo_pagina_atual = driver.find_element(By.XPATH,
                                              '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]')

    while ultimo_pagina_atual != registros_totais:
        for nire in range(len(lista_nires)):
            cnpj = ''
            while cnpj == '':
                try:
                    lista_nires = driver.find_elements(By.XPATH,'//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]//td[contains(@class, "item01")]')
                    try:
                        print(lista_nires[nire].text)
                    except IndexError:
                        driver.close()
                        return lista_cnpjs
                    # print(f'posição numero {nire + 1} de um total de {len(lista_nires)}')
                    lista_nires[nire].click()
                    sleep(2)
                    cnpj = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_frmPreVisualiza_lblCnpj"]')
                    cnpj = cnpj.text
                    break
                except:
                    sleep(1)
            lista_cnpjs.append(cnpj)
            cnpj = ''
            driver.back()
            while True:
                try:
                    valida_pagina = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]/tbody/tr[1]/th[1]/span').text
                    if valida_pagina == 'NIRE':
                        break
                except:
                    sleep(1)
            for x in range(conta_pagina):
                while True:
                    try:
                        try:
                            botao_proxima_pagina = driver.find_element(By.XPATH,'//*[@id="ctl00_cphContent_gdvResultadoBusca_pgrGridView_btrNext_lbtText"]')
                        except:
                            break
                        pagina_antes = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
                        botao_proxima_pagina.click()
                        pagina_depois = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
                        while pagina_antes == pagina_depois:
                            sleep(1)
                            pagina_depois = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]').text
                        break
                    except:
                        sleep(1)
            while True:
                try:
                    lista_nires = driver.find_elements(By.XPATH,'//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]//td[contains(@class, "item01")]')
                    break
                except:
                    sleep(1)
        conta_pagina += 1

        ultimo_pagina_atual = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_gdvResultadoBusca_ifbGridView_lblLastDoc"]')
        ultimo_pagina_atual = ultimo_pagina_atual.text
        if ultimo_pagina_atual < registros_totais:
            for x in range(conta_pagina):
                while True:
                    try:
                        botao_proxima_pagina = driver.find_element(By.XPATH, '//*[@id="ctl00_cphContent_gdvResultadoBusca_pgrGridView_btrNext_lbtText"]')
                        botao_proxima_pagina.click()
                        break
                    except Exception as error:
                        print(error)
            while True:
                try:
                    lista_nires = driver.find_elements(By.XPATH,'//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]//td[contains(@class, "item01")]')
                    break
                except:
                    sleep(1)
    driver.close()
    return lista_cnpjs
