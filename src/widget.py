from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(num_card: str) -> str:
    """Функция общей маскировки карты и счета"""
    if "Счет" in num_card:
        account_number = num_card[5:]
        result = get_mask_account(account_number)
        symbol_list1 = "Счет"
    else:
        word_list = num_card.split()
        num_list = []
        symbol_list = []
        for word in word_list:
            if word.isalpha():
                symbol_list.append(word)
            elif word.isnumeric():
                num_list.append(word)
        symbol_list1 = " ".join(symbol_list)
        num_list1 = "".join(num_list)
        result = get_mask_card_number(num_list1)
    return f"{symbol_list1} {result}"


def get_data(date_output: str) -> str:
    """Функция преобразования даты"""
    data_result = date_output[:10]
    data_list = data_result.split("-")
    data_list.reverse()
    result = ".".join(data_list)
    return result
