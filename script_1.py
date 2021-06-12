import time
import random
import os

data = [
    ['X' for _ in range(14)] for i in range(10)
]


def print_field(data: list):
    for row in data:
        print()
        for item in row:
            print(item, end=' ')
    print()


def update_field(x_pos, y_pos):
    data[y_pos][x_pos] = 'O'


x = 0
y = 0
while True:
    time.sleep(.01)
    os.system('CLS')
    update_field(x, y)
    print_field(data)
    x += 1
    if x == 14: y += 1
    if x == 14: x = 0
    if y == 10: y = 0




