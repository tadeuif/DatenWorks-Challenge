import pandas as pd

def csvToDf(csv1, csv2): #transforma o .csv em DataFrame
  df1 = pd.read_csv(csv1)
  df2 = pd.read_csv(csv2)
  return df1, df2