# -*- coding: utf-8 -*-


def single_word_check(segments):
    '''
    Function for checking to see if there are any single
    repeating words in the English text. Common examples include
    'the the' and 'is is'.
    '''

    for segment in segments:

        # Only proceed if there is target text.
        if segment.target_text:
            if not segment.target_text.isspace():

                previous_substring = ''
                substrings = segment.target_text.split()

                for substring in substrings:
                    current_string = substring

                    if previous_substring.lower() == current_string.lower():
                        segment.error_found = True
                        segment.repeated_word_found = True
                        segment.repeated_words.append(previous_substring +
                                                      ' ' + current_string)

                    previous_substring = current_string

    return segments


def double_word_check(segments):
    '''
    Function for checking to see if there are any repeating two-word
    combinations in the English text. Common examples include
    'of the of the' and 'will be will be'.
    '''

    for segment in segments:

        # Only proceed if there is target text.
        if segment.target_text:
            if not segment.target_text.isspace():

                substrings = segment.target_text.split()

                '''
                Loop through substrings one by one.
                Build and compare two-word combinations based on
                current substring and next substring.
                '''
                i = 0
                while (i + 3) < len(substrings):
                    substring_A = substrings[i] + ' ' + substrings[i + 1]
                    substring_B = substrings[i + 2] + ' ' + substrings[i + 3]

                    # Compare substrings
                    if substring_A == substring_B:
                        segment.error_found = True
                        segment.repeated_word_found = True
                        segment.repeated_words.append(substring_A + ' '
                                                      + substring_B)

                    i += 1

    return segments
