import csv

import pandas as pd


def csv_read(path_csv: str) -> list:
    """Функция принимает путь до csv файла
    и возвращает список словарей из строк файла"""
    with open(path_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        trans_list_csv = []
        for row in reader:
            trans_list_csv.append(row)
    return trans_list_csv


def excel_read(path_excel: str) -> list:
    """Функция принимает путь до excel файла
    и возвращает список словарей из строк файла"""
    excel_data = pd.read_excel(path_excel).to_dict("records")
    return excel_data

# if __name__ == '__main__':
    # print(type((excel_read('../data/transactions_excel.xlsx'))))
    # print(csv_read('../data/transactions.csv'))