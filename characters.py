#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def jap_character_check(segments):
    '''
    Function for checking if any Japanese or full-width characters
    are included in the English text.
    '''

    for segment in segments:

        eng_text = segment.eng_text.strip()

        # BUG - not detecting hiragana or katakana
        # Place character ranges in a list and just have one for loop

        for n in re.findall(r'[\u4E00-\u9FEF]+', eng_text):  # kanji
            print(n)

        for n in re.findall(r'[\u3040–\u309F]+', eng_text):  # hiragana
            print(n)

        for n in re.findall(r'[\u30A0–\u30FF]+', eng_text):  # katakana
            print(n)

    return segments


'''
Japanese Unicode character ranges

CJK_unified_ideographs = r'[\u4E00-\u9FEF]'
CJK_unified_ideographs_extension_A = r'[\u3400–\u4DB5]'
CJK_unified_ideographs_extension_B = r'[\u20000–\u2A6D6]'
CJK_unified_ideographs_extension_C = r'[\u2A700–\u2B734]'
CJK_unified_ideographs_extension_D = r'[\u2B740–\u2B81D]'
CJK_unified_ideographs_extension_E = r'[\u2B820–\u2CEA1]'
CJK_unified_ideographs_extension_F = r'[\u2CEB0–\u2EBE0]'
CJK_compatibility_ideographs = r'[\uF900–\uFAFF]'
CJK_compatibility_ideographs_supplement = r'[\u2F800–\u2FA1F]'
CJK_radicals = r'[\u2F00–\u2FDF]'
CJK_radicals_supplement = r'[\u2E80–\u2EFF]'
CJK_strokes = r'[\u31C0–\u31EF]'
hiragana = r'[\u3040–\u309F]'
kana_extended_A = r'[\u1B100–\u1B12F]'
kana_supplement = r'[\u1B000–\u1B0FF]'
small_kana_extension = r'[\u1B130–\u1B16F]'
kanbun = r'[\u3190–\u319F]'
fullwidth_katakana = r'[\u30A0–\u30FF]'
halfwidth_katakana = r'[\uFF65–\uFF9F]'
katakana_phonetic_extensions = r'[\u31F0–\u31FF]'
halfwidth_CJK_punctuation = r'[\uFF61–\uFF64]'
halfwidth_symbols = r'[\uFFE8–\uFFEE]'
CJK_symbols_and_punctuation = r'[\u3000–\u303F]'
ideographic_symbols_and_punctuation = r'[\u16FE0–\u16FFF]'
enclosed_CJK_letters_and_months = r'[\u3200–\u32FF]'
enclosed_CJK_letters_and_months = r'[\u3200–\u32FF]'
enclosed_ideographic_supplement = r'[\u1F200–\u1F2FF]'
squared_katakana_words = r'[\u3300–\u3357]'
telegraph_symbols_for_hours = r'[\u3358–\u3370]'
telegraph_symbols_for_days = r'[\u33E0–\u33FE]'
japanese_era_names = r'[\u337B–\u337E]'

Full-width ASCII Unicode character ranges

fullwidth_ASCII_symbols_1 = r'[\uFF01–\uFF9F]'
fullwidth_ASCII_symbols_2 = r'[\uFF1A–\uFF20]'
fullwidth_ASCII_symbols_3 = r'[\uFF3B–\uFF4A]'
fullwidth_ASCII_symbols_4 = r'[uFF5B–\uFF60]'
fullwidth_ASCII_numbers = r'[\uFF10–\uFF19]'
fullwidth_symbols = r'[\uFFE0–\uFFE6]'
fullwidth_ASCII_uppercase_letters = r'[\uFF21–\uFF3A]'
fullwidth_ASCII_lowercase_letters = r'[\uFF41–\uFF5A]'
'''
