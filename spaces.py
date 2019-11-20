# -*- coding: utf-8 -*-


def consecutive_space_check(segments):
    '''
    Function for checking if consecutive spaces appear in the target text.
    '''
    consecutive_space = '  '
    exception = '.  '  # Not treated as an error (spacing between sentences)

    for segment in segments:

        # Only proceed if there is target text.
        if segment.target_text:
            if not segment.target_text.isspace():

                if (consecutive_space in segment.target_text) and \
                   (exception not in segment.target_text):

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

        # Only proceed if there is target text.
        if segment.target_text:
            if not segment.target_text.isspace():

                if segment.target_text.startswith(' '):

                    if not segment.source_text.startswith(' '):

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

        # Only proceed if there is target text.
        if segment.target_text:
            if not segment.target_text.isspace():

                if segment.target_text.endswith(' '):

                    if not segment.source_text.endswith(' '):
                        segment.trailing_space_found = True
                        segment.error_found = True

    return segments
