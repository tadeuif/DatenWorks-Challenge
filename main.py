import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

notas = pd.Series([2,7,5,10,6], index=["Wilfred", "Abbie", "Harry", "Julia", "Carrie"])

#print(notas)
def media(list1, list2):
  lista_media = []
  for x, y in zip(list1, list2):
    result = (x + y)/2
    lista_media.append(result)
  return lista_media

df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0],
                   })

#print(df)

média = media(df['Prova'],df['Seminário'])

df['Média'] = média

#print(df)
#print(df["Faltas"].value_counts().plot.bar())

#df1 = pd.read_excel("Login-Logout_Eventos CARINA.xlsx", index_col = 1)

#print(df1)
df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")
print(df1.head(n=10))
print(df2.head(n=20))
print(df1[['NAME','ATTACK_SPEED']])
print("//////////")
frames = [df1,df2]

result = pd.concat(frames)
names = result['NAME'].unique()

#print(result)
#print(names)

#print(result['NAME'][2])
champName_list = result['NAME']
tam = len(names)
print(tam)

#print(result.groupby("NAME").mean())#PULO DO GATO PODE ESTAR AQUI
#result2 = pd.concat(frames,sort=False, ignore_index="True")
result2 = pd.merge(df1, df2, on='NAME', how='outer')#PULO DO GATO REAL
names2 = result2['NAME'].unique()
result2.fillna(0)
print(result2)
dps = result2['ATTACK_DAMAGE'][1]*result2['ATTACK_SPEED'][1]#AJUSTAR NaN
print(result2['NAME'][0])
print(dps)
#print(champName_list)
#for x in names:
  #if champName_list[x] == names[x]:
    #dps = result['ATTACK_DAMAGE']*result['ATTACK_SPEED']
    #listaDps = []
    #listaDps.append(dps)

dfDPS = pd.DataFrame({'NAME':[names[0]],
                      'DPS':[0],})

#print(dfDPS)

#df.to_csv("aulas.csv")
#df.to_excel("aulas.xlsx")