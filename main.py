#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Checks if numbers are consistent between source and target segments TMX file.
A Japanese>English TMX file is assumed here.
Requires three arguments to execute:
python3 number-checker.py filename
Results sent to stdout.
'''

import sys
import gather
import digits
import spaces
import output

# Get the last argument (filename) from the command line.
file = sys.argv[-1] 

# Only proceed if the provided file is a TMX file.
if file.lower().endswith(".tmx"):

    # Gather Japanese and English translation segments.
    segments = gather.gather_segments()

    # Check for missing numbers appearing as digits.
    segments = digits.digit_check(segments)

    # Check for extra numbers in the English text.
    # segments = digits.digit_check(segments)

    # Check for double spaces
    segments = spaces.double_space_check(segments)

    # Check for repeated words

    # Check for unpaired symbols such as quotation marks, brackets, parentheses, etc.

    # Check for untranslated segments

    # output final results
    output.output_results(segments)

else:
    print("\nINCORRECT FILE TYPE. ONLY TMX FILES ACCEPTED.\n")
