#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

def testing(render_screen):
    string = render_screen("Welcome to Testing!\n\n"\
                           "Enter a string to test.")
    render_screen(f"You entered: {string}\n\n"\
                  f"isalnum(): {string.isalnum()}\n"\
                  f"isalpha(): {string.isalpha()}\n"\
                  f"isdigit(): {string.isdigit()}\n"\
                  f"islower(): {string.islower()}\n"\
                  f"isspace(): {string.isspace()}\n"\
                  f"isupper(): {string.isupper()}\n\n"\
                  f"Press return/enter to exit to main menu.")
