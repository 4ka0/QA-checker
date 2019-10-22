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
import gather
import numbers
import spaces
import repeaters
import unpaired
import alphanums
import output


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
    print('\nNO TRANSLATION FILE SPECIFIED.')
    print('PLEASE SPECIFY A TMX FILE IN THE FOLLOWING WAY.')
    print('python3 QA-checker.py file.tmx\n')

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

    # Check for missing alphanumerical combinations (e.g. 符号 refnums)
    segments = alphanums.alphanum_check(segments)

    # Check mathematical formulas match

    # Check key vocab appears

    # Check for untranslated segments

    # output final results
    output.output_results(segments)

else:
    print('\nINCORRECT FILE TYPE. ONLY TMX FILES ARE ACCEPTED.')
    print('PLEASE SPECIFY A TMX FILE IN THE FOLLOWING WAY.')
    print('python3 QA-checker.py file.tmx\n')
