#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

'''
Function for extracting all numbers from each Japanese and English segment using regex.
'''
def extract_numbers(segments):
    for segment in segments:
        segment.jap_nums = re.findall(r'\d+', segment.jap_text) # \d+ means one or more numbers
        segment.eng_nums = re.findall(r'\d+', segment.eng_text)
    return segments

'''
Function for Loop for finding any numbers that are missing from the English segments.
'''
def missing_number_check(segments):

    segments = extract_numbers(segments)

    for segment in segments:

        '''
        missing_nums is a full copy of jap_nums to begin with.
        Numbers are then removed from missing_nums when found.
        '''
        segment.missing_nums = segment.jap_nums.copy()
        
        '''
        eng_nums_copy is a a full copy of eng_nums to begin with.
        Numbers are then removed from eng_nums_copy when found.
        Using a copy here avoids altering the original list of found numbers,
        and helps to counter the situation where there is more than one instance of a given number.
        '''
        eng_nums_copy = segment.eng_nums.copy()

        '''
        After this loop, missing_nums contains only
        numbers that have not been found in the Japanese segment.
        '''
        for numeral in segment.jap_nums:
            if numeral in eng_nums_copy:
                eng_nums_copy.remove(numeral) # remove() deletes only the first match from the list.
                segment.missing_nums.remove(numeral)

        if len(segment.missing_nums) > 0:
            segment.error_found = True

    return segments

'''
Function for checking if extra numbers are included the English segment.
Essentially the same logic as above.
'''
def extra_number_check(segments):

    segments = extract_numbers(segments)

    for segment in segments:

        segment.extra_nums = segment.eng_nums.copy()
        jap_nums_copy = segment.jap_nums.copy()

        for numeral in segment.eng_nums:
            if numeral in jap_nums_copy:
                jap_nums_copy.remove(numeral)
                segment.extra_nums.remove(numeral)

        if len(segment.extra_nums) > 0:
            segment.error_found = True

    return segments