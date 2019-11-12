# -*- coding: utf-8 -*-


def consecutive_space_check(segments):
    '''
    Function for checking if consecutive spaces appear in the target text.
    '''
    double_space = '  '
    exception = '.  '  # Not treated as an error (spacing between sentences)

    for segment in segments:
        if (double_space in segment.eng_text) and \
           (exception not in segment.eng_text):
            segment.consecutive_space_found = True
            segment.error_found = True

    return segments


def leading_space_check(segments):
    '''
    Function for checking if whitespace appears at the start of
    the target text. Only treated as an error if there is no whitespace
    at the start of the source text.
    '''
    for segment in segments:
        if segment.eng_text.startswith(' '):
            if not segment.jap_text.startswith(' '):
                segment.leading_space_found = True
                segment.error_found = True

    return segments


def trailing_space_check(segments):
    '''
    Function for checking if whitespace appears at the end of
    the target text.Only treated as an error if there is no whitespace
    at the end of the source text.
    '''
    for segment in segments:
        if segment.eng_text.endswith(' '):
            if not segment.jap_text.endswith(' '):
                segment.trailing_space_found = True
                segment.error_found = True

    return segments
