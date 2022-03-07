#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

def slicing(render_screen):
    val = render_screen("Welcome to Slicing!\n\n"\
                        "Please input a value to chop up.")
    start = render_screen(f"You entered: {val}\n\n"\
                          f"Where would you like to start slicing from? (inclusive)")
    end = render_screen(f"Where would you like to end slicing? (exclusive)")
    render_screen(f"Your original text was: {val}\n\n"\
                  f"Your slice query was: {start}:{end}\n\n"\
                  f"Your final result is: {val[int(start):int(end)]}\n\n"\
                  f"Press enter/return to go back to the main menu.")
