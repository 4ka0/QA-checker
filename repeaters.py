#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking to see if there are any repeating words in
the English text. Common examples include "the the" and "is is".
'''

import re

def repeated_word_check(segments):

    '''
    loop through japanese segment text
        compare last substring with current substring
            if the same
                error flag
                save repeated substrings in list
    '''

    for segment in segments:
        # Only proceed if there is English text in the segment.
        if segment.eng_text:
            substrings = segment.eng_text.split()
            # print("\n" + str(substrings))
            previous_substring = ""
            for substring in substrings:
                # remove punctuation chars etc. from currrent substring
                current_string = re.sub('[,.;:/?*"+=!_@#$<>()\[\]]', '', substring)
                if previous_substring.lower() == current_string.lower():
                    # print("... MATCH FOUND")
                    # print(previous_substring.lower())
                    # print(current_string.lower())
                    segment.repeated_words.append(previous_substring + " " + current_string)
                    # print(segment.repeated_words)
                    segment.repeated_word = True
                    segment.error_found = True
                previous_substring = current_string

    '''
    add loop for catching two-word repetitions such as "may be may be"
    '''


    

    return segments