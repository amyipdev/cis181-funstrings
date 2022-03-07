#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

def modi(render_screen):
    string = render_screen("Welcome to Modifications!\n\n"\
                           "Please enter a string to show example mod functions.")
    render_screen(f"You entered: {string}\n\n"\
                  f"lower(): {string.lower()}\n"\
                  f"lstrip(): {string.lstrip()}\n"\
                  f"rstrip(): {string.rstrip()}\n"\
                  f"strip(): {string.strip()}\n"\
                  f"upper(): {string.upper()}\n\n"
                  f"Press enter/return to exit to main menu.")
