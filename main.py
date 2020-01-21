from csvtoDf import csvToDf
from mergeDf import mergeDf
from dpsCalc import dpsCalc

#metodo main abaixo serve como primeiro teste após passar os argumentos corretamente para as funções,
#segundo a documentação.

def main():
  dfs = csvToDf('data1.csv','data2.csv')
  dfUnido = mergeDf(dfs[0],dfs[1],'NAME','outer')
  dpsCalc(dfUnido, 'dsc') #asc, dsc
  
main()