# **Análise de Dados com Python [T2]**
## Mini-Projeto Avaliativo - Módulo 1 - Semana 07
### Estudante: Larissa Alquieri


## Descrição Inicial
Este Mini-Projeto tem como objetivo a Análise Exploratória de Dados aplicada ao varejo para aprender como transformar dados brutos em informações útei, para que seja possível a aplicação da parte teórica aprendida nas aulas em análises reais.

## Instruções Iniciais
Para que seja possível a execução correta dos arquivos deste mini-projeto , é necessário ter instalado em seu computador: 
* Python
* Visual Studio Code [VS Code]
* Bibliotecas: Pandas, Numpy, Matplotlib e Seaborn

## ETL
A extração, transformação e carregamento de dados é base para uma análises de dados coerente.Neste mini-projeto utilizamos destes recursos para gerar análises coerentes e de fácil entendimento, pois é nesta etapa que são encontradas as inconsistências que prejudicariam os insights e as conclusões.
Tratar destes dados é de suma importância para não haver distorção nas estatísticas levantadas e causar falsas afirmações sobre os dados encontrados.


## Preparação dos Dados
Antes de serem realizadas as análises exploratórias junto ao banco de dados, foram realizadas algumas limpezas para melhora na hora de serem realizadas as análises. Dentre os processos realizados cabe destacar a eliminação de 4 colunas que não incluiam dados, foram removidos espaços desnecessários entre as palavras, remoção de linhas duplicadas, eliminação de elementos nulos que atrapalhariam a estatística, conversão de datas para que fosse possível uma melhor análise. O arquivo tratado foi salvo na pasta `./data/arquivo.limpo/Varejo_Limpo.csv` para versionamento.

## INSIGHTS

### Ajustes nos registros
Ao primeiro comando para o levantamento de registros e colunas foi encontrado 830000 registros e apenas 1 coluna. Por isso foi necessário acrescentar o comando 'sep=' no comando inicial de leitura do arquivo para que a bilbioteca pandas conseguisse identificar a separação de colunas da maneira correta. Após este comando foram encontradas 14 colunas no arquivo. Após os primeiros comandos percebeu-se que existiam 4 colunas com elementos vazios pois ao analisar a quantidade de valores nulos por coluna, elas apresentaram exatos 830.000 elementos nulos ou seja, a coluna inteira era nula.

### Média e mediana
Ao rodar os comandos para as médias e medianas relacionados a filhos dos clientes pode-se observar que a média de filhos é de 1.15** e a **mediana é de 0. 
Com isso observa-se que a **maioria dos clientes não possui filhos**.Quando se observa o desvio padrão nota-se que este valor nos leva aos dados de que apesar de ter clientes sem filhos, existem alguns que possuem mais do que um filho, mostrando perfis diferentes dentro de uma mesma base de clientes. Ao gerar o **'Gráfico 1'**, nota-se a  diversidade no quesito filhos, mas ainda assim prevalecendo a maioria não possuindo filhos. Estes dados podem ser importantes para influenciar as definições mais acertadas para novas campanhas ou melhorar as já existentes dos públicos alvos definidos.

### Volume de vendas
Quando se faz o cruzamento de dados entre **gênero e volume de compras** e é gerado o **'Gráfico** 2', nota-se que a categoria alimentos é a mais vendida, seguido de higiene e limpeza. Outro dado que destaca-se é de que predominantemente o sexo feminino é o maior comprador, em todas as categorias.
Analisando outro cruzamento de dados seguindo a direção das análises já feitas nos mostram que a grande maioria de mulheres**(53,35%)** não possuem filhos, seguido por mulheres que possuem apenas 1 filho**(13.1%)**. 

### Produtos mais vendidos
Quando feito a análise dos dados cruzando as informações de mulheres e alimentos, foi encontrado os produtos alimentícios com maiores vendas, conforme Gráfico 3. Dos top 5 produtos, 4 são produtos refrigerados e pode gerar sugestões de campanhas para impulsionar produtos que sejam corelacionados.

## CONCLUSÃO
Com base nas análises realizadas concluiu-se que o público feminino em todas as categorias são a maioria nas vendas, o gênero masculino não teve o maior foco nestas análises haja vista que a predominância nas vendas é do público feminino.
Com isso se fez necessário uma maior atenção nas escolhas das análises, aumentando o foco no perfil de consumo feminino e consequentemente auxiliando nas escolhas de campanhas e posicionamento de produtos.
 Os produtos com maior destaque dentro da categoria alimentícia foram os refrigerados,dentre os  principais com maior volume de vendas refrigerados e de uso diário, onde de cinco itens quatro são desta categoria.
O posicionamento de produtos é crucial para trazer maior visibilidade e assim possivelmente aumento de vendas haja vista que nas áreas onde são as maiores vendas também há consequentemente maior circulação.