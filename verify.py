#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from colorama import init
from colorama import Fore


init()  # From colorama, used to activate colored output on Windows OS


def user_input_check():
    '''
    Function for validating user input entered at the command line.
    '''
    input_verified = True

    # If two arguments have not been entered
    if len(sys.argv) != 2:
        input_verified = False
        print(Fore.RED + 'Incorrect number of arguments entered.')

    # If two arguments have been entered
    else:
        file = sys.argv[1]

        # If the second argument is not a tmx file
        if not file.lower().endswith('.tmx'):
            input_verified = False
            print(Fore.RED + 'Incorrect file type. Only tmx files accepted.')

    if not input_verified:
        print(Fore.RED + 'Please try again using the following format.')
        print(Fore.CYAN + 'python3 checker.py yourfile.tmx')

    return input_verified
