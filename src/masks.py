def get_mask_card_number(mask_card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    new_string = f"{mask_card_number[0:4]} {mask_card_number[4:6]}** **** {mask_card_number[-4:]}"
    return new_string


def get_mask_account(mask_account: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    mask_acc_number = f"**{mask_account[-4:]}"
    return mask_acc_number
