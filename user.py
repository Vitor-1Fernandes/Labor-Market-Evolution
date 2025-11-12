import requests

def getData(title):

    # Define um agente para autilizar a API sem bloqueio na requisição
    header = {"User-Agent": "VitorLaborMarketData/1.0 (vitorfernandes11122006@gmail.com)"}

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
    def getProps(url, params, header, title):
        rawData = requests.get(url, params=params, headers=header)
        try:
            data = rawData.json()
            wikiPage = list(data["query"]["pages"].keys())
            wikiData = data["query"]["pages"][str(wikiPage[0])]["pageprops"]["wikibase_item"]
            return(wikiData)
        except:
            print(title, " não foi encontrado na Wikipedia")

    # dataRequest busca os dados utilizando a id retornada pela getProps
    def dataRequest(url, params, header, wikiDataId, title):

        # Dicionário que receberá os dados
        dataDict = {
            "Country": title,
            "Gross Domestic Product":"", 
            "Human Development Index":"",
            "Unemployement Rate":"",
            "Retirement Age":"",
            "Population":"",
        }

        rawData = requests.get(url, params=params, headers=header)

        data = rawData.json()
        try:
            dataDict["Gross Domestic Product"] = int(data["entities"][wikiDataId]["claims"]["P2131"][0]['mainsnak']['datavalue']['value']['amount'])
        except:
            pass
        try:
            dataDict["Human Development Index"] = float(data["entities"][wikiDataId]["claims"]["P1081"][-1]["mainsnak"]["datavalue"]["value"]["amount"])
        except:
            pass
        try:
            dataDict["Unemployement Rate"] = float(data["entities"][wikiDataId]["claims"]["P1198"][-1]["mainsnak"]["datavalue"]["value"]["amount"])
        except:
            pass
        try:
            dataDict["Retirement Age"] = int(data["entities"][wikiDataId]["claims"]["P3001"][0]["mainsnak"]["datavalue"]["value"]["amount"])
        except:
            pass
        try:
            dataDict["Population"] = int(data["entities"][wikiDataId]["claims"]["P1082"][-1]["mainsnak"]["datavalue"]["value"]["amount"])
        except:
            pass
        return dataDict
    
    # API para requisição dos dados
    urlData = "https://www.wikidata.org/w/api.php"
    # Configuração da busca dos dados
    wikiDataId = getProps(url, params, header, title)
    paramsData = {
        "action": "wbgetentities",
        "ids": wikiDataId,
        "format": "json",
        "props": "claims"
    }

    return(dataRequest(urlData, paramsData, header, wikiDataId, title))


def buscaPaises(listNames, willPrint):
    dictCountries = {}
    for countries in listNames:
        dictCountries[countries] = (getData(countries))
    if (willPrint):
        print(dictCountries)
    return dictCountries


listCountries = ["Brasil", "Argentina", "Peru", "Chile", "México", "Canadá", "Estados Unidos", "Cuba", "Alemanha", "França", "Itália", "Espanha", "China", "Japão", "Índia", "Coreia do Sul", "Egito", "África do Sul", "Nigéria", "Angola"]

def ApresentaDado(dict, prop):
    for keys in dict.keys():
        data = dict[keys][prop] 
        try:
            print(f"{keys} - População = {int(data)}")
        except:
            print(f"{keys} não possui essa informação registrada na wikpedia")


def ApresentaPais(dict, prop):
    for keys in dict.keys():
        if keys.lower() == prop.lower():
            return print(f"\n {dict[keys]}\n")
    return print(prop, "não foi encontrado na lista de países")

def userInput(listCountries):
    listChoice = input("Você deseja criar uma lista de países?\nInsira sua resposta \n1-Sim\n2-Não\n ")

    if listChoice == "1":
        listCountries = input("\nInsira o nome dos países separados por vírgulas e sem espaço\n").split(',')

    choice = input("\nQual função você deseja testar?\n1-ApresentaPais()\n2-ApresentaDado()\n ")
    if choice == "1":
        prop = input("\n Insira o nome de um país presente na lista de países\n para visualizar todos os dados disponíveis \n")
        dict = buscaPaises(listCountries, False)
        ApresentaPais(dict, prop)
    if choice == "2":
        prop = input("\n Selecione uma das opções abaixo para visualizar todos os dados disponíveis \n1-Gross Domestic Product\n2-Human Devlopment Index\n3-Unemployement Rate\n4-Retirement Age\n5-Population\n ")
        if prop == "1":
            prop ="Gross Domestic Product"
        if prop == "2":
            prop ="Human Devlopment"
        if prop == "3":
            prop ="Unemployement Rate"
        if prop == "4":
            prop ="Retirement Age"
        if prop == "5":
            prop ="Population"
        dict = buscaPaises(listCountries, False)
        ApresentaDado(dict, prop)


userInput(listCountries)