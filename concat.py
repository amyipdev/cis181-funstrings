#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

def concat(render_screen):
    s1 = render_screen("Welcome to Concatenate!\n\n"\
                       "First, enter one string...")
    s2 = render_screen("Now, enter another...")
    render_screen(f"Tada!\n\nFirst string: {s1}\n\n"\
                  f"Second string: {s2}\n\n"\
                  f"And together: {s1.join(s2)}\n\n"
                  f"Press enter/return to go to the main menu.")
