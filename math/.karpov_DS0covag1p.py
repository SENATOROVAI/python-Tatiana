# %%NBQA-CELL-SEPfaab7c
hash(0x8EFDCDF2)


# %%NBQA-CELL-SEPfaab7c
c = (a**2 + b**2) ** 0.5


# %%NBQA-CELL-SEPfaab7c
result = father_age - 2 * (son_age)


# %%NBQA-CELL-SEPfaab7c
# https://lab.karpov.courses/learning/243/module/2453/lesson/24444/70058/305938/
from collections import deque


def find_new_neighbors(coordinate):
    """
    :param coordinate: tupple = (int, int)
    :return: None
    :side effects: modify added_cells, queue and parents
    """
    for j, k in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = coordinate[0] + j, coordinate[1] + k
        if (
            0 <= x < size
            and 0 <= y < size
            and (x, y) not in added_cells
            and city_map_list[x][y] == 1
        ):
            added_cells.add((x, y))
            queue.append((x, y))
            parents[(x, y)] = coordinate


def write_path(end, start):
    """
    :param end: tupple = (int, int)
    :param start: tupple = (int, int)
    :return: None
    :side effects: modify variable - path
    """
    x, y = end
    next_cell = parents.get((x, y))
    while next_cell != start:
        path.append(next_cell)
        next_cell = parents.get(next_cell)


# в постановке задачи сперва задаются столбики, потом строки,
# переставим по-питонячи: сперва строки, потом столбики
courier_location = (courier_location[1], courier_location[0])
orders_location = [(j, i) for i, j in orders_location]

# наш путь сохранять будем в:
route = []

# к адресам доставки добавим исходную точку
locations = orders_location.insert(0, courier_location)

size = len(city_map_list)

# алгоритм BFS на всем поле (потом надо будет сделать до ближайшей точки).
# В словаре parents запоминаем откуда пришли в данную ячейку
# и по этому словарю восстанавливаем путь до первого адреса доставки.
# Записав путь, обнуляем все и запускаем BFS уже от первого адреса доставки.
# Ищем путь до второго адреса. И т.д.
for i in range(1, len(orders_location)):
    parents = {}
    queue = deque()
    added_cells = set()
    path = []

    added_cells.add(orders_location[i - 1])
    queue.append(orders_location[i - 1])

    while queue:
        find_new_neighbors(queue.popleft())

    write_path(orders_location[i], orders_location[i - 1])
    path.append(orders_location[i - 1])
    route.extend(path[::-1])

# не забываем последний адрес доставки добавить
route.append(orders_location[-1])

# из питонячей "системы координат" переходим в "геометрическую"
route = [(j, i) for i, j in route]

print(route)
