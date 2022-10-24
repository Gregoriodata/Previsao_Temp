import time
from schedule import every, repeat, run_pending
import requests
import json
import pyodbc
from datetime import date, datetime

#ab = 0
# while ab <= 3:


@repeat(every(1).hour)
def fazer():
    dados_conexao = (
        "Driver={SQL Server};"  # Drive do banco utilizado.
        "Server=DESKTOP-NQ82MK2;"  # CMD HOSTNAME
        "Database=PRE_TEMPO;")  # Nome do Banco de dados
    conexao = pyodbc.connect(dados_conexao)
    print("Conexao com o banco realizada com sucesso")
    data = datetime.today().replace(microsecond=0)
    idi = 'pt_br'
    itoken = '95bad896508cf4e07d03dcbe6b0ee65c'
    a = ('Curitiba', 'Brasilia', 'Maranhão')
    for icity in a:
        icity = icity.upper()
        try:
            iurl = f'https://api.openweathermap.org/data/2.5/weather?q={icity}&appid={itoken}&lang={idi}'
            requisicao = requests.request("GET", iurl)
            iretorno_req = json.loads(requisicao.text)
            print(iretorno_req['cod'])
            clima = iretorno_req['weather'][0]['description']
            temperatura = round(iretorno_req['main']['temp'] - 273.15, 1)
        except:
            exit(
                print("Erro de Conexao, API não está respondendo, o programa será finalizado"))
        print(
            f'A Cidade de {icity},no data {data}, apresenta céu {clima}, com temperatura em {temperatura}')
        cursor = conexao.cursor()
        comando = f"""INSERT INTO PREVI_TEMPO(CIDADE,DATA,TEMPERATURA,CLIMA)
        VALUES('{icity}','{data}','{temperatura}','{clima}')"""
        # print(comando)
        cursor.execute(comando)
        cursor.commit()
    print("Seus dados foram salvos com sucesso")
    # schedule.every().day.at("10:26").do(fazer)
    # schedule.every(60).seconds.do(fazer) #Funciona
    # schedule.every(1).minutes.do(fazer)  # Funciona.
    # Funciona.

    # while True:
    #     run_pending()
    #     #print(ab)
    #     time.sleep(1)
    #     #ab = ab + 1"


while True:
    run_pending()
    time.sleep(2)
print("Processo finalizado")
