def get_mask_card_number(card_num: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по заданному правилу
    """
    card_num_str: str = str(card_num)
    result: str = f"{card_num_str[:4]} {card_num_str[4:6]}** **** {card_num_str[12:]}"
    return result


print(get_mask_card_number(7000792289606361))


def get_mask_account(invoice_num: int) -> str:
    """
    Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по заданному правилу
    """
    invoice_num_str: str = str(invoice_num)
    result: str = f"**{invoice_num_str[-4:]}"
    return result


print(get_mask_account(73654108430135874305))
