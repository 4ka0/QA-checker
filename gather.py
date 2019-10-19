#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Translate-toolkit used to parse TMX file.
http://docs.translatehouse.org/projects/translate-toolkit/en/latest/api/storage.html#module-translate.storage.tmx
'''


import sys
from translate.storage.tmx import tmxfile


class Segment():
    '''
    Used to create an object for each Japanese-English segment.
    Includes actual segment text and numerous variables for QA checks.
    '''

    def __init__(self, jap_text, eng_text, jap_nums, eng_nums, error_found, missing_nums, extra_nums, double_space_found, repeated_word_found, repeated_words, unpaired_symbol_found, unpaired_symbols, untranslated_seg):
        self.jap_text = jap_text # String, Japanese text
        self.eng_text = eng_text # String, English text
        self.jap_nums = jap_nums # List of ints, numbers extracted from Japanese text
        self.eng_nums = eng_nums # List of ints, numbers extracted from English text
        self.error_found = error_found # Boolean = True if any errors are found
        self.missing_nums = missing_nums # List of ints, numbers missing from English text
        self.extra_nums = extra_nums # List of ints, extra numbers found in English text
        self.double_space_found = double_space_found # Boolean, True if double spaces found
        self.repeated_word_found = repeated_word_found # Boolean, True if repeated words found
        self.repeated_words = repeated_words # List of strings, repeated words if any found
        self.unpaired_symbol_found = unpaired_symbol_found # Boolean, True if unpaired symbols found (parentheses etc.)
        self.unpaired_symbols = unpaired_symbols # List of missing paired symbols if any found
        self.untranslated_seg = untranslated_seg # Boolean, True if no English text is found



def gather_segments():
    '''
    Function for gathering translations segments from a TMX file.
    '''

    file = sys.argv[-1] # Gets last command line argument (filename)
    with open(file, 'rb') as f:
        tmx_file = tmxfile(f)

    segments = [] # List of Segment objects

    # Iterates over TMX file and extracts text from segments.
    for node in tmx_file.unit_iter():
        jap_text = node.getsource()
        eng_text = node.gettarget()
        segment = Segment(jap_text, eng_text, [], [], False, [], [], False, False, [], False, [], False)
        segments.append(segment)

    return segments
