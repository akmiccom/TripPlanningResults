from setting import FILE_NAME, EXCEL_FILE_NAME
import pandas as pd

def csvToExcel():
    csv = pd.read_csv(FILE_NAME, encoding='shift-jis')
    csv.drop_duplicates(inplace=True)
    csv.to_excel(EXCEL_FILE_NAME, index=False)

csvToExcel()