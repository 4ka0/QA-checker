#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking if more than one consecutive space appears in an English segment.
'''
def doubleSpaceCheck(segments):

    double_space = "  "

    for segment in segments:
        if double_space in segment.eng:
            segment.doubleSpace = True

    return segments