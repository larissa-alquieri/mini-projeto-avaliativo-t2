#IMPORTAÇÃO DAS BIBLIOTECAS:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#====================================================================================

#LEITURA ARQUIVO BASE:
df_original = pd.read_csv('./data/original/Base Varejo.csv', sep=';') #Reconhecimento de ';' como coluna

#==================================================================================

#CÓPIA DO ARQUIVO ORIGINAL PARA NÃO MODIFICAR AS INFORMAÇÕES BASE:
df = df_original.copy()

#================================================================================

#REMOÇÃO DE COLUNAS NULAS:
colunas_nulas = ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
df.drop(columns=colunas_nulas, inplace=True)

#=====================================================================

#DEIXANDO AS COLUNAS COM AS ESCRITAS DA MESMA MANEIRA:
colunas_texto = ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip().str.upper()

#=================================================================================
#TRATAMENTO NULOS

df['PR_CAT'] = df['PR_CAT'].apply(lambda x: 'SEM CATEGORIA' if x in ['NAN', '', 'N/D', 'N/A'] else x)
#=============================================================================== 

#REMOÇÃO DE DUPLICADOS:
duplicados_qtd = df.duplicated().sum()
if duplicados_qtd > 0:
    df.drop_duplicates(inplace=True)

#===============================================================================
#REMOÇÃO DE NULOS:
df.dropna(subset=['CL_GENERO', 'CL_ID', 'CO_ID'], inplace=True)

#=================================================================================
#DATE TIME

df = df[df['CO_ID'].notnull()]
def valida_converte_data(data_str):
    try:
        return datetime.strptime(str(data_str).strip(), '%d/%m/%Y')
    except ValueError:
        return None

df['DATA'] = df['DATA'].apply(valida_converte_data)
df.dropna(subset=['DATA'], inplace=True)

#=================================================================================

#TRANSFORMAÇÃO DO TIPO DAS COLUNAS:
colunas_inteiras = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']
for col in colunas_inteiras:
    df[col] = df[col].astype('int64')
print("Colunas Inteiras ok")

#================================================================================

#GERANDO CÓPIA ARQUIVO BASE:
df.to_csv('./data/arquivo.limpo/Varejo_Limpo.csv', sep=';', index=False)

#==============================================================================

#NÚMERO DE FILHOS POR CLIENTES:
coluna_filhos = 'CL_FHL'
estatisticas = df[coluna_filhos].describe()
quantidade_padrao_filhos = df[coluna_filhos].mode()[0]
print(f"Média de filhos:  {estatisticas['mean']:.2f}")
print(f"Mediana de filhos: {estatisticas['50%']:.2f}")
print(f"Mode de filhos:    {quantidade_padrao_filhos}")
print(f"Desvio Padrão:     {estatisticas['std']:.2f}\n")

#=========================================================================================

#GRÁFICO 1
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

ax.set_title("Gráfico 1: FILHOS POR CLIENTE", fontsize=10, fontweight='bold')
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

#========================================================================================
#GRÁFICO 2

df['PR_CAT'] = df['PR_CAT'].astype(str).str.strip().str.upper()
filtro_sujeira = df['PR_CAT'].str.contains('N/D|N/A|NAN', na=True)
df_limpo_cat = df[~filtro_sujeira]
genero_cat = df_limpo_cat.groupby(['CL_GENERO', 'PR_CAT']).size().reset_index(name='TOTAL.VENDAS')
print("\nAGRUPAMENTO GENEROXCATEGORIA")
print(genero_cat.head(10))
df_plot = df_limpo_cat.groupby(['PR_CAT', 'CL_GENERO']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor('white')
cores = ["#a6163f", "#124fb0"]
df_plot.plot(kind='bar', ax=ax, color=cores, width=0.8)
for container in ax.containers:
    ax.bar_label(container, padding=0, fontsize=7, fmt='%d', color="#5a5758")
ax.set_title("Gráfico 2: COMPRAS CATEGORIA X GÊNERO", fontsize=12, fontweight='bold', pad=20)
ax.set_xlabel("CATEOGRIA(PR_CAT)", fontsize=8, fontweight='bold', labelpad=10, )
ax.set_ylabel("COMPRAS(CL_GENERO)", fontsize=8, fontweight='bold', labelpad=10)
plt.xticks(rotation=0, ha='center')
ax.grid(axis='y', linestyle='--', alpha=0.3)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
plt.tight_layout()
plt.show()

#==================================================================================================

#GÊNERO FEMININO X FILHOS
df_m = df[df['CL_GENERO'] == 'F']
mulheres_filhos = df_m.groupby('CL_FHL').size().reset_index(name='TOTAL')
print("\nTabela de distribuição de filhos (Público Feminino):")
print(mulheres_filhos)

mulheres_filhos['PERCENTUAL'] = (mulheres_filhos['TOTAL'] / mulheres_filhos['TOTAL'].sum()) * 100
print("\nTabela de distribuição com Porcentagem:")
print(mulheres_filhos)

#==================================================================================================

#PRODUTOS MAIS VENDIDOS ENTRE MULHERES:

df_alimentos_mulheres = df_limpo_cat[(df_limpo_cat['PR_CAT'] == 'ALIMENTOS') & (df_limpo_cat['CL_GENERO'] == 'F')]
top_produtos = df_alimentos_mulheres['PR_NOME'].value_counts().head(5)
print(df_alimentos_mulheres)

#GRÁFICO 3

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_facecolor('white')
top_produtos.plot(kind='barh', ax=ax, color="#6f0416", width=0.7)
ax.invert_yaxis() 
for container in ax.containers:
    ax.bar_label(container, padding=5, fontsize=8, fmt='%d', color="#5a5758")
ax.set_title("Gráfico 3:PRODUTOS MAIS VENDIDOS", fontsize=12, fontweight='bold', pad=20)
ax.set_xlabel("Quantidade de Vendas (Volume)", fontsize=9, fontweight='bold', labelpad=10)
ax.set_ylabel("Nome do Produto (PR_NOME)", fontsize=9, fontweight='bold', labelpad=10)
ax.grid(axis='x', linestyle='--', alpha=0.3)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
plt.tight_layout()
plt.show()