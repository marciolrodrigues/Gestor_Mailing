import datetime


def calcula_tempo(lista_clientes, consultados=0):
    hora_atual = datetime.datetime.now()
    min_totais = ((len(lista_clientes) - consultados) / 3) - 1
    hora_final = hora_atual + datetime.timedelta(minutes=min_totais)
    return hora_final.strftime("%H:%M")
