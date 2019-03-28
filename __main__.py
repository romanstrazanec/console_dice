from os import system, name
from math import ceil
from random import random

from dice import Dice


def clear_screen():
    system("cls" if name == 'nt' else "clear")
    print("[n]umber of dices | [l]ose | [q]uit")
    print()


def roll():
    return int(random() * 6) + 1


def split_in_rows(l, n, print_func):
    for i in range(0, len(l), n):
        print_func(l[i:i + n])
        print()


def display(dices, spaces=3):
    if type(dices) == int:
        rolled = [roll() for _ in range(dices)]
        split_in_rows(rolled, ceil(len(rolled) ** .5), display)

    elif type(dices) == list:
        for n_layer in range(len(Dice.layers)):
            for n in dices:
                print(Dice(n).layer(n_layer), end=" " * spaces)
            print()


def ask_ndices():
    while True:
        try:
            i = input("n <<< ")
            return abs(int(i))
        except ValueError:
            print("Should be an integer!")


def throw(dices, times=10):
    for _ in range(times):
        clear_screen()
        display(dices)
    print()


def play():
    dices = 0
    while True:
        while dices <= 0:
            dices = ask_ndices()

        throw(dices)

        i = input(">>> ")
        if i == "q":
            clear_screen()
            break

        if i == "l":
            dices -= 1 if dices > 0 else 0

        if i == "n":
            dices = ask_ndices()


if __name__ == "__main__":
    play()
