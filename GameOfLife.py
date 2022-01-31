import os
from typing import *
from random import randint
from time import sleep


def resize(width: int, height: int) -> Tuple[int, int]:
    if width < 10:
        width = 10
    if width > 75:
        width = 75

    if height < 10:
        height = 10
    if height > 45:
        height = 45

    return width, height


def randomly_fill_matrix(matrix: List[List[int]]) -> List[List[int]]:
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            life = randint(0, 10)
            if life == 10:
                matrix[y][x] = 1
    return matrix


def count_neighbors(y: int, x: int, matrix: List[List[int]]) -> int:
    result = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not(i == 0 and j == 0):

                if y + i != len(matrix) and x + j != len(matrix[0]):
                    if matrix[y + i][x + j] == 1:
                        result += 1

                elif y + i == len(matrix) and x + j == len(matrix[0]):
                    if matrix[0][0] == 1:
                        result += 1

                elif y + i != len(matrix) and x + j == len(matrix[0]):
                    if matrix[y + i][0] == 1:
                        result += 1

                elif y + i == len(matrix) and x + j != len(matrix[0]):
                    if matrix[0][x + j] == 1:
                        result += 1
    
    return result


def change_state(matrix: List[List[int]]) -> List[List[int]]:
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i].copy())

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            neighbors = count_neighbors(y, x, matrix)

            if matrix[y][x] == 0:
                if neighbors == 3:
                    new_matrix[y][x] = 1

            else:
                if neighbors < 2 or neighbors > 3:
                    new_matrix[y][x] = 0
    
    return new_matrix


def draw(matrix: List[List[int]]) -> None:
    for row in matrix:
        for cell in row:
            if cell == 1:
                print('██', sep='', end='')
            else:
                print('  ', sep='', end='')
        print()


def game_of_life(width: int, height: int) -> None:
    width, height = resize(width, height)

    os.system('mode ' + str(width*2 + 1) + ',' + str(height + 1))

    matrix = []
    for i in range(height):
        matrix.append([0] * width)

    matrix = randomly_fill_matrix(matrix)

    while True:
        os.system('cls')
        matrix = change_state(matrix)
        draw(matrix)
        sleep(0.5)


if __name__ == "__main__":
    game_of_life(200, 200)
