Análise de Dados com Python [T2]
Mini-Projeto Avaliativo - Módulo 1 - Semana 07
Estudante: Larissa Alquieri


============== DESCRIÇÃO INICIAL DO MINI-PROJETO =============
Este Mini-Projeto tem como objetivo a Análise Exploratória de Dados aplicada ao varejo para aprender como transformar dados brutos em informações útei, para que seja possível a aplicação da parte teórica aprendida nas aulas em análises reais.
============================*=============================


============== INSTRUÇÕES INICIAIS ================
1.Para que seja possível a execução correta dos arquivos deste mini-projeto , é necessário ter instalado em seu computador: Python, Visual Studio Code [VS Code] e as bibliotecas Pandas e NumPy.
============================*=============================

========== INSIGHTS ==========
Ao primeiro comando para o levantamento de registros e colunas foi encontrado 830000 registros e apenas 1 coluna. Por isso foi necessário acrescentar o comando 'sep=' no comando inicial de leitura do arquivo para que a bilbioteca pandas conseguisse identificar a separação de colunas da maneira correta. Após este comando foram encontradas 14 colunas no arquivo.

Após os primeiros comandos percebeu-se que existiam 4 colunas com elementos vazios pois ao analisar a quantidade de valores nulos por coluna, elas apresentaram exatos 830.000 elementos nulos ou seja, a coluna inteira era nula.
