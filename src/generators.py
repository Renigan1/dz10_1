"""Модуль генераторов для обработки массивов транзакций"""

from typing import Iterable, Iterator


def filter_by_currency(transactions: Iterable[dict], currency_code: str) -> Iterator[dict]:
    """функция, которая принимает на вход список словарей, представляющих транзакции, и должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Iterator[str]:
    """генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        string_to_return = ""
        block_counter = 0
        for digit in number:
            block_counter += 1
            if block_counter <= 4:
                string_to_return += digit
            else:
                string_to_return += " " + digit
                block_counter = 1
        yield string_to_return
