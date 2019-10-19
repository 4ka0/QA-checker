#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def alphanum_check(segments):
    '''
    Function for checking for missing alphanumerical combinations.
    (Combinations such as "100a" and "240B" often appear in Japanese
    patent texts.)
    '''

    # Identify substrings containing both letters and numbers.
    for segment in segments:
        # Look at Japanese text
        words = segment.jap_text.split()
        for word in words:
            if alphanum_identify(word) == True:
                segment.jap_alphanums.append(word)
        # Look at English text
        words = segment.eng_text.split()
        for word in words:
            if alphanum_identify(word) == True:
                segment.eng_alphanums.append(word)

        # Compare




    return segments


def alphanum_identify(substring):
    '''
    Function for identifying strings that contain
    at least one letter and at least one number
    '''
    letter_present = False
    number_present = False
    for letter in substring:
        if letter.isalpha():
            letter_present = True
        if letter.isdigit():
            number_present = True
        if (letter_present == True and number_present == True):
            return True
        else:
            return False
