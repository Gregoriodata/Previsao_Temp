import requests
import json
idi = 'pt_br'
itoken = '95bad896508cf4e07d03dcbe6b0ee65c'
icity = input('Informe o nome de uma cidade: ')
icity = icity.upper()
iurl = f'https://api.openweathermap.org/data/2.5/weather?q={icity}&appid={itoken}&lang={idi}'

requisicao = requests.request("GET", iurl)
iretorno_req = json.loads(requisicao.text)
descri = iretorno_req['weather'][0]['description']
temp = iretorno_req['main']['temp'] - 273.15

print(f'Cidade de {icity}, apresenta céu {descri}, com temperatura em {temp}')
