#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking if more than one consecutive space appears in an English segment.
'''
def double_space_check(segments):

    double_space_chars = "  "

    for segment in segments:
        if double_space_chars in segment.eng_text:

            '''
            should only be an error if not preceded by a full-stop
            '''

            segment.double_space = True
            segment.error_found = True

    return segments