# Type Hinting = Статическая типизация =Аннотация типов in python 3.8
# Раннее авыявление ошибок, отладка кода

x: int = 6

def getValue(value: int) -> int:
    return value + 5

#print(getValue('5'))
print(getValue(x))

num: int = 1

def get_Value(value: int) -> bool:
    return value == 5

#print(getValue('5'))
print(getValue(x))

get_Value('5')


