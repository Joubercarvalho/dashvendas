from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import openpyxl as op


app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("vendas_cosmeticos_ficticio.xlsx")

#cria o grafico
fig = px.bar(df, x="Produto", y="Quantidade", color="Loja", barmode="group")

#cria a opção de loja
opcoes = list(df['Loja'].unique())
opcoes.append("Todas")

#cria a opção produtos
opcoes_produtos = list(df['Produto'].unique())
opcoes_produtos.append("Todos")

app.layout = html.Div(children=[
    html.H1(children='relatório de vendas'),
    html.H2(children='Gráfico com o faturamento da cada Loja:'),
    html.Div(children='''
        Quantidade de produtos vendidos.
    '''),
    #cria o dropdown
    dcc.Dropdown(opcoes, 'Todas', id='lista_lojas'),
    dcc.Graph(
        id='quantidade_vendas',
        figure=fig
        )
    ])

@app.callback(
    Output('quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="Loja", barmode="group")
    else:
        tabela_filtro = df.loc[df['Loja']==value, :]
        fig = px.bar(tabela_filtro, x="Produto", y="Quantidade", color="Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=False)