from utils import transaction_data

transactions_list = transaction_data('../data/operations.json')
for transact in transactions_list:
    if transact == {}:
        continue
    # print(transact)
    def transaction_amount(operation: tuple) -> float:
      if transact['operationAmount']['currency']['code'] == 'RUB':
        return transact['operationAmount']['amount']
      else:
        return transact['operationAmount']['amount']

    print(transaction_amount(transact))



