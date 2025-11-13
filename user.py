import requests

def getData(title):

    header = {"User-Agent": "VitorLaborMarketData/1.0 (vitorfernandes11122006@gmail.com)"}

    url = "https://pt.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "pageprops",
        "titles": title,
        "exintro": True,
        "explaintext": 1,
    }

    def getProps(url, params, header, title):
        rawData = requests.get(url, params=params, headers=header,  verify=False)
        try:
            data = rawData.json()
            wikiPage = list(data["query"]["pages"].keys())
            wikiData = data["query"]["pages"][str(wikiPage[0])]["pageprops"]["wikibase_item"]
            return(wikiData)
        except:
            print(title, " não foi encontrado na Wikipedia")

    def dataRequest(url, params, header, wikiDataId, title):

        dataDict = {
            "Country": title,
            "Gross Domestic Product":"", 
            "Human Development Index":"",
            "Unemployement Rate":"",
            "Retirement Age":"",
            "Population":"",
        }

        rawData = requests.get(url, params=params, headers=header,  verify=False)

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
    
    urlData = "https://www.wikidata.org/w/api.php"

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

def pegaDado(dict, prop):
    dataList = []
    nameCountries = []
    for keys in dict.keys():
        dataList.append(dict[keys][prop]) 
        nameCountries.append(keys)
    return dataList, nameCountries

def soma(data):
    result = 0
    for num in data:
        result = result + num
    return result

def ApresentaPais(dict, prop):
    for keys in dict.keys():
        if keys.lower() == prop.lower():
            return print(f"\n {dict[keys]}\n")
    return print(prop, "não foi encontrado na lista de países")

def ApresentaDado(dict, prop):
        dataList = pegaDado(dict, prop)[0]
        nameCountries = pegaDado(dict, prop)[1]
        for count in range(len(dataList)):
            if dataList[count] != "" and dataList[count] != " " and dataList[count] != None:
                print(f"{nameCountries[count]} - {prop} = {(dataList[count]):,}")

            else: print(f"{nameCountries[count]} não possui essa informação registrada na wikpedia")

def ApresentaMedia(dict, prop, willPrint=True):
    rawDataList = pegaDado(dict, prop)[0]
    dataList = []
    for count in range(len(rawDataList)):
        if rawDataList[count] != "" and rawDataList[count] != " " and rawDataList[count] != None:
            dataList.append(float(rawDataList[count]))
    if (willPrint):
        try:
            print(f'A média do indicador {prop} entre os países da lista é {(soma(dataList)/len(dataList)):,.2f}\n{len(dataList)} de {len(rawDataList)} paises possuem {prop} registrado')
        except ZeroDivisionError:
            print("Não foi possível captar informações suficientes sobre os países selecionados, impossibilitando o cálculo dessa função")
            quit()
    else:
        try:
            media=soma(dataList)/len(dataList)
            return(media, dataList)
        except ZeroDivisionError:
            print("Não foi possível captar informações suficientes sobre os países selecionados, impossibilitando o cálculo dessa função")
            quit()

def MediaPonderada(dict, prop):
    rawDataList = pegaDado(dict, prop)[0]
    popList = pegaDado(dict, "Population")[0]
    popNewList = []
    dataList = []
    for count in range(len(rawDataList)):
        if rawDataList[count] != "" and rawDataList[count] != " " and rawDataList[count] != None:
            dataList.append(float(rawDataList[count]) * float(popList[count]))
            popNewList.append(float(popList[count]))
    dataListSoma = soma(dataList)
    divisor = soma(popNewList)
    try:
        print(f"a Média Ponderada de {prop}, com peso relativo à população é {dataListSoma/divisor:,.2f}")
    except ZeroDivisionError:
        print("Não foi possível captar informações suficientes sobre os países selecionados, impossibilitando o cálculo dessa função")
        quit()

def Variancia(dict, prop):
    media, rawDataList = ApresentaMedia(dict, prop, willPrint=False)
    dataListList = []
    dataList = 0

    countValues = 0
    for values in range(len(rawDataList)):
        if (rawDataList[values] == "" or rawDataList[values] == " " or rawDataList[values] == None):
            pass
        else: 
            dataListList.append(rawDataList[values])
            countValues += 1

    for count in range(len(dataListList)):
            dataList = dataList + (float((dataListList[count] - media)**2))
    print(f" A taxa de variância do indicador {prop} é de {dataList/countValues:.2f} entre os países selecionados")

def Amplitude(dict, prop):
    rawDataList = pegaDado(dict, prop)[0]
    nameList = pegaDado(dict, prop)[1]
    dataList = []
    dataListNames = []

    countValues = 0
    for values in range(len(rawDataList)):
        if (rawDataList[values] == "" or rawDataList[values] == " " or rawDataList[values] == None):
            pass
        else: 
            dataList.append(rawDataList[values])
            dataListNames.append(nameList[values])
            countValues += 1
        
    if countValues < 2:
        print("Não foi possível captar informações suficientes sobre os países selecionados, impossibilitando o cálculo dessa função")
        quit()

    biggest = max(dataList)
    smallest = min(dataList)

    biggestName = dataListNames[dataList.index(biggest)]
    smallestName = dataListNames[dataList.index(smallest)]

    amplitude = biggest - smallest 

    print(f"A amplitude do indicador {prop} é de {amplitude:,.2f},\nsendo {smallestName} o menor = {smallest:,.2f} e {biggestName} o maior = {biggest:,.2f}")

def functionByChoice(defName, dict):
    choice = input("\n Selecione uma das opções abaixo para visualizar todos os dados disponíveis \n1-Gross Domestic Product\n2-Human Development Index\n3-Unemployement Rate\n4-Retirement Age\n5-Population\n ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        input("\n Selecione uma das opções abaixo para visualizar todos os dados disponíveis \n1-Gross Domestic Product\n2-Human Development Index\n3-Unemployement Rate\n4-Retirement Age\n5-Population\n ")
    if choice == "1":
        choice ="Gross Domestic Product"
    if choice == "2":
        choice ="Human Development Index"
    if choice == "3":
        choice ="Unemployement Rate"
    if choice == "4":
        choice ="Retirement Age"
    if choice == "5":
        choice ="Population"
    if defName == "ApresentaDado":
        ApresentaDado(dict, choice)
    if defName == "ApresentaMedia":
        ApresentaMedia(dict, choice)
    if defName == "MediaPonderada":
        MediaPonderada(dict, choice)
    if defName == "Variancia":
        Variancia(dict, choice)
    if defName == "Amplitude":
        Amplitude(dict, choice)
    

def userInput(listCountries):
    listChoice = input("\nVocê deseja criar uma lista de países?\nInsira sua resposta \n1-Sim\n2-Não\n ")
    while listChoice != "1" and listChoice != "2":
        listChoice = input("Você deseja criar uma lista de países?\nInsira sua resposta \n1-Sim\n2-Não\n ")
    if listChoice == "1":
        listCountries = input("\nInsira o nome dos países separados por vírgulas e sem espaço\n ").split(',')
    choice = input("\nQual função você deseja testar?\n1-ApresentaPais()\n2-ApresentaDado()\n3-ApresentaMedia()\n4-ApresentaMediaPonderada()\n5-Variância()\n6-Amplitude()\n ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        choice = input("\nQual função você deseja testar?\n1-ApresentaPais()\n2-ApresentaDado()\n3-ApresentaMedia()\n4-Apresenta MediaPonderada()\n5-Variância()\n6-Amplitude()\n ")

    if choice == "1":
        prop = input("\n Insira o nome de um país presente na lista de países\n para visualizar todos os dados disponíveis \n")
        dictionary = buscaPaises(listCountries, False)
        ApresentaPais(dictionary, prop)
    if choice == "2":
        dictionary = buscaPaises(listCountries, False)
        functionByChoice("ApresentaDado", dictionary)
    if choice == "3":
        dictionary = buscaPaises(listCountries, False)
        functionByChoice("ApresentaMedia", dictionary)
    if choice == "4":
        dictionary = buscaPaises(listCountries, False)
        functionByChoice("MediaPonderada", dictionary)
    if choice == "5":
        dictionary = buscaPaises(listCountries, False)
        functionByChoice("Variancia", dictionary)
    if choice == "6":
        dictionary = buscaPaises(listCountries, False)
        functionByChoice("Amplitude", dictionary)


userInput(listCountries)