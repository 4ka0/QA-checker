#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Program for performing various QA checks on a Jap>Eng tmx file.
Checks for the following issues:
    Inconsistent numbers (missing or extra numbers)
    Double spaces etc.
    Repeated words
    Unpaired symbols such as parentheses
    Untranslated segments
Takes three arguments to execute from the command line:
    python3 checker.py yourfile.tmx
Results sent to stdout.
'''

import sys
import verify_input
import gather
import numbers
import spaces
import repeaters
import unpaired
import refnums
import output


'''
Include main()?
https://realpython.com/python-main-function/
'''

# Only proceeds if True is returned
if verify_input.user_input_check():

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

    # Check for untranslated segments
        # Empty segs
        # Segs containing only whitespace etc.
        # Segs that are too short to be complete translation,
            # compare char count of source and word count of target?

    # Check source/target segment inconsistencies

    # Check leading and trailing whitespace

    # Check punctuation at end (compared to source seg)

    # Check starting capitalization

    # Check for mathematical expressions
    '''
    https://stackoverflow.com/questions/51439794/get-mathematical-expressions-single-letters-numbers-equations-using-regex
    Look at Japanese text for substrings given in the "units to be ignored" list in refnums.
    '''

    # Check key vocab appears

    # output final results
    output.output_results(segments)
