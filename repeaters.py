#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking to see if there are any repeating words in
the English text. Common examples include "the the" and "is is".
'''

import re

def repeated_word_check(segments):

    repeated_words = []

    '''
    loop through japanese segment text
        compare last substring with current substring
            if the same
                error flag
                save repeated substrings in list
    '''

    for segment in segments:
        substrings = segment.eng_text.split()
        if substrings: # Proceeds only if list is populated.
            previous_substring = ""
            for substring in substrings:
                # remove punctuation chars from substring
                cleaned_string = re.sub('[,.<>()/?=!@#$]', '', substring) # check this line
                print(substring)
                print(cleaned_string + "\n")
                if previous_substring.lower() == cleaned_string.lower():
                    print("... MATCH FOUND")
                    print(previous_substring.lower())
                    print(cleaned_string.lower() + "\n")
                    segment.repeated_word = True
                    segment.error_found = True
                previous_substring = cleaned_string

    return segments