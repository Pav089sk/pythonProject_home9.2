import csv
import pandas as pd


def csv_read(path_csv: str) -> list:
    """Функция принимает путь до csv файла
    и возвращает список словарей из строк файла """
    with open(path_csv) as file:
        reader = csv.DictReader(file, delimiter=';')
        trans_list_csv = []
        for row in reader:
            trans_list_csv.append(row)
    return trans_list_csv

# print(csv_read('../data/transactions.csv'))

def excel_read(path_excel: str) -> list:
    """Функция принимает путь до excel файла
    и возвращает список словарей из строк файла"""
    excel_data = pd.read_excel(path_excel).to_dict('records')
    return excel_data


# print(excel_read('../data/transactions_excel.xlsx'))