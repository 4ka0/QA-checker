#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter


def number_check(segments):
    '''
    Function for finding any number inconsistencies between the Japanese
    English text.
    '''

    for segment in segments:

        # Extract numbers
        segment.jap_nums = re.findall(r'\d+', segment.jap_text)
        segment.eng_nums = re.findall(r'\d+', segment.eng_text)

        # Identifies number of instances of each number
        jap_nums = Counter(segment.jap_nums)
        eng_nums = Counter(segment.eng_nums)

        # Compares number instances between Jap and Eng
        segment.missing_nums = jap_nums - eng_nums
        segment.extra_nums = eng_nums - jap_nums

        # Raise error flag if necessary
        if segment.missing_nums:
            segment.error_found = True
        if segment.extra_nums:
            segment.error_found = True

    return segments
