#IMPORTAÇÃO DAS BIBLIOTECAS:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#LEITURA ARQUIVO BASE:
df_original = pd.read_csv('./data/original/Base Varejo.csv', sep=';') #Reconhecimento de ';' como coluna

#CÓPIA DO ARQUIVO ORIGINAL PARA NÃO MODIFICAR AS INFORMAÇÕES BASE:
df = df_original.copy()


#RECONHECIMENTO PRIMEIRAS INFORMAÇÕES DO ARQUIVO BASE:
print(f"Total de registros: {df.shape[0]}") #Registros
print(f"Total de colunas: {df.shape[1]}") #Colunas
print(df.columns.tolist()) #Nome das Colunas
print(df.head(3)) #Primeiras linhas
print(df.dtypes)# Tipo de cada coluna
print(df.isnull().sum()) # %Valores Nulos

#REMOÇÃO DE COLUNAS NULAS:
colunas_nulas = ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
df.drop(columns=colunas_nulas, inplace=True)
print("Col. Nulas ok")

#DEIXANDO AS COLUNAS COM AS ESCRITAS DA MESMA MANEIRA:
colunas_texto = ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip().str.upper()
print("Col. Textos ok")

#TRANSFORMAÇÃO DO TIPO DAS COLUNAS:
colunas_inteiras = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']
for col in colunas_inteiras:
    df[col] = df[col].astype('int64')
print("Col.Inteiras ok")

#REMOÇÃO DE DUPLICADOS:
duplicados_qtd = df.duplicated().sum()
if duplicados_qtd > 0:
    df.drop_duplicates(inplace=True)
print("Duplicados ok")

#REMOÇÃO DE NULOS:
df.dropna(inplace=True)
print("Nulos ok")

#TRANSFORMAÇÃO DA COLUNA DATA EM FORMATO ADEQUADO:
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
print("Data ok")

#GERANDO CÓPIA ARQUIVO BASE:
df.to_csv('./data/arquivo.limpo/Varejo_Limpo.csv', sep=';', index=False)

#REMOÇÃO DE DUPLICADOS
duplicados_qtd = df.duplicated().sum()
if duplicados_qtd > 0:
    df.drop_duplicates(inplace=True)
print("Duplicados ok")

#TRANSFORMAÇÃO DA COLUNA DATA EM FORMATO ADEQUADO DE DATA
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
print("Data ok")

#ESTATÍSTICAS:

#Número de Filhos por cliente
coluna_filhos = 'CL_FHL'
estatisticas = df[coluna_filhos].describe()
quantidade_padrao_filhos = df[coluna_filhos].mode()[0]
print(f"Média de filhos:  {estatisticas['mean']:.2f}")
print(f"Mediana de filhos: {estatisticas['50%']:.2f}")
print(f"Mode de filhos:    {quantidade_padrao_filhos}")
print(f"Desvio Padrão:     {estatisticas['std']:.2f}\n")

#CRIAÇÃO DE GRÁFICO PARA REPRESENTAÇÃO DAS ESTATISTICAS ENCONTRADAS CL_FHL:

dados_filhos = df["CL_FHL"].values
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_facecolor('white')
sns.histplot(data=df, x='CL_FHL', discrete=True, hue='CL_FHL',
              palette='dark',alpha=0.85, ax=ax, legend=False,
              edgecolor='white',linewidth=2)

media_filhos = estatisticas ["mean"]
mediana_filhos = estatisticas ["50%"]

ax.axvline(media_filhos,   color="#0A0A0A",
            linewidth=2, linestyle='--', label=f'Média: {media_filhos:.2f}')

ax.axvline(mediana_filhos, color='orange',
            linewidth=2, linestyle='--',  label=f'Mediana: {mediana_filhos:.2f}')

ax.set_title("FILHOS POR CLIENTE", fontsize=10, fontweight='bold')
ax.set_xlabel("Quantidade de Filhos (CL_FHL)", fontsize=9)
ax.set_ylabel("Quantidade de Clientes", fontsize=10)
ax.legend(fontsize=9)

ax.grid(axis='y', linestyle=':', alpha=0.3)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.tight_layout()
plt.show()

