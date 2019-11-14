# -*- coding: utf-8 -*-

from colorama import init
from colorama import Fore


init()  # From colorama, used to activate colored output on Windows OS


def user_input_check(argv):
    '''
    Function for validating user input entered at the command line.
    Two arguments should have been entered.
    The second argument should be a tmx file.
    '''
    input_verified = True

    # If two arguments have not been entered
    if len(argv) != 2:
        input_verified = False
        print(Fore.RED + 'Incorrect number of arguments entered.')

    # If two arguments have been entered
    else:
        file = argv[1]

        # If the second argument is not a tmx file
        if not file.lower().endswith('.tmx'):
            input_verified = False
            print(Fore.RED + 'Incorrect file type. Only tmx files accepted.')

    if not input_verified:
        print(Fore.RED + 'Please try again using the following format.')
        print(Fore.CYAN + 'python3 checker.py yourfile.tmx')

    '''
    CHECK FILE ACTUALLY EXISTS HERE RATHER THAN IN GATHER
    USE FOLLOWING CODE
    DELETE CORRESPONDING SECTION FROM GATHER
    THEN RETEST VERIFY
    '''
    '''
    file = argv[1]
    try:
        with open(file, 'rb') as f:
            tmx_file = tmxfile(f)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    '''


    return input_verified
