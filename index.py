#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

def index(render_screen):
    string = render_screen("Welcome to Indexing!\n\n"\
                           "Enter a string to index...")
    inx = int(render_screen(f"Now, enter the index for the string...\n\t'{string}'"))
    try:
        render_screen(f"Index {inx} of\n\t{string}\nis '{string[inx]}'\n\n"\
                      f"Press return/enter to go to the main menu.")
    except IndexError:
        render_screen("Could not index! Press return/enter.")
