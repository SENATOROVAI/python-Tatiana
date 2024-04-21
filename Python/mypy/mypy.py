"""
 docs module
"""
# Type Hinting = Статическая типизация =Аннотация типов in python 3.8
# Раннее авыявление ошибок, отладка кода
from __future__ import annotations

x: int = 6


def get_value(value: int) -> int:
    """Function printing python version."""
    return value + 5


print(get_value(x))

num: int = 1


def get_value2(value: int) -> bool:
    """Function printing python version."""
    return value == 5


print(get_value2(x))

get_value2(5)
