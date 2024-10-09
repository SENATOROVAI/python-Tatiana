# %%NBQA-CELL-SEPfaab7c
"Module on garbage collector, hash, system hashing, types annotation, systen coding."


# %%NBQA-CELL-SEPfaab7c
import dis
import hashlib
import socket
import ssl
from typing import Dict, List

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

# !pip install cryptography


# %%NBQA-CELL-SEPfaab7c
list1 = [
    2
]  # структура даннных (содержит данные или др списки). структура даннных - контейнер,кот хранит все данные
list2 = list1
id(list1) == id(list2)
list1 is list2
del list1
# id(list2)
# id(list1)
print(list2)
del list2
id(list2)


# %%NBQA-CELL-SEPfaab7c
# Late binding. See picture below
powers = []  #
for i in (1, 2):  # loop over the tuple (1,2)

    def inner(var_x):  # i == 1. Entering the def.
        return var_x**i  # no x added at the point.

    powers.append(
        inner
    )  # calling the function and putting it into powers as 1st\2nd element
for (
    var_p
) in (
    powers
):  # call for each element in powers(2 inner functions), and feed 5 into each of the functions.Return result
    print(var_p(5))  #


# %%NBQA-CELL-SEPfaab7c
powers = []
for i in (1, 2):

    def inner(var_x):
        return var_x**i

    powers.append(inner)
dis.dis(powers[0])
for var_p in powers:
    print(var_p(5))


# %%NBQA-CELL-SEPfaab7c
def plus_one(var_x: int) -> int:
    return var_x + 1


dis.dis(plus_one)


# %%NBQA-CELL-SEPfaab7c
#  Например, создадим MD5-хэш строки:
data = "Hello, Python!"
hash_object = hashlib.md5(data.encode())
md5_hash = hash_object.hexdigest()

print(md5_hash)


# %%NBQA-CELL-SEPfaab7c
# Генерация ключа
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Шифрование данных
data = b"Hello, Python!"
encrypted_data = cipher_suite.encrypt(data)

# Дешифрование данных
decrypted_data = cipher_suite.decrypt(encrypted_data)

print(encrypted_data)
print(decrypted_data)


# %%NBQA-CELL-SEPfaab7c
# Генерация пары ключей
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)
public_key = private_key.public_key()

# Шифрование данных
data = b"Hello, Python!"
encrypted_data = public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Дешифрование данных
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print(encrypted_data)
print(decrypted_data)


# %%NBQA-CELL-SEPfaab7c
# Пример создания безопасного соединения с использованием ssl:

hostname = "www.python.org"
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())


# %%NBQA-CELL-SEPfaab7c
# Аннотация переменных

# чтобы указать тип переменной в Python, просто добавьте двоеточие с пробелом,
# за которым следует тип (str, int, List[] и т. д.), сразу после имени переменной

name: str = "Tommy"
age: int = 24
height_in_meters: float = 1.7
colleagues: List[str] = ["Alicia", "John"]


# %%NBQA-CELL-SEPfaab7c
# Аннотация функций

# чтобы указать тип возврата (return), мы добавляем стрелку –>, за которой следует его тип.
#


def convert_celcius_to_fahrenheit(celcius_temp: float) -> float:
    return (celcius_temp * 9 / 5) + 32


def get_email_status(
    subject: str, body: str, recipients: List[str], cache: Dict[str, str]
) -> bool:
    # пропущено для краткости
    return True  # или False
