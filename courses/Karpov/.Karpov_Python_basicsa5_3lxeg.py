# %%NBQA-CELL-SEPfaab7c
import numpy as np


# %%NBQA-CELL-SEPfaab7c
city_map = [
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

start_point = (4, 2)  # start (format(x,y))
target_point = [(6, 0), (1, 4), (2, 2)]  # target  (format(x,y))

start_point = [
    start_point[1],
    start_point[0],
]  # (reverse start point (to get format(y-rows,x-columns)))
print(start_point, " " * 4, sep="\n")


# %%NBQA-CELL-SEPfaab7c
start_point = (4, 2)  # start (format(x,y))
print(start_point)
route = [start_point]  # изменение
print(route)


# %%NBQA-CELL-SEPfaab7c
# Транспонирование сработало


city_map_list = np.array(
    [
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
    ]
)
city_map_list2 = city_map_list.transpose()

city_map_list, "\n", city_map_list2


# %%NBQA-CELL-SEPfaab7c
# Транспонирование сработало!!!


city_map_list = [
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
]

courier_location = (2, 2)  # стартовая позиция курьера
orders_location = [(4, 0), (0, 2), (4, 3)]  # координаты для доставки трех товаров

# route = [
# (3, 2),
# (4, 2),
# (4, 1),
# (4, 0), # адрес доставки
# (4, 1),
# (4, 2),
# (3, 2),
# (2, 2),
# (1, 2),
# (0, 2), # адрес доставки
# (1, 2),
# (2, 2),
# (3, 2),
# (4, 2),
# (4, 3) # адрес доставки
# ]


rows_cnt = len(city_map_list)  # number of rows
cols_cnt = len(city_map_list[0])  # number of columns

new_city_map_list = [
    [0] * rows_cnt for _ in range(cols_cnt)
]  # create matrix with all 0 size:rows_cntx cols_cnt
#
for i in range(rows_cnt):  # i - ,
    for j in range(cols_cnt):  #
        new_city_map_list[j][i] = city_map_list[i][j]  #

for row in new_city_map_list:  #
    print(row)  #


# %%NBQA-CELL-SEPfaab7c
a = (2, 2)
b = [(4, 0), (0, 2), (4, 3)]
a[0] < b[0][0], a[1] > b[0][1]


# %%NBQA-CELL-SEPfaab7c
start_point = list((2, 2))
# start_point, start_point[0]+1


# %%NBQA-CELL-SEPfaab7c
# start_point = list((2,2))
orders_location = [(4, 2), (0, 2), (4, 3)]
cur_point = start_point.copy()
route = [start_point]

for order in orders_location:
    if order not in route:

        for order in range(len(orders_location)):  # order 0...2
            # сравниваем х по тек точке и назначению и смотрим шаг вниз по х == 1
            if (cur_point[0] < orders_location[order][0]) and (
                new_city_map_list[cur_point[0] + 1][cur_point[1]] == 1
            ):  #
                cur_point[0] = cur_point[0] + 1  #
            # сравниваем х по тек точке и целевой и смотрим шаг вверх по х == 1
            if (cur_point[0] > orders_location[order][0]) and (
                new_city_map_list[cur_point[0] - 1][cur_point[1]] == 1
            ):  #
                cur_point[0] = cur_point[0] - 1  #
            # сравниваем х по тек точке и назначению и смотрим шаг вправол по у == 1
            if (
                (cur_point[0] == orders_location[order][0])
                and (cur_point[1] > orders_location[order][1])
                and (new_city_map_list[cur_point[0]][cur_point[1] - 1] == 1)
            ):
                cur_point[1] = cur_point[1] - 1
            # сравниваем х по тек точке и назначению и смотрим шаг влево по у == 1
            if (
                (cur_point[0] == orders_location[order][0])
                and (cur_point[1] < orders_location[order][1])
                and (new_city_map_list[cur_point[0]][cur_point[1] + 1] == 1)
            ):
                cur_point[1] = cur_point[1] + 1

route.append(cur_point)


print(route)  # "True down", cur_point,


# %%NBQA-CELL-SEPfaab7c
# orders_location[order][0]
new_city_map_list[cur_point[0]][cur_point[1] - 1]


# %%NBQA-CELL-SEPfaab7c
s = [(1, 2), (3, 4)]
l = [(4, 5), (6, 7), (8, 9)]
for i in s:
    if i not in l:
        print("+")
else:
    None


# %%NBQA-CELL-SEPfaab7c
cur_point = list(map(int, input().split()))
route = []
orders_location = [(4, 0), (0, 2), (4, 3)]
for (
    i
) in (
    orders_location
):  # пока тек точка == целевой мы ищем путь как только == то переходим к след
    while cur_point != i:  #
        # route.append(cur_point)
        route += list(map(int, input().split()))
    continue


# %%NBQA-CELL-SEPfaab7c
start_point


# %%NBQA-CELL-SEPfaab7c
new_city_map_list[cur_point[0] + 1][
    cur_point[1]
]  # проверяем значение ниже по столбцу == 1
# new_city_map_list[3][2]
cur_point[0] + 1
# cur_point[1]


# %%NBQA-CELL-SEPfaab7c
# делаем шаг =  перезаписываем cur_point и добавляем его в route
cur_point[0] = cur_point[0] + 1
print(cur_point)


# %%NBQA-CELL-SEPfaab7c
target_point = [(6, 0), (1, 4), (2, 2)]  # target  (format(x,y))

target_point_to_list = []  # reverse target point to get format(y-rows,x-columns)))
for coordinate in target_point:
    target_point_to_list.append([coordinate[1], coordinate[0]])

print(f"Targets are: {target_point_to_list}")  #  , " " * 4, sep="\n" изменение
