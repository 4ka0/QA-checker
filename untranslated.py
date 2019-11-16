# -*- coding: utf-8 -*-


def untranslated_check(segments):
    '''
    Function for checking for untranslated segments.
    Segments treated as untranslated if:
        - there is no English text
        - the English text contains only whitespace
    '''
    for segment in segments:
        if not segment.target_text:
            segment.untranslated_seg = True
            segment.error_found = True
        elif segment.target_text.isspace():
            segment.untranslated_seg = True
            segment.error_found = True
    return segments
