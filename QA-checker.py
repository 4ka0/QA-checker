#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Program for performing various QA checks on a Jap>Eng TMX file.
Checks for the following issues:
    Inconsistent numbers (missing or extra numbers)
    Double spaces etc.
    Repeated words
    Unpaired symbols such as parentheses
    Untranslated segments
Takes three arguments to execute from the command line:
    python3 QA-checker.py <your tmx file>
Results sent to stdout.
'''

import sys
from colorama import init
from colorama import Fore
import gather
import numbers
import spaces
import repeaters
import unpaired
import refnums
import output

init() # To activate colored output on Windows OS


'''
!!! USE ARGPARSE !!!
https://stackoverflow.com/questions/7427101/simple-argparse-example-wanted-1-argument-3-results
'''

# Get the last argument (filename) from the command line.
file = sys.argv[-1]

'''
Check input more thoroughly, use argparse?
https://docs.python.org/dev/library/argparse.html
    arg1 should be python3?
    arg2 should be QA-checker.py
    arg3 should be .tmx
'''

'''
Include main()?
https://realpython.com/python-main-function/
'''


# If no file has been specified on the command line.
if file == 'QA-checker.py':
    print(Fore.RED + '\nNO TRANSLATION FILE SPECIFIED.')
    print(Fore.RED + 'PLEASE SPECIFY A TMX FILE IN THE FOLLOWING WAY.')
    print(Fore.CYAN + 'python3 QA-checker.py file.tmx\n')

# Only proceed if the provided file is a TMX file.
elif file.lower().endswith('.tmx'):

    # Check given file actually exists


    # Gather Japanese and English translation segments.
    segments = gather.gather_segments()

    # Check for missing/extra numbers appearing as numbers.
    segments = numbers.missing_number_check(segments)
    segments = numbers.extra_number_check(segments)

    # Check for double spaces
    segments = spaces.double_space_check(segments)

    # Check for repeated words
    segments = repeaters.single_word_check(segments)
    segments = repeaters.double_word_check(segments)

    # Check for unpaired symbols such as parentheses
    segments = unpaired.unpaired_symbol_check(segments)

    # Check for missing reference numbers (符号 in Japanese patents)
    segments = refnums.refnum_check(segments)

    # Check for mathematical expressions
    '''
    https://stackoverflow.com/questions/51439794/get-mathematical-expressions-single-letters-numbers-equations-using-regex
    Look at Japanese text for substrings given in the "units to be ignored" list in refnums.
    '''

    # Check for untranslated segments
    # Empty or containing only whitespace or no letters
    # Too short to be complete translation, compare char count of source and word count of target?

    # Check source/target segment inconsistencies

    # Check leading and trailing whitespace

    # Check punctuation at end (compared to source seg)

    # Check starting capitalization

    # Check key vocab appears

    # output final results
    output.output_results(segments)

else:
    print(Fore.RED + '\nINCORRECT FILE TYPE. ONLY TMX FILES ARE ACCEPTED.')
    print(Fore.RED + 'PLEASE SPECIFY A TMX FILE IN THE FOLLOWING WAY.')
    print(Fore.CYAN + 'python3 QA-checker.py file.tmx\n')
