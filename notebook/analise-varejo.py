#IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import numpy as np

#LEITURA ARQUIVO BASE
df_original = pd.read_csv('./data/original/Base Varejo.csv', sep=';') #Reconhecimento de ';' como coluna

#CÓPIA DO ARQUIVO ORIGINAL PARA NÃO MODIFICAR AS INFORMAÇÕES BASE
df = df_original.copy()

#RECONHECIMENTO PRIMEIRAS INFORMAÇÕES DO ARQUIVO BASE
#print(f"Total de registros: {df.shape[0]}") #Registros
#print(f"Total de colunas: {df.shape[1]}") #Colunas
#print(df.columns.tolist()) #Nome das Colunas
#print(df.head(3)) #Primeiras linhas
#print(df.dtypes)# Tipo de cada coluna
#print(df.isnull().sum()) # %Valores Nulos

#REMOÇÃO DE COLUNAS NULAS
colunas_nulas = ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
df.drop(columns=colunas_nulas, inplace=True)

#DEIXANDO AS COLUNAS COM AS ESCRITAS DA MESMA MANEIRA
colunas_texto = ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip().str.upper()


colunas_inteiras = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']
for col in colunas_inteiras:
    df[col] = df[col].astype('int64')








#GERANDO ARQUIVO NOVO DE LIMPEZA
df.to_csv('./data/arquivo.limpo/Varejo_Limpo.csv', sep=';', index=False)