import pandas as pd

def mergeDf(df1, df2, column, joinType):  #une os DataFrames
  dfUnited = pd.merge(df1, df2, on=column, how=joinType)
  return dfUnited