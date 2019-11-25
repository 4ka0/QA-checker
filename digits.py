# -*- coding: utf-8 -*-

import re
from collections import Counter


def digit_check(segments):
    '''
    Function for finding any digit inconsistencies
    between the source Japanese and target English text.
    '''

    for segment in segments:

        # Only proceed if there is source and target text.
        if segment.source_text and segment.target_text:
            if not segment.source_text.isspace() and \
               not segment.target_text.isspace():

                # Extract digit
                segment.source_nums = re.findall(r'\d+', segment.source_text)
                segment.target_nums = re.findall(r'\d+', segment.target_text)

                # Identifies number of instances of each digit
                source_nums = Counter(segment.source_nums)
                target_nums = Counter(segment.target_nums)

                # Compares digit instances between Jap and Eng
                segment.missing_nums = source_nums - target_nums
                segment.extra_nums = target_nums - source_nums

                # Raise error flag if necessary
                if segment.missing_nums or segment.extra_nums:
                    segment.error_found = True

    return segments
