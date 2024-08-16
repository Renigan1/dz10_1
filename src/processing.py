def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает
    новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    filtered_list = []
    for dictionary_element in list_of_dicts:
        if dictionary_element.get("state") == state:
            filtered_list.append(dictionary_element)
    return filtered_list


def sort_by_date(list_of_dicts: list, is_descending: bool = True) -> list:
    """Функция, которая принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате"""
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=is_descending)
    return sorted_list
