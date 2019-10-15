#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Translate-toolkit used to parse TMX file.
http://docs.translatehouse.org/projects/translate-toolkit/en/latest/api/storage.html#module-translate.storage.tmx
'''

import sys
from translate.storage.tmx import tmxfile

'''
Object for each Japanese-English segment.
Includes actual segment text and numerous variables for QA checks.
'''
class Segment():
    def __init__(self, jap_text, eng_text, jap_nums, eng_nums, error_found, missing_nums, extra_nums, double_space, repeated_word, repeated_words, unpaired_symbol, missing_symbols, untranslated_seg):
        self.jap_text = jap_text # String, Japanese text
        self.eng_text = eng_text # String, English text
        self.jap_nums = jap_nums # List of ints, numbers extracted from Japanese text
        self.eng_nums = eng_nums # List of ints, numbers extracted from English text
        self.error_found = error_found # Boolean = True if any errors are found
        self.missing_nums = missing_nums # List of ints, numbers missing from English text
        self.extra_nums = extra_nums # List of ints, extra numbers found in English text
        self.double_space = double_space # Boolean, True if double spaces found
        self.repeated_word = repeated_word # Boolean, True if repeated words found
        self.repeated_words = repeated_words # List of strings, repeated words if any found
        self.unpaired_symbol = unpaired_symbol # Boolean, True if unpaired symbols found (parentheses etc.)
        self.missing_symbols = missing_symbols # List of missing paired symbols if any found
        self.untranslated_seg = untranslated_seg # Boolean, True if no English text is found

'''
Function for gathering translations segments from a TMX file.
'''
def gather_segments():

    file = sys.argv[-1] # Gets last command line argument (filename here)
    with open(file, 'rb') as f:
        tmx_file = tmxfile(f)

    segments = [] # List of Segment objects

    # Iterates oves TMX file and extracts text from segments.
    for node in tmx_file.unit_iter():
        jap_text = node.getsource()
        eng_text = node.gettarget()
        segment = Segment(jap_text, eng_text, [], [], False, [], [], False, False, [], False, [], False)
        segments.append(segment)

    return segments