# 📊 Análise de Dados Socioeconômicos Globais via API

Este projeto em Python é uma ferramenta robusta para coletar, tratar e analisar dados socioeconômicos de diversos países em tempo real. Utilizando a interoperabilidade entre sistemas, o script consome dados diretamente da **Wikipedia** e do **Wikidata** para transformar informações brutas em insights estatísticos e visuais.

---

## 🛠️ Funcionalidades

O script oferece uma interface interativa para realizar as seguintes operações:

1.  **Coleta Automatizada (Web Scraping/API):** Extrai dados dinâmicos utilizando identificadores específicos do Wikidata.
2.  **Indicadores Suportados:**
    * **Produto Interno Bruto (PIB)**
    * **Índice de Desenvolvimento Humano (IDH)**
    * **Taxa de Desemprego**
    * **Idade de Aposentadoria**
    * **População Total**
3.  **Análise Estatística Avançada:**
    * **Média Aritmética:** Média simples dos indicadores entre os países selecionados.
    * **Média Ponderada:** Cálculo de indicadores (como IDH ou PIB) utilizando a **População** como fator de peso.
    * **Variância:** Medição da dispersão dos dados para entender a desigualdade entre os países.
    * **Amplitude:** Identificação da disparidade entre os valores máximos e mínimos do conjunto.
4.  **Visualização Gráfica:** Geração automática de gráficos de linha com `matplotlib` para facilitar a análise comparativa.

---

## ⚙️ Configuração e Instalação

### Pré-requisitos

Para rodar este projeto, você precisará do Python instalado e das seguintes bibliotecas:

* `requests`: Para comunicação com as APIs.
* `matplotlib`: Para geração dos gráficos.
* `numpy`: Para suporte em cálculos numéricos.

Você pode instalar todas de uma vez com o comando abaixo:

```bash
pip install requests matplotlib numpy