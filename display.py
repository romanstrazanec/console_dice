from os import system
from random import random


def cls():
    system("cls")


def roll():
    return int(random() * 6) + 1


def display(l, s=3):
    # print(type(l), print(l))
    if type(l) == int:
        k = [roll() for _ in range(l + 1)]
        display(k[:3])
        print()
        if l > 2:
            display(k[3:])

    elif type(l) == list:
        for _ in l:
            print("+---------+", end=" " * s)
        print()

        for _ in l:
            print("|         |", end=" " * s)
        print()

        for n in l:
            if n == 1:
                print("|         |", end=" " * s)
            if n == 2:
                print("|     o   |", end=" " * s)
            if n == 3:
                print("|     o   |", end=" " * s)
            if n == 4:
                print("|  o   o  |", end=" " * s)
            if n == 5:
                print("|  o   o  |", end=" " * s)
            if n == 6:
                print("|  o   o  |", end=" " * s)
        print()

        for n in l:
            if n == 1:
                print("|    o    |", end=" " * s)
            if n == 2:
                print("|         |", end=" " * s)
            if n == 3:
                print("|    o    |", end=" " * s)
            if n == 4:
                print("|         |", end=" " * s)
            if n == 5:
                print("|    o    |", end=" " * s)
            if n == 6:
                print("|  o   o  |", end=" " * s)
        print()

        for n in l:
            if n == 1:
                print("|         |", end=" " * s)
            if n == 2:
                print("|   o     |", end=" " * s)
            if n == 3:
                print("|   o     |", end=" " * s)
            if n == 4:
                print("|  o   o  |", end=" " * s)
            if n == 5:
                print("|  o   o  |", end=" " * s)
            if n == 6:
                print("|  o   o  |", end=" " * s)
        print()

        for _ in l:
            print("|         |", end=" " * s)
        print()

        for _ in l:
            print("+---------+", end=" " * s)
        print()


def play():
    n = 5
    while True:
        for _ in range(10):
            cls()
            display(n)
        print()

        i = input("[l]ose? | [q]uit? ")
        if i == "q":
            cls()
            break
        if i == "l":
            n = (n - 1) % 6


if __name__ == "__main__":
    play()
