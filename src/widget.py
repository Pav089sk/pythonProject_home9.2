from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_invoice_num: str) -> str:
    """
    функция обработки информации о картах и счетах
    """

    if card_or_invoice_num == '' or card_or_invoice_num == ' ':
        return 'Информация отсутствует'

    parts: list = list(card_or_invoice_num.split())
    number: int = int(parts[-1])
    name: str = str(" ".join(parts[:-1]))

    if name.lower() == "счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    return f"{name} {mask_number}"


# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
# print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """
    функция форматирования типа строки даты
    """
    if len(date_string) < 8:
        return ''

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"


# print(get_date("2024-03-11T02:26:18.671407"))
