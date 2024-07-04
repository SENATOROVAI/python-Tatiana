# Type Hinting = Статическая типизация =Аннотация типов in python 3.8
# Раннее авыявление ошибок, отладка кода
from __future__ import annotations

var_x: int = 6


def get_value(value: int) -> int:
    """Function printing python version."""
    return value + 5


print(get_value(var_x))

num: int = 1


def get_value2(value: int) -> bool:
    """Function printing python version."""
    return value == 5


print(get_value2(var_x))

get_value2(5)
