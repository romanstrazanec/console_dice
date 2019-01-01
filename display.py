from os import system, name
from math import ceil
from random import random

from dice import Dice


def clear_screen():
    system("cls" if name == 'nt' else 'clear')


def roll():
    return int(random() * 6) + 1


def split_in_rows(l, n, print_func):
    for i in range(0, len(l), n):
        print_func(l[i:i + n])
        print()


def display(l, s=3):
    # print(type(l), print(l))
    if type(l) == int:
        rolled = [roll() for _ in range(l + 1)]
        split_in_rows(rolled, ceil(len(rolled) ** .5), display)

    elif type(l) == list:
        for n_layer in range(len(Dice.layers)):
            for n in l:
                print(Dice(n).layer(n_layer), end=" " * s)
            print()


def play():
    n = 5
    while True:
        for _ in range(10):
            clear_screen()
            display(n)
        print()

        i = input("[l]ose? | [q]uit? ")
        if i == "q":
            clear_screen()
            break

        if i == "l":
            n = (n - 1) % 6


if __name__ == "__main__":
    play()
