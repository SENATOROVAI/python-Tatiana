# Type Hinting = Статическая типизация =Аннотация типов in python 3.8
# Раннее авыявление ошибок, отладка кода

x: int = 6


def get_value(value: int) -> int:
    """Function printing python version."""
    return value + 5


# print(getValue('5'))
print(get_value(x))

num: int = 1

def get_Value(value: int) -> bool:
    """Function printing python version."""
    return value == 5


# print(getValue('5'))
print(get_Value(x))

get_Value(5)
