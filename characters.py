# -*- coding: utf-8 -*-


def asian_character_check(segments):
    '''
    Identifies Asian characters included in the English text of a given
    segment. A character is defined as being Asian if the Unicode code
    point of the character is greater than that for the ideographic space
    (doublebyte/fullwidth space). This results in characters such as the
    following being caught:
        Kanji
        Hiragana
        Katakana (fullwidth and halfwidth forms)
        Fullwidth Latin characters
    '''
    ideographic_space = 0x3000
    for segment in segments:

        # Only proceed if there is target text
        if segment.target_text:

            for char in segment.target_text:

                if ord(char) > ideographic_space:

                    segment.error_found = True
                    segment.asian_char_found = True
                    segment.asian_chars.append(char)

    return(segments)
