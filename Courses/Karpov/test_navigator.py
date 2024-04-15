from typing import List, Tuple

city_map = [
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

start_point = (4, 2)  # start (format(x,y))
target_point = [(6, 0), (1, 4), (2, 2)]  # target  (format(x,y))

start_point: List[int] = [
    start_point[1],
    start_point[0],
]  # (reverse start point (to get format(y-rows,x-columns)))
print(start_point, " " * 4, sep="\n")

target_point_to_list = []  # reverse target point to get format(y-rows,x-columns)))
for coordinate in target_point:
    target_point_to_list.append([coordinate[1], coordinate[0]])

print(f"Targets are: {target_point_to_list}", " " * 4, sep="\n")

route = [tuple(start_point)]

# river_coordinates
river_coordinates = [
    (row_idx, col_idx)
    for row_idx, row in enumerate(city_map)
    for col_idx, value in enumerate(row)
    if value == 0
]

print(f"River coordinates: {river_coordinates}")
print(" " * 4, sep="\n")


def check_move(
    current_route_point: Tuple[int, int],
    potential_step: int,
    moves: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    river_coordinates: List[Tuple[int, int]],
    type_check: str,
) -> bool:
    """
    This function checks if we can do the next step or not
    The goal of this function is to avoid loops and rivers when making moves.

    Arguments of this function are:
    current_route_point: Our current position on the map,
    potential_step: Integer used to change location between rows or columns.
    moves: List of needed tuples where:
    (first -> Tuple[int, int] - position where we start,
    second -> Tuple[int, int] - position where we end,)
    river_coordinates: coordinates of points that have a river (zero value) in it
    type_check: "column" or "row", depending on what type of check for move we need (for rows or for columns).
    """

    if type_check == "row":
        potential_way_row = [
            (current_route_point, (potential_step, current_route_point[1]))
        ]
        return (
            not any(potential_way_row == move for move in moves)
            and potential_way_row[0][1] not in river_coordinates
        )

    elif type_check == "column":
        potential_way_column = [
            (current_route_point, (current_route_point[0], potential_step))
        ]
        return (
            not any(potential_way_column == move for move in moves)
            and potential_way_column[0][0] not in river_coordinates
        )

    return False


moves: List[int] = []

# create an iteration to reach the end of target_point
for i in target_point_to_list:
    moves = []
    # rows direction up_down
    while route[-1][0] != i[0]:
        new_row = (
            route[-1][0] + 1
            if (
                route[-1][0] < i[0]
                and check_move(
                    route[-1], route[-1][0] + 1, moves, river_coordinates, "row"
                )
                and 0 <= route[-1][0] + 1 < len(city_map)
            )
            else (
                route[-1][0] - 1
                if (
                    check_move(
                        route[-1], route[-1][0] - 1, moves, river_coordinates, "row"
                    )
                    and 0 <= route[-1][0] - 1 < len(city_map)
                )
                else route[-1][0]
            )
        )
        if new_row != route[-1][0]:  # Check for row updates
            route.append((new_row, route[-1][1]))
            # print(f"New row :{new_row}")
            moves.append((route[-2], route[-1]))
        else:  # if we can update row from current_pos,skip block for this time and go to next direction
            break

    # column direction left-right
    while route[-1][1] != i[1]:
        new_col = (
            route[-1][1] + 1
            if (
                route[-1][1] < i[1]
                and check_move(
                    route[-1], route[-1][1] + 1, moves, river_coordinates, "column"
                )
                and 0 <= route[-1][1] + 1 < len(city_map[0])
            )
            else (
                route[-1][1] - 1
                if (
                    check_move(
                        route[-1], route[-1][1] - 1, moves, river_coordinates, "column"
                    )
                    and 0 <= route[-1][1] - 1 < len(city_map[0])
                )
                else route[-1][1]
            )
        )

        if new_col != route[-1][1]:  # Check for column updates
            route.append((route[-1][0], new_col))
            # print(f"New col :{new_col}")
            moves.append((route[-2], route[-1]))

        else:  # If we can move, skip this direction and return to previous direction
            break

        print(moves)

        if route[-1] == i:  # Перевірка досягнення поточної цілі
            print("Reached target:", i)
            moves.clear()  # Очищати список moves тільки після досягнення цілі
        else:
            print("Failed to reach target:", i)

for point in route:
    print(f"Our points {point}")

print("" * 4, sep="\n")

print(route)
