import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.lines import lineStyles

dados = {'Materiais': ['Lápis', 'Borracha', 'Canetas','Livros','Cadernos','Tesouras'],
         'Quantidade': [3,4,12,8,8,15]

}

df = pd.DataFrame(dados)

print(df)
print(df['Quantidade'].mean())
print(df['Quantidade'].std())
print(df['Quantidade'].median())
print('Moda:', df['Quantidade'].mode())


#variância populacional
print(df['Quantidade'].var(ddof= 0))

#Quartil

print('Primeiro quartil:', df['Quantidade'].quantile(q=0.25))
print('Segundo quartil:', df['Quantidade'].quantile(q=0.50))
print('Terceiro quartil:', df['Quantidade'].quantile(q=0.75))
print('Amplitude:', df['Quantidade'].max() - df['Quantidade'].min())

print(df.describe())

dados = [3,4,12,8,8,15]

print('Média: ', np.mean(dados))
print('Mediana : ', np.median(dados))
print('Variancia: ', np.var(dados))
print('Desvio padrão: ', np.std(dados))

ax = sns.histplot(dados, stat = 'density', color = 'y', kde=True, lw=1)
plt.show()
