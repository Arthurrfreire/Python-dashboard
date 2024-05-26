## Análise do Dataset de Vinhos
Este projeto Dash explora as relações entre diversos ingredientes usados na criação de três tipos diferentes de vinhos (classe_0, classe_1 e classe_2).

## Demostração

![](https://i.imgur.com/fXt1vtz.png)

## Funcionalidades

 - Gráfico de Dispersão Interativo: Visualize a relação entre dois ingredientes selecionados. Escolha quais ingredientes exibir nos eixos X e Y e se deseja codificar as cores por tipo de vinho.
 - Gráfico de Barras Comparativo: Compare a média dos ingredientes selecionados em cada tipo de vinho. Escolha quais ingredientes incluir na análise.

## Como Usar

**Selecione os Ingredientes:**

 - **Gráfico de Dispersão:** Use os menus suspensos para escolher os ingredientes para os eixos X e Y. Marque a caixa "Color-Encode" para colorir os pontos por tipo de vinho.
 - **Gráfico de Barras:** Use o menu suspenso de múltipla seleção para escolher os ingredientes a serem comparados.

## Explore os Gráficos:

 - **Gráfico de Dispersão:** Observe a distribuição dos pontos e as relações entre os ingredientes. Cores diferentes podem indicar diferentes tipos de vinho.
 - **Gráfico de Barras:** Analise as médias de cada ingrediente para os diferentes tipos de vinho. Identifique quais ingredientes são mais predominantes em cada tipo.

## Estrutura do Código

 - **load_data():** Carrega o dataset de vinhos e o prepara para análise.
 - **create_scatter_chart():** Cria o gráfico de dispersão interativo.
 - **create_bar_chart():** Cria o gráfico de barras comparativo.
 - **Widgets:** Menus suspensos e caixa de seleção para interação do usuário.
 - **Layout do App:** Estrutura a interface do usuário com os gráficos e widgets.
 - **Callbacks:** Atualizam os gráficos dinamicamente com base nas seleções do usuário.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

 - pandas
 - plotly
 - scikit-learn
- dash

## Como Executar

1. **Clone este repositório.**
   
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   
3. **Execute o app:**
   ```bash
   python app.py

4. Abra o navegador e acesse http://127.0.0.1:8050/

## Observações
Os dados utilizados neste projeto são do dataset de vinhos do scikit-learn.
Este é um exemplo simples de aplicação Dash. Você pode personalizar e expandir as funcionalidades para análises mais complexas.

Divirta-se explorando os dados dos vinhos! 🍷
