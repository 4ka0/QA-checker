# -*- coding: utf-8 -*-


def leading_capital_check(segments):
    '''
    Function for checking if the first word in the target text
    has been capitalized.
    '''
    for segment in segments:

        # Only proceed if there is target text.
        if segment.target_text:

            text = segment.target_text.lstrip()
            first_char = text[0]

            if first_char.isalpha() and first_char.islower():
                segment.capitalization_error_found = True
                segment.error_found = True

    return segments
