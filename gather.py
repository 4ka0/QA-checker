#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from colorama import Fore
from translate.storage.tmx import tmxfile


class Segment():
    '''
    Used to create an object for each Japanese-English segment.
    Includes actual segment text and numerous variables for QA checks.
    '''

    def __init__(self, jap_text, eng_text, jap_nums, eng_nums,
                 error_found, missing_nums, extra_nums,
                 consecutive_space_found, leading_space_found,
                 trailing_space_found, capitalization_error_found,
                 trailing_punctuation_error, repeated_word_found,
                 repeated_words, unpaired_symbol_found,
                 unpaired_symbols, jap_refnums, eng_refnums,
                 missing_refnums, extra_refnums, untranslated_seg):
        # String, Japanese text
        self.jap_text = jap_text
        # String, English text
        self.eng_text = eng_text
        # List of ints, numbers extracted from Japanese text
        self.jap_nums = jap_nums
        # List of ints, numbers extracted from English text
        self.eng_nums = eng_nums
        # Boolean = True if any errors are found
        self.error_found = error_found
        # List of ints, numbers missing from English text
        self.missing_nums = missing_nums
        # List of ints, extra numbers found in English text
        self.extra_nums = extra_nums
        # Boolean, True if consecutive spaces found
        self.consecutive_space_found = consecutive_space_found
        # Boolean, True if leading space found
        self.leading_space_found = leading_space_found
        # Boolean, True if trailing space found
        self.trailing_space_found = trailing_space_found
        # Boolean, True if first word in target text is not capitalized
        self.capitalization_error_found = capitalization_error_found
        # Boolean, True if first word in target text is not capitalized
        self.trailing_punctuation_error = trailing_punctuation_error
        # Boolean, True if repeated words found
        self.repeated_word_found = repeated_word_found
        # List of strings, repeated words if any found
        self.repeated_words = repeated_words
        # Boolean, True if unpaired symbols found (parentheses etc.)
        self.unpaired_symbol_found = unpaired_symbol_found
        # List of missing paired symbols if any found
        self.unpaired_symbols = unpaired_symbols
        # List of reference numbers extracted from Japanese text
        self.jap_refnums = jap_refnums
        # List of reference numbers extracted from English text
        self.eng_refnums = eng_refnums
        # Counter objects of reference numbers missing from
        # the English text
        self.missing_refnums = missing_refnums
        # Counter objects of extra reference numbers found in
        # the English text
        self.extra_refnums = extra_refnums
        # Boolean, True if no English text is found
        self.untranslated_seg = untranslated_seg


def gather_segments():
    '''
    Function for gathering translations segments from a tmx file.
    Translate-toolkit used to parse tmx file.
    http://docs.translatehouse.org/projects/translate-toolkit/en/latest/api/storage.html#module-translate.storage.tmx
    '''

    file = sys.argv[1]

    try:
        with open(file, 'rb') as f:
            tmx_file = tmxfile(f)
    except:
        print(Fore.RED + 'File not found.')
        quit()
    else:
        segments = []  # Used as list of Segment objects
        for node in tmx_file.unit_iter():
            jap_text = node.getsource()
            eng_text = node.gettarget()
            segment = Segment(jap_text, eng_text, [], [], False, [], [],
                              False, False, False, False, False, False,
                              [], False, [], [], [], {}, {}, False)
            segments.append(segment)

    return segments
