#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def leading_capital_check(segments):
    '''
    Function for checking if the first word in the target text
    has been capitalized.
    '''
    for segment in segments:
        # Only check if text is present
        if segment.eng_text:
            words = segment.eng_text.split()
            first_word = words[0]
            first_char = first_word[0]
            # Only check if the firt char is in the alphabet
            if first_char.isalpha():
                if not first_char.isupper():
                    segment.capitalization_error_found = True
                    segment.error_found = True

    return segments
