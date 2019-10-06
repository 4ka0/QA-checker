#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking if more than one consecutive space appears in an English segment.
'''
def double_space_check(segments):

    double_space = "  "

    for segment in segments:
        if double_space in segment.eng_text:
            segment.doubleSpace = True

    return segments