import requests
import json
import array


def cid():
    iurl = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    requisicao = requests.request("GET", iurl)
    print(requisicao)
    retorno_req = json.loads(requisicao.text)
    # print(retorno_req)
    #cit = (retorno_req[0])
    # print(cit)

    # print(retorno_req[0:]['nome'])
    estados = []
    if estados is not None:
        for i in retorno_req:
            estados.append(i['nome'])
    print(estados)
    return estados
