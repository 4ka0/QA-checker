#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def untranslated_check(segments):
    '''
    Function for checking for untranslated segments.
    Segments treated as untranslated if:
        - the English text is empty
        - the English text contains only whitespace
    '''

    return segments


def partially_translated_check(segments):
    '''
    Function for checking for partially translated segments.
    Segments treated as partially translated if:
        - the English text is shorter than the Japanese text
          i.e. the Eng wordcount is less than half of the Jap character count
    '''

    return segments
