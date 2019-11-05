#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ending_punctuation_check(segments):
    '''
    Function for checking if the source and target text
    end with the same punctuation.
    '''

    # List of Japanese punctuation marks
    jap_punc = ['\u3001', '\u002C', '\uFF0C', '\uFF64', '\u3002',
                '\u002E', '\uFF0E', '\uFF61', '\uFF09', '\uFF60',
                '\uFF3D', '\uFF5D', '\u3015', '\u3017', '\u3011',
                '\u3019', '\u301B', '\u3009', '\u300B', '\u300D',
                '\u300F', '\u301C', '\uFF5E', '\u2026', '\u0029',
                '\u005D', '\u003E', '\u0022']

    # Dict of Japanese punctuation marks and
    # the corresponding English punctuation marks
    corresponding_punc = {'\u3001': '\u002C', '\u002C': '\u002C',
                          '\uFF0C': '\u002C', '\uFF64': '\u002C',
                          '\u3002': '\u002E', '\u002E': '\u002E',
                          '\uFF0E': '\u002E', '\uFF61': '\u002E',
                          '\uFF09': '\u0029', '\uFF60': '\u0029',
                          '\u0029': '\u0029', '\uFF3D': '\u005D',
                          '\uFF5D': '\u005D', '\u3015': '\u005D',
                          '\u3017': '\u005D', '\u3011': '\u005D',
                          '\u3019': '\u005D', '\u301B': '\u005D',
                          '\u005D': '\u005D', '\u3009': '\u003E',
                          '\u003E': '\u003E', '\u300B': '\u003E',
                          '\u300D': '\u0022', '\u0022': '\u0022',
                          '\u300F': '\u0022', '\u301C': '\u2026',
                          '\uFF5E': '\u2026', '\u2026': '\u2026'}

    for segment in segments:

        jap_text = segment.jap_text.strip()
        eng_text = segment.eng_text.strip()
        last_jap_char = jap_text[-1]

        if last_jap_char in jap_punc:
            last_eng_char = eng_text[-1]
            # Compare trailing punctuation between Jap and Eng,
            # these should correspond.
            corresponding_eng = corresponding_punc[last_jap_char]
            if last_eng_char != corresponding_eng:
                segment.trailing_punctuation_error = True

    return segments


'''
REFERENCE - Japanese closing puntuation marks

Commas (corresponding to English version ',' '\u002C')
'\u3001'  # ideographic comma '、'
'\u002C'  # basic latin comma ','
'\uFF0C'  # fullwidth comma '，'
'\uFF64'  # halfwidth ideographic comma '､'

Periods (corresponding to English version '.' '\u002E')
'\u3002'  # ideographic period '。' => '.'
'\u002E'  # basic latin period '.'
'\uFF0E'  # fullwidth period '．'
'\uFF61'  # halfwidth ideographic period '｡'

Parentheses (corresponding to English version ')' '\u0029')
'\uFF09'  # right single parenthesis '）'
'\uFF60'  # right double parenthesis '｠'

Square brackets (corresponding to English version ']' '\u005D')
'\uFF3D'  # right bracket '］'
'\uFF5D'  # right curly bracket '｝'
'\u3015'  # right tortoise shell bracket '〕'
'\u3017'  # right white lenticular bracket '〗'
'\u3011'  # right solid lenticular bracket '】'
'\u3019'  # right white tortoise shell bracket '〙'
'\u301B'  # right white square bracket '〛'

Angle brackets (corresponding to English version '>' '\u003E')
'\u3009'  # right angle bracket '〉'
'\u300B'  # right double angle bracket '》'

Corner Brackets (corresponding to English version '"' '\u0022')
'\u300D'  # right corner bracket '」'
'\u300F'  # right white corner bracket '』'

Tildes (corresponding to English version '…' '\u2026')
'\u301C'  # kara symbol '〜'
'\uFF5E'  # fullwidth tilde '～'
'\u2026'  # ellipsis '…'
'''
