def filter_by_state(list_dictionary, state='EXECUTED'):
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    соответствует указанному значению.
    """
    sort_list=[]
    for param in list_dictionary:
         i = param.get('state')
         if i == 'EXECUTED':
            sort_list.append(param)


    return sort_list

print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]))



# def sort_by_date(list_dict):
#     """Функция возвращает новый список, отсортированный по дате"""
#
#     pass
#

# #print(filter_by_state([
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]))