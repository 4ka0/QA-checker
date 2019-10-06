#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

'''
Function for checking if numbers in Japanese segments are 
present in corresponding English segments as actual digits.
'''
def missing_number_check(segments):

    '''
    Uses regex to extract all digits from each Japanese and English segment.
    "\d" is a digit and "+" means 1 or more times, so "\d+"" means 1 or more digits.
    '''
    for segment in segments:
        segment.jap_nums = re.findall(r'\d+', segment.jap_text)
        segment.eng_nums = re.findall(r'\d+', segment.eng_text)

    # Identifies any digits that are missing from the Japanese segments.
    for segment in segments:
        
        '''
        missing_nums is a full copy of jap_nums to begin with.
        Digits are then removed from missing_nums when found.
        '''
        segment.missing_nums = segment.jap_nums.copy()
        
        '''
        eng_nums_copy is a a full copy of eng_nums to begin with.
        Digits are then removed from eng_nums_copy when found.
        Using a copy here avoids altering the original list of found digits,
        and helps to counter the situation where there is more than one instance of a digits.
        '''
        eng_nums_copy = segment.eng_nums.copy()

        '''
        Once this loop has finished, missing_nums contains 
        only digits that have not been found in the Japanese segment.
        '''
        for numeral in segment.jap_nums:
            if numeral in eng_nums_copy:
                eng_nums_copy.remove(numeral) # remove() deletes the first matching digit from the list.
                segment.missing_nums.remove(numeral)

        if len(segment.missing_nums) > 0:
            segment.errors_found = True

    return segments

'''
Function for checking if extra numbers are included the English segment.
'''
def extra_number_check(segments):
    return segments