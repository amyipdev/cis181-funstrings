#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

import os

import slicing
import concat
import index
import testing
import modi
import serrep

def q(render_screen):
    pass

FUNCS = {
    "q": q,
    "x": slicing.slicing,
    "c": concat.concat,
    "i": index.index,
    "t": testing.testing,
    "m": modi.modi,
    "s": serrep.serrep
}

# Renders a screen with nice formatting, returning user input.
# Should be continuously run until the end of the program.
# Lines must be no longer than 80 columns wide, 18 rows long
def render_screen(text: str) -> str:
    # Presumes the "Standard Unix Terminal" terminal size
    # May render incorrectly if not performed on 80x24
    cls()
    print(f"{''.join('=' for n in range(80))}\n")
    p = text.splitlines()
    for l in p:
        print(l)
    print("".join("\n" for z in range(18 - len(p))))
    print(f"\n{''.join('=' for n in range(80))}")
    return input("lc8$ ")


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # Presumes the "Standard Unix Terminal" terminal size
    # May render incorrectly if not performed on 80x24
    render_screen("Hello! Welcome to TextEngine 3000+, the premier text engine!\n\n"\
                      "Please press 'enter' or 'return' to continue.")
    operation = ""
    while operation != "q":
        operation = render_screen("Please choose an application:\n\n"\
                                  "q - Quit this app\n"\
                                  "x - Slicing\n"\
                                  "c - Concatenation\n"\
                                  "i - Indexing\n"\
                                  "t - Testing\n"\
                                  "m - Modification\n"\
                                  "s - Search and Replace\n")
        try:
            FUNCS[operation](render_screen)
        except KeyError:
            render_screen("Unknown, please press return/enter to try again.")
    cls()


if __name__ == "__main__":
    main()
