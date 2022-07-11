# código de geração do gráfico 

import pandas as pd
import matplotlib as plt
import seaborn as sns


df = pd.read_csv('gasolina.csv')

figura = sns.lineplot(x='dia', y='venda', data=df)
figura.set(xlabel='Dia', ylabel='Preço', title='Variação do Preço da Gasolina')
figura.figure.savefig("gasolina.png")