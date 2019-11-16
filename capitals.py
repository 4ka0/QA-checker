# -*- coding: utf-8 -*-


def leading_capital_check(segments):
    '''
    Function for checking if the first word in the target text
    has been capitalized.
    '''
    for segment in segments:

        # Only proceed if there is target text.
        if segment.target_text:

            # Only proceed if there is text to check (REQUIRED?)
            if (segment.target_text.isspace() is False) and \
               (segment.target_text != ''):

                words = segment.target_text.split()
                first_word = words[0]
                first_char = first_word[0]

                if first_char.isalpha():
                    if first_char.islower():
                        segment.capitalization_error_found = True
                        segment.error_found = True

    return segments
