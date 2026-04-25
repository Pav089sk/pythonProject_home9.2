import logging
import os


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
log_path = os.path.join(project_root, "logs", "masks.log")
file_handler = logging.FileHandler(log_path, mode="w")
file_formater = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по заданному правилу
    """
    logger.debug("Принимаем номер карты")
    card_num_str: str = str(card_num)
    if len(card_num_str) > 16 or len(card_num_str) < 16:
        logger.error("Ошибочный формат номера карты")
        return "Неверный номер карты"

    result: str = f"{card_num_str[:4]} {card_num_str[4:6]}** **** {card_num_str[12:]}"
    logger.info("Номер карты возвращён замаскированным")
    return result


def get_mask_account(invoice_num: int) -> str:
    """
    Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по заданному правилу
    """
    logger.debug("Принимаем номер счета")
    invoice_num_str: str = str(invoice_num)
    if len(invoice_num_str) > 20 or len(invoice_num_str) < 20:
        logger.error("Ошибочный формат номера счета")
        return "Неверный номер счета"
    result: str = f"**{invoice_num_str[-4:]}"
    logger.info("Номер счета возвращён замаскированным")
    return result
