def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает
    новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение"""
    sorted_list = []
    for dict_element in list_dict:
        if dict_element.get("state") == state:
            sorted_list.append(dict_element)
    return sorted_list


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """Функция, которая принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list
