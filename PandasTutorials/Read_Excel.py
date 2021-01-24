import pandas as pd
df_excel = pd.read_excel('C:/Users/DESK01/Desktop/Excel Class/Dummy Data.xlsx', 'Data')
print(df_excel)
print(df_excel['Region'].unique())
# print(pd.unique(df_excel[['Region','Country']].values.ravel('K')))
print(df_excel.drop_duplicates(['Region','Country'])[['Region','Country']])