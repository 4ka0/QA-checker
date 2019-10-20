#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def alphanum_check(segments):
    '''
    Function for checking for missing alphanumerical combinations.
    (Combinations such as "100a" and "240B" often appear in Japanese
    patent texts.)
    '''

    # Identify substrings containing both letters and numbers.
    for segment in segments:

        # Look at Japanese text
        '''
        BUG - no spaces in Japanese so extracts too much
        split() uses whitespace as a delimiter
         need different extraction method for Japanese
        '''
        '''
        words = segment.jap_text.split()
        for word in words:
            if alphanum_identify(word) == True:
                segment.jap_alphanums.append(word)
        '''
        print("\n")
        jap_text = clean_string(segment.jap_text)
        jap_text = strip_Japanese(jap_text)
        jap_words = jap_text.split()
        for word in jap_words:
            if alphanum_identify(word) == True:
                segment.jap_alphanums.append(word)
        print(segment.jap_alphanums)

        # Look at English text
        eng_text = clean_string(segment.eng_text)
        eng_words = eng_text.split()
        for word in eng_words:
            if alphanum_identify(word) == True:
                segment.eng_alphanums.append(word)
        print(segment.eng_alphanums)

        # Compare




    return segments


def alphanum_identify(substring):
    '''
    Function for identifying strings that contain
    at least one letter and at least one number
    '''
    letter_present = False
    number_present = False
    for letter in substring:
        if letter.isalpha():
            letter_present = True
        if letter.isdigit():
            number_present = True
    if letter_present and number_present:
        return True
    else:
        return False


def strip_Japanese(jap_text):
    '''
    Function for removing Japanese characters from a string.
    Based on jp_regex.py, see:
    https://github.com/olsgaard/Japanese_nlp_scripts/blob/master/jp_regex.py
    Copyright (c) 2014-2015, Mads Sørensen Ølsgaard
    All rights reserved. Released under BSD3 License.
    Regular expression unicode blocks, collected from:
    http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/
    '''

    # Regular expression unicode blocks
    hiragana_full_width = r'[ぁ-ゟ]'
    katakana_full_width = r'[゠-ヿ]'
    katakana_half_width = r'[｟-ﾟ]'
    kanji = r'[㐀-䶵一-鿋豈-頻]'
    radicals = r'[⺀-⿕]'
    alphanum_full_width = r'[！-～]'
    symbols_punct = r'[、-〿]'
    misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'

    # Strip Japanese segment of characters included in above blocks
    jap_text = re.sub(kanji, " ", jap_text)
    jap_text = re.sub(hiragana_full_width, " ", jap_text)
    jap_text = re.sub(katakana_full_width, " ", jap_text)
    jap_text = re.sub(katakana_half_width, " ", jap_text)
    jap_text = re.sub(radicals, " ", jap_text)
    jap_text = re.sub(symbols_punct, " ", jap_text)
    jap_text = re.sub(misc_symbols, " ", jap_text)
    jap_text = re.sub(alphanum_full_width, " ", jap_text)

    return jap_text


'''
Function for removing punctuation chars etc. from a string (normalizing).
'''
def clean_string(text):
    clean_text = re.sub('[,.;:/?*"+=!_@#$<>()\[\]]', ' ', text)
    return clean_text
