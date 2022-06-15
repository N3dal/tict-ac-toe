#!/usr/bin/python3
# -----------------------------------------------------------------
# simple tic tac toe game.
#
#
#
# Author:N84.
#
# Create Date:Thu Apr  7 15:27:45 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

from os import name as OS_NAME
from os import system
from time import sleep
from random import randint


# link for lines that i used for drawing the game map:
# https: // en.wikipedia.org/wiki/Box-drawing_character


# possible moves for user or python to win.
MOVES_TO_WIN = [
    # horizontal moves to win.
    ([0, 0], [0, 1], [0, 2]),
    ([1, 0], [1, 1], [1, 2]),
    ([2, 0], [2, 1], [2, 2]),

    # vertical moves to win.
    ([0, 0], [1, 0], [2, 0]),
    ([0, 1], [1, 1], [2, 1]),
    ([0, 2], [1, 2], [2, 2]),

    # diagonal moves to win.
    ([0, 0], [1, 1], [2, 2]),
    ([0, 2], [1, 1], [2, 0])

]


def clear():
    """wipe the terminal."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


def create_game_map(gameMap):
    """draw the game map"""

    game_map = """
╭───┬───┬───╮
│ {0} │ {1} │ {2} │
├───┼───┼───┤
│ {3} │ {4} │ {5} │
├───┼───┼───┤
│ {6} │ {7} │ {8} │
╰───┴───┴───╯
""".format(*sum(gameMap, []))
    print(game_map)


def get_usr_input(msg: str):
    """"""

    return input(msg).strip().lower()


def set_characters():
    """ask the users about the character they want,
    to play with it and get it from them, and select,
    character for python too depending on the user character.

    simply-out get the users character by asking them.
    return tuple contain two strings,
    values one for user-char and the another,
    one for python-char."""

    while (usr_char := get_usr_input("Choose 'X' or 'O': ")
           .strip()
           .lower()
           ) not in ('x', 'o'):
        # keep asking the user.
        usr_char = get_usr_input("Choose 'X' or 'O': ").strip().lower()

    return usr_char, ('x' if usr_char == 'o' else 'o')


def main():
    u, p = set_characters()
    print(f"'usr: {u}', py: '{p}'")


if __name__ == "__main__":
    main()
