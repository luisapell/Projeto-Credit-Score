# Credit Score 

## Resumo do Projeto  
O projeto tem como objetivo criar um modelo de Machine Learning para o score de crédito. As etapas foram: 

## 1. Dados do projeto 
Trata-se de um problema de credit scoring para cartão de crédito: utilizando uma amostra de 15 safras coletadas entre janeiro de 2015 e março de 2016, na tentativa de prever a inadimplência do cliente ou que não pagará suas dívidas. Os clientes inadimplentes são marcados como "maus" no conjunto de dados.

## 2. Exploração dos dados
Os dados coletados são explorados para entender sua estrutura, distribuição, correlações e possíveis padrões; envolvendo a análise estatística dos dados, visualização de gráficos e identificação de insights relevantes. 

## 3. Limpeza e pré-processamento 
Nesta fase os dados são submetidos a um processo de tratamento. Esse tratamento envolve a eliminação de dados faltantes, codificação de variáveis categóricas, normalizar ou padronizar variáveis numéricas, identificar e tratar outliers, etc. 

## 4. Modelo
Após o tratamento dos dados, foi utilizado a ferramenta Pycaret para o treinamento adequado do modelo e ajuste de hiperparâmetros. O algoritmo de machine learning escolhido foi o Light Gradient Boosting Machine devido ao seu bom desempenho e baixo custo computacional.

Para detalhes do projeto, clique [aqui](https://github.com/luisapell/Projeto-Credit-Score/blob/main/Desenvolvimento.ipynb) 

## 5. Deploy do modelo
Após o treinamento, ajuste e validação do modelo, criamos a implementação no Streamlit, desenvolvido na intenção de receber os dados, realizar as previsões e retornar um arquivo excel.

[streamlit-app_pycaret-2024-10-10-23-10-42.webm](https://github.com/user-attachments/assets/d8fea3fb-ddce-448f-bc9e-ce8a9704331d)


