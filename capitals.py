# -*- coding: utf-8 -*-


def leading_capital_check(segments):
    '''
    Function for checking if the first word in the target text
    has been capitalized.
    '''
    for segment in segments:
        if segment.eng_text:
            words = segment.eng_text.split()
            first_word = words[0]
            first_char = first_word[0]
            if first_char.isalpha():
                if first_char.islower():
                    segment.capitalization_error_found = True
                    segment.error_found = True

    return segments
