import pandas as pd

def convert_Excel_To_CSV():
    # Need to Install pandas, openpyxl
    data_xls = pd.read_excel('C:/Users/DESK01/Desktop/Excel Class/Dummy Data.xlsx', 'Data', dtype=str, index_col=None)
    data_xls.to_csv('C:/Users/DESK01/Desktop/Excel Class/Dummy Data.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    convert_Excel_To_CSV()