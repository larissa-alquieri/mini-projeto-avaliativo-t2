# **Análise de Dados com Python [T2]**
## Mini-Projeto Avaliativo - Módulo 1 - Semana 07
### Estudante: Larissa Alquieri


## Descrição Inicial:
Este Mini-Projeto tem como objetivo a Análise Exploratória de Dados aplicada ao varejo para aprender como transformar dados brutos em informações útei, para que seja possível a aplicação da parte teórica aprendida nas aulas em análises reais.

## Instruções Iniciais:
Para que seja possível a execução correta dos arquivos deste mini-projeto , é necessário ter instalado em seu computador: 
* Python
* Visual Studio Code [VS Code]
* Bibliotecas: Pandas, Numpy, Matplotlib e Seaborn

## INSIGHTS:

1. Ao primeiro comando para o levantamento de registros e colunas foi encontrado 830000 registros e apenas 1 coluna. Por isso foi necessário acrescentar o comando 'sep=' no comando inicial de leitura do arquivo para que a bilbioteca pandas conseguisse identificar a separação de colunas da maneira correta. Após este comando foram encontradas 14 colunas no arquivo

2. Após os primeiros comandos percebeu-se que existiam 4 colunas com elementos vazios pois ao analisar a quantidade de valores nulos por coluna, elas apresentaram exatos 830.000 elementos nulos ou seja, a coluna inteira era nula.

3. Ao rodar os comandos para as médias e medianas relacionados a filhos dos clientes pode-se observar que a média de filhos é de 1.15 e a mediana é de 0. Com isso observa-se que a maioria dos clientes não possui filhos.Quando se observa o desvio padrão nota-se que este valor nos leva aos dados de que apesar de ter clientes sme filhos, existem alguns que possuem mais do que 1 filho, mostrando que existem perfis diferentes dentro de uma mesma base de clientes.

*IMAGEM REPRESENTANDO OS DADOS ENCONTRADOS NA MEDIA E MEDIANA REFERENTE AOS FILHOS DE CLIENTES:*

![Gráfico Demonstrando a relação clientes x filhos](C:\Users\Larissa\Python\mini-projeto\notebook\Gráfico Filhos por Cliente.png)

É possível observar pelo gráfico que existe uma gama diversificada de clientes com filhos, porém a maioria não possui filhos. Estes dados podem ser importantes para influenciar as definições mais acertadas para novas campanhas ou melhorar as já existentes dos públicos alvos definidos.