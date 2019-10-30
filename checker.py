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

import verify
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

if verify.user_input_check():

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

    # Check for missing reference numbers
    segments = refnums.refnum_check(segments)

    # output final results
    output.output_results(segments)
