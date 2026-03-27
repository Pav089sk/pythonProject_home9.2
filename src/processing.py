from mypy.server.update import sort_messages_preserving_file_order


def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    соответствует указанному значению.
    """
    sort_list = []
    for param in list_dictionary:
        if param.get("state") == state:
            sort_list.append(param)

    return sort_list


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    for operation in list_dict:
       if len(operation['date']) < 26:
         return "Некорректный формат даты"

    return sorted(list_dict, key=lambda i: i.get("date"), reverse=direction)
