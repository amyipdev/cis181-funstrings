#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

def serrep(render_screen):
    string = render_screen("Welcome to Search and Replace!\n\n"\
                           "Please enter your primary string...")
    substring = render_screen("Now, enter your substring...")
    render_screen(f"First string: {string}\n\n"\
                  f"Substring: {substring}\n\n"\
                  f"endswith(): {string.endswith(substring)}\n"\
                  f"find(): {string.find(substring)}\n"\
                  f"startswith(): {string.startswith(substring)}\n\n"\
                  f"Press enter/return to exit to main menu.")
