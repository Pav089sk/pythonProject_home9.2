from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_invoice_num: str) -> str:
    """
    функция обработки информации о картах и счетах
    """

    if card_or_invoice_num == "" or card_or_invoice_num == " ":
        return "Информация отсутствует"

    parts: list = list(card_or_invoice_num.split())
    number: int = int(parts[-1])
    name: str = str(" ".join(parts[:-1]))

    if name.lower() == "счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    return f"{name} {mask_number}"


def get_date(date_string: str) -> str:
    """
    функция форматирования типа строки даты
    """
    if len(date_string) < 8:
        return ""

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"
