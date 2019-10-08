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
    def __init__(self, jap_text = "", eng_text = "", jap_nums = [], eng_nums = [], error_found = False, missing_nums = [], extra_nums = [], double_space = False, repeated_word = False, repeated_words = [], unpaired_symbol = False, untranslated_seg = False):
        self.jap_text = jap_text # Japanese text
        self.eng_text = eng_text # English text
        self.jap_nums = jap_nums # Numbers extracted from Japanese text
        self.eng_nums = eng_nums # Numbers extracted from English text
        self.error_found = error_found # Flag = True if any errors are found
        self.missing_nums = missing_nums # Numbers missing from English text
        self.extra_nums = extra_nums # Extra numbers found in English text
        self.double_space = double_space # Flag = True if double spaces found
        self.repeated_word = repeated_word # Flag = True if repeated words found
        self.repeated_words = repeated_words # List of repeated words if any found
        self.unpaired_symbol = unpaired_symbol # Flag = True if unpaired symbols found (parentheses etc.)
        self.untranslated_seg = untranslated_seg # Flag = True if no English text is found

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
        segment = Segment(jap_text, eng_text)
        segments.append(segment)

    return segments