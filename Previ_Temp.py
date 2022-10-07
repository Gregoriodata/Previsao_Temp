import requests
import json
import pyodbc
from datetime import date

a = ('Brasília')
data = date.today()
idi = 'pt_br'
itoken = '95bad896508cf4e07d03dcbe6b0ee65c'
icity = a
icity = icity.upper()
iurl = f'https://api.openweathermap.org/data/2.5/weather?q={icity}&appid={itoken}&lang={idi}'
requisicao = requests.request("GET", iurl)
iretorno_req = json.loads(requisicao.text)
descri = iretorno_req['weather'][0]['description']
temp = round(iretorno_req['main']['temp'] - 273.15, 1)
print(
    f'Cidade de {icity}, apresenta céu {descri}, com temperatura em {temp}')
dados_conexao = (
    "Driver={SQL Server};"  # Drive do banco utilizado.
    "Server=DESKTOP-NQ82MK2;"  # CMD HOSTNAME
    "Database=PRE_TEMPO;"  # Nome do Banco de dados
)
conexao = pyodbc.connect(dados_conexao)
print("Conexao com o banco realizada com sucesso")
cursor = conexao.cursor()
comando = f"""INSERT INTO PREV_TEMP(CIDADE,DATA,TEMP,DESCRI)
        VALUES('{icity}','{data}','{temp}','{descri}')"""
print(comando)
cursor.execute(comando)
cursor.commit()
print("Seus dados foram salvos com sucesso")
