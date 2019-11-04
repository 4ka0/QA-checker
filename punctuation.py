#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def ending_punctuation_check(segments):
    '''
    Function for checking if the source and target text
    end with the same punctuation.
    '''
    for segment in segments:

        jap_text = segment.jap_text.strip()
        eng_text = segment.eng_text.strip()
        last_jap_char = jap_text[-1]

        jap_punc_marks = ['\u3001', '\u002C', '\uFF0C', '\uFF64', '\u3002',
                          '\u002E', '\uFF0E', '\uFF61', '\uFF09', '\uFF60',
                          '\uFF3D', '\uFF5D', '\u3015', '\u3017', '\u3011',
                          '\u3019', '\u301B', '\u3009', '\u300B', '\u300D',
                          '\u300F', '\u301C', '\uFF5E', '\u2026']

        # if jap ends with punctuation mark
        if last_jap_char in jap_punc_marks:

            # get trailing punctuation in eng
            last_eng_char = eng_text[-1]

            '''
            compare trailing punctuation
            does last char in eng correspond to jap punctuation mark
            need a list of Jap-Eng corresponding punctuation marks
            corresponding punctuation marks as list of lists?
            '''




        trailing_punctuation_error = True

    return segments


'''
# Japanese closing puntuation marks (for reference)
# Commas (corresponding to ',' '\u002C')
'\u3001'  # ideographic comma '、'
'\u002C'  # basic latin comma ','
'\uFF0C'  # fullwidth comma '，'
'\uFF64'  # halfwidth ideographic comma '､'
# Periods (corresponding to '.' '\u002E')
'\u3002'  # ideographic period '。' => '.'
'\u002E'  # basic latin period '.'
'\uFF0E'  # fullwidth period '．'
'\uFF61'  # halfwidth ideographic period '｡'
# Parentheses (corresponding to ')' '\u0029')
'\uFF09'  # right single parenthesis '）'
'\uFF60'  # right double parenthesis '｠'
# Square brackets (corresponding to ']' '\u005D')
'\uFF3D'  # right bracket '］'
'\uFF5D'  # right curly bracket '｝'
'\u3015'  # right tortoise shell bracket '〕'
'\u3017'  # right white lenticular bracket '〗'
'\u3011'  # right solid lenticular bracket '】'
'\u3019'  # right white tortoise shell bracket '〙'
'\u301B'  # right white square bracket '〛'
# Angle brackets (corresponding to ']' '\u003E')
'\u3009'  # right angle bracket '〉'
'\u300B'  # right double angle bracket '》'
# Corner Brackets (corresponding to '"' '\u0022')
'\u300D'  # right corner bracket '」'
'\u300F'  # right white corner bracket '』'
# Tildes (corresponding to '...' and '…' '\u2026')
'\u301C'  # kara symbol '〜'
'\uFF5E'  # fullwidth tilde '～'
'\u2026'  # ellipsis '…'
'''
