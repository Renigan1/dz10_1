def mask_account_card(num_card: str) -> str:
    """Функция общей маскировки карты и счета"""
    if 'Счет' in num_card:
        result = f'Счет **{num_card[-4:]}'
    else:
        word_list = num_card.split()
        symbol_list = []
        for word in word_list:
            if word.isalpha():
                symbol_list.append(word)
        symbol_list1 = ' '.join(symbol_list)
        result = f'{symbol_list1} {num_card[-19:-14]}** ****{num_card[-5:]}'
    return result

def get_data(date_output: str) -> str:
    """Функция преобразования даты"""
    data_result = date_output[:10]
    data_list = data_result.split('-')
    data_list.reverse()
    result = '.'.join(data_list)
    return result
