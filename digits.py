#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

'''
Function for checking if numbers in Japanese segments are 
present in corresponding English segments as actual digits.
'''
def digitCheck(segments):

    '''
    Uses regex to extract all digits from each Japanese and English segment.
    "\d" is a digit and "+" means 1 or more times, so "\d+"" means 1 or more digits.
    '''
    for segment in segments:
        segment.japNums = re.findall(r'\d+', segment.jap)
        segment.engNums = re.findall(r'\d+', segment.eng)

    # Identifies any digits that are missing from the Japanese segments.
    for segment in segments:
        
        '''
        missingNums is a full copy of japNums to begin with.
        Digits are then removed from missingNums when found.
        '''
        segment.missingNums = segment.japNums.copy()
        
        '''
        engNumsCopy is a a full copy of engNums to begin with.
        Digits are then removed from engNumsCopy when found.
        Using a copy here avoids altering the original list of found digits,
        and helps to counter the situation where there is more than one instance of a digits.
        '''
        engNumsCopy = segment.engNums.copy()

        '''
        Once this loop has finished, missingNums contains 
        only digits that have not been found in the Japanese segment.
        '''
        for numeral in segment.japNums:
            if numeral in engNumsCopy:
                engNumsCopy.remove(numeral) # remove() deletes the first matching digit from the list.
                segment.missingNums.remove(numeral)

    return segments