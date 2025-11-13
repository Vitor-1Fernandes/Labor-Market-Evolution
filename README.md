## 🇧🇷 Análise de Dados Socioeconômicos Globais

Este projeto em Python é uma ferramenta para coletar e analisar dados socioeconômicos de diversos países, utilizando as APIs da Wikipedia e do Wikidata. O código extrai indicadores chave e realiza análises estatísticas básicas para fornecer uma visão rápida do perfil de cada nação.

-----

## 🛠️ Funcionalidades

O script é dividido em módulos de coleta, manipulação e análise de dados, oferecendo as seguintes funcionalidades:

1.  **Coleta de Dados:** Extrai dados de países a partir do **Wikidata**, utilizando o nome do país como ponto de partida (via Wikipedia).
2.  **Indicadores Coletados:**
      * **Produto Interno Bruto** (`P2131`)
      * **Índice de Desenvolvimento Humano** (`P1081`)
      * **Taxa de Desemprego** (`P1198`)
      * **Idade de Aposentadoria** (`P3001`)
      * **População** (`P1082`)
3.  **Análise Estatística:**
      * **Média Aritmética:** Calcula a média simples de qualquer indicador.
      * **Média Ponderada:** Calcula a média de um indicador usando a **População** como peso.
      * **Variância:** Mede a dispersão dos dados em torno da média.
      * **Amplitude:** Determina a diferença entre o maior e o menor valor de um indicador na lista.
4.  **Interação com o Usuário:** Permite ao usuário escolher entre uma lista padrão de países ou fornecer sua própria lista, e selecionar qual função de análise executar.

-----

## ⚙️ Como Usar

### Pré-requisitos

O único requisito é a biblioteca `requests`, utilizada para fazer requisições HTTP para as APIs.

```bash
pip install requests
```

### Execução

1.  Salve o código como um arquivo Python (ex: `analise_paises.py`).

2.  Execute o arquivo no seu terminal:

    ```bash
    python analise_paises.py
    ```

3.  O programa guiará você com um menu de opções:

      * Escolha se deseja usar a lista padrão de países ou inserir uma nova lista.
      * Selecione a função de análise desejada (ex: `ApresentaDado()`, `ApresentaMedia()`).
      * Selecione o indicador para o qual a análise deve ser feita (ex: "Population", "Human Development Index").

-----

## 📂 Estrutura do Código

| Função | Descrição |
| :--- | :--- |
| `getData(title)` | Função principal que faz a requisição em duas etapas (Wikipedia e Wikidata) para coletar todos os indicadores de um país. |
| `buscaPaises(listNames, willPrint)` | Itera sobre a lista de países, chamando `getData` para cada um e agrupando os resultados em um dicionário. |
| `pegaDado(dict, prop)` | Extrai uma lista de valores e nomes de países para uma propriedade específica do dicionário principal. |
| `ApresentaDado(dict, prop)` | Exibe o valor de um indicador para cada país na lista. |
| `MediaPonderada(dict, prop)` | Calcula e exibe a média ponderada, utilizando a População como fator de peso. |
| `Variancia(dict, prop)` | Calcula e exibe a taxa de variância do indicador. |
| `Amplitude(dict, prop)` | Calcula e exibe a diferença entre o valor máximo e mínimo. |
| `userInput(listCountries)` | Função de interface do usuário para gerenciar as escolhas de lista de países e função de análise. |