#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def double_space_check(segments):
    '''
    Function for checking if more than one consecutive space
    appears in an English segment.
    '''

    double_space = "  "
    exception = ".  " # Not treated as an error

    for segment in segments:
        if (double_space in segment.eng_text and \
            exception not in segment.eng_text):
            segment.double_space_found = True
            segment.error_found = True

    return segments
