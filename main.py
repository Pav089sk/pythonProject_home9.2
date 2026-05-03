from src.utils import transaction_data
from src.reader import csv_read, excel_read
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency


def main():
    """Функция основной логики работы приложения"""
    while True:
    #Модуль приветствия и выбора типа входных данных"""
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        user_choise = input("Пользователь: ")

        if user_choise == "1":
            file_type = "JSON"
            data = transaction_data("data/operation.json")
            break
        elif user_choise == "2":
            file_type = "CSV"
            data = csv_read("data/transactions.csv")
            break

        elif user_choise == "3":
            file_type = "XLSX"
            data = excel_read("data/transactions_excel.xlsx")
            break
        print("Некорректный ввод/n")
    print(f"Для обработки выбран {file_type}-файл.")

    while True:
    # Модуль фильтрации по статусу операции
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Пользователь: ").upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            choose_data = filter_by_state(data, status)
            break
        print(f"Статус операции {status} недоступен.")
    print(f"Операции отфильтрованы по статусу {status}")

    # Модуль сортировки и необходимости сортировки по дате
    while True:
        print('Отсортировать операции по дате? Да/Нет')
        sort_status = input().lower()
        if sort_status == 'нет':
            sort_status = False
            break
        elif sort_status == 'да':
            sort_status = True
            break
    while True:
        if not sort_status:
            sorted_list = choose_data
            break
        else:
            print('Отсортировать по возрастанию или по убыванию?')
            sort_direction = input().lower()
            if sort_direction == 'по возрастанию':
                sorted_list = sort_by_date(choose_data, False)
                break
            elif sort_direction == 'по убыванию':
                sorted_list = sort_by_date(choose_data)
                break

    # Фильтрация по рублевым транзакциям
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_currency_choiсe = input().lower()
        if user_currency_choiсe == 'да':
            current_list = list(filter_by_currency(list(sorted_list),'RUB'))
            break
        elif user_currency_choiсe == 'нет':
            current_list = sorted_list



if __name__ == '__main__':
    main()