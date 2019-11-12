# -*- coding: utf-8 -*-


def untranslated_check(segments):
    '''
    Function for checking for untranslated segments.
    Segments treated as untranslated if:
        - there is no English text
        - the English text contains only whitespace
    '''
    for segment in segments:
        if not segment.eng_text:
            segment.untranslated_seg = True
        if segment.eng_text.isspace():
            segment.untranslated_seg = True
    return segments
