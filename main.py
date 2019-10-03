#!/usr/bin/env python3

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
# import ordinals
import words
import output

# Get the last argument (filename) from the command line.
file = sys.argv[-1] 

# Only proceed if the provided file is a TMX file.
if file.lower().endswith(".tmx"):

    # Gather Japanese and English translation segments.
    segments = gather.gatherSegments()

    # Check for missing numbers appearing as digits.
    segments = digits.digitCheck(segments)

    # Check for double spaces
    segments = spaces.doubleSpaceCheck(segments)

    # Check for repeated words

    # Check for unpaired symbols such as quotation marks, brackets, parentheses, etc.

    # Check for untranslated segments
    

    # output final results
    output.outputResults(segments)

else:
    print("\nINCORRECT FILE TYPE. ONLY TMX FILES ACCEPTED.\n")
