from random import randint
from typing import Callable
from sys import stderr


def gen_menu(options: list[tuple[str, Callable]]):
    for idx, i in enumerate(options):
        print(f"\t[{idx}] {i[0]}")
    print()


def main() -> None:
    OPTIONS = [
        ("Random guesser", random_guesser),
        ("Exit", exit)
    ]
    gen_menu(OPTIONS)
    while True:
        option = int(input())
        if option >= len(OPTIONS):
            print("ERROR: invalid option", file=stderr)
        OPTIONS[option][1]()


def random_guesser() -> None:
    g = int(input("your guess: "))
    n = randint(0, 100)
    while True:
        if g > n:
            print("g is greater than n")
            g = int(input("your guess: "))
            continue
        elif g < n:
            print("g is less than n")
            g = int(input("your guess: "))
            continue
        elif g == n:
            print("g is equal to n")
            return


if __name__ == "__main__":
    main()
