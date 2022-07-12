# código de geração do gráfico 

import pandas as pd
import matplotlib as plt
import seaborn as sns


df = pd.read_csv('gasolina.csv')

figura = sns.lineplot(x='dia', y='venda', data=df, legend=False, markers=True)

figura.set(xlabel='Dia', ylabel='Valor', title='Variação do Preço da Gasolina!')
figura.figure.savefig("gasolina.png")

#como já havia colocado essas informações na versão anterior, fiz pequenas alteraçoes e adicionei este comentário
