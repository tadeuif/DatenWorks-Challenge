import pandas as pd

def dpsCalc(df, sortOrder): #calcula o DPS de cada campeão no DataFrame unido
  if sortOrder == 'asc':
    sort = True
  elif sortOrder == 'dsc':
    sort = False
  dfUnited = df
  names = dfUnited['NAME'].unique()
  lengthNames = len(dfUnited['NAME'])
  dpsList = []
  for x in range(lengthNames):
    if names[x] == dfUnited['NAME'][x]:
      dps = dfUnited['ATTACK_DAMAGE'][x]*dfUnited['ATTACK_SPEED'][x]
      dpsList.append(dps)

  dfDPS = pd.DataFrame({'NAME':dfUnited['NAME'],
                        'DPS':dpsList})

  return print(dfDPS.sort_values(by=['DPS'], ascending=sort))