import requests

# Define um agente para autilizar a API sem bloqueio na requisição
header = {"User-Agent": "VitorLaborMarketData/1.0 (vitorfernandes11122006@gmail.com)"}

# Título da página que será buscada na wikipedia
title = "Peru"

# Link para utilização da API
url = "https://pt.wikipedia.org/w/api.php"

# Configuração da busca
params = {
    "action": "query",
    "format": "json",
    "prop": "pageprops",
    "titles": title,
    "exintro": True,
    "explaintext": 1,
}


# getProps acessa a página da wikipedia e retorna a id para buscarmos os dados em outra requisição
def getProps(url, params, header):
    rawData = requests.get(url, params=params, headers=header)
    try:
        data = rawData.json()
        wikiPage = list(data["query"]["pages"].keys())
        wikiData = data["query"]["pages"][str(wikiPage[0])]["pageprops"]["wikibase_item"]
        return(wikiData)
    except:
        print("Deu Erro", rawData)

# dataRequest busca os dados utilizando a id retornada pela getProps
def dataRequest(url, params, header, wikiDataId):
    rawData = requests.get(url, params=params, headers=header)
    try:
        data = rawData.json()
        print(data["entities"][wikiDataId]["claims"]["P2131"][0]['mainsnak']['datavalue']['value']['amount'])
    except:
        print("Deu Erro", rawData)

# API para requisição dos dados
urlData = "https://www.wikidata.org/w/api.php"
# Configuração da busca dos dados
wikiDataId = getProps(url, params, header)
paramsData = {
    "action": "wbgetentities",
    "ids": wikiDataId,
    "format": "json",
    "props": "claims"
}

dataRequest(urlData, paramsData, header, wikiDataId)


