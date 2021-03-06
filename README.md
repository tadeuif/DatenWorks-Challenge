# DatenWorks-Challenge

DATENWORKS Development Code challenge!

Esta documentação serve como guia para utilização das funções baseadas nos 2 arquivos enviados pela DATENWORKS.

Temos as seguintes funções implementadas separadamente em cada arquivo .py:

    csvToDf(csv1, csv2): 
    Transforma os arquivos .csv em DataFrames.
    - os arquivos devem rigorosamente ser do tipo .CSV;
    - devem conter as colunas NAME,ATTACK_SPEED,ATTACK_DAMAGE, sendo NAME obrigatório em ambos;
    - os argumentos passados para a função devem ser do tipo String, com o nome dos arquivos + .csv. Ex.: 'arquivo.csv';
    - a função retorna os dois arquivos passados já em formatos de DataFrame;

    mergeDf(df1, df2, column, joinType):
    Irá unir os 2 DataFrames passados nos argumentos, através da coluna com função ID escolhida e também o tipo de JOIN utilizado.
    - como os DataFrames possuem a coluna NAME, é recomendado que seja passado este valor para as colunas. Para o tipo de JOIN, é também recomendado que seja passado o valor 'outer', para que não tenhamos nenhum tipo de perde de dados;
    - a função retorna um único DataFrame com todas as informações de ambos os DataFrames anteriores, sem duplicatas;

    dpsCalc(df, sortOrder):
    Calculará o DPS de cada campeão pelas colunas ATTACK_DAMAGE e ATTACK_SPEED.
    - o DataFrame passado deve conter obrigatóriamente as colunas NAME,ATTACK_SPEED,ATTACK_DAMAGE;
    - para o parametro sortOrder, podem ser passados dois valores: asc, dsc. É recomendado que seja passado o valor 'dsc', para que esteja de acordo com o desafio(do mais forte para o mais fraco);
    - todos os campeões terão seu DPS calculado, exceto os que não possuem algum dos valores, ou seja, ATTACK_DAMAGE ou ATTACK_SPEED;
    - no caso de falta de informações, será exibido a sigla NaN(Not a number), pois não foi possível realizar o cálculo;
