from masks import get_mask_card_number, get_mask_account

def mask_account_card (card_or_invoice_num: str) -> str:
    """ функция обработки информации о картах и счетах
    """
    parts = card_or_invoice_num.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    return f"{name} {mask_number}"


print(mask_account_card("Счет 64686473678894779589"))

def get_date(date_string: str) -> str:
    """ функция форматирования типа строки даты
    """
    return f"{date_string[8:10]}-{date_string[5:7]}-{date_string[:4]}"

print(get_date("2024-03-11T02:26:18.671407"))