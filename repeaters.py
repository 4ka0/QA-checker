#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking to see if there are any repeating words in
the English text. Common examples include "the the" and "is is".
'''

import re

def repeated_word_check(segments):

    '''
    Loop for catching single word repetitions such as "the the".
    '''
    for segment in segments:

        print("\nCurrent list of repeated words=")
        print(segment.repeated_words)
        
        # Only proceed if there is English text in the segment.
        if segment.eng_text:
            previous_substring = ""
            substrings = segment.eng_text.split()

            for substring in substrings:
                # clean punctuation chars etc. from substring
                current_string = re.sub('[,.;:/?*"+=!_@#$<>()\[\]]', '', substring)
        
                if previous_substring.lower() == current_string.lower():
 
                    print("... MATCH FOUND")
                    print(previous_substring.lower())
                    print(current_string.lower())
                    '''
                    !!! Bug found !!!
                    REPEATED WORD FOUND.
					['is is', 'circuit circuit']
					segment.repeated_words is somehow GLOBAL !?
					'''
                    segment.error_found = True
                    segment.repeated_word = True
                    segment.repeated_words.append(previous_substring + " " + current_string)
                    print("New list of repeated words =")
                    print(segment.repeated_words)

                previous_substring = current_string

    '''
    Loop for catching double word repetitions such as "is the is the".
    '''



    

    return segments