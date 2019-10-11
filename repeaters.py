#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

'''
Function for checking to see if there are any single repeating words in the English text.
Common examples include "the the" and "is is".
'''
def single_word_check(segments):

    for segment in segments:

        # Only proceed if there is English text in the segment.
        if segment.eng_text:
            previous_substring = ""
            substrings = segment.eng_text.split()

            for substring in substrings:
                # clean punctuation chars etc. from substring
                current_string = re.sub('[,.;:/?*"+=!_@#$<>()\[\]]', '', substring)

                if previous_substring.lower() == current_string.lower():
                    segment.error_found = True
                    segment.repeated_word = True
                    segment.repeated_words.append(previous_substring + " " + current_string)

                previous_substring = current_string

    return segments


'''
Function for checking to see if there are any double repeating words in the English text.
Common examples include "there is there is" and "will be will be".
'''
def double_word_check(segments):

    for segment in segments:

        # CONTINUE FROM HERE !!!!!!!

        # Only proceed if there is English text in the segment.
        if segment.eng_text:
            previous_substring = ""
            substrings = segment.eng_text.split()

            for substring in substrings:
                # clean punctuation chars etc. from substring
                current_string = re.sub('[,.;:/?*"+=!_@#$<>()\[\]]', '', substring)

                if previous_substring.lower() == current_string.lower():
                    segment.error_found = True
                    segment.repeated_word = True
                    segment.repeated_words.append(previous_substring + " " + current_string)

                previous_substring = current_string

    return segments