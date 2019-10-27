#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter


def refnum_check(segments):
    '''
    Function for checking for missing reference numbers which often
    appear in Japanese patent texts, such as '100a' and '240B'.
    '''

    # Extract reference numbers from Japanese and English text
    segments = collect_Jap_refnums(segments)
    segments = collect_Eng_refnums(segments)

    # Look for missing and extra reference numbers
    for segment in segments:

        # Identifies number of instances of each reference number
        jap_refnums = Counter(segment.jap_refnums)
        eng_refnums = Counter(segment.eng_refnums)

        # Compares reference number instances between Jap and Eng
        segment.missing_refnums = jap_refnums - eng_refnums
        segment.extra_refnums = eng_refnums - jap_refnums

        # Raise error flag if necessary
        if segment.missing_refnums:
            segment.error_found = True
        if segment.extra_refnums:
            segment.error_found = True

    return segments


def collect_Jap_refnums(segments):
    '''
    Function for extracting reference numbers from Japanese text.
    '''

    # Mathematical characters to be ignored
    math_symbols = ['+', '-', '/', 'x', '*', '=', '<', '>', '≦', '≧',
                    '≤', '≥', '.']

    # Units to be ignored
    units = ['km', 'm', 'cm', 'mm', 'nm', 'mg', 'ml', 'kw', 'kwh',
             'kg', 'kl', 'km', 'µg', 'µm', 'mm2', 'm2', 'cm2'
             'mm3', 'm3', 'cm3', 'kb', 'gb', 'mb', 'pm', 'ns'
             'ms', 'mw', 'mwh', 'gw', 'gwh']

    for segment in segments:
        jap_text = clean_string(segment.jap_text)
        jap_text = strip_Japanese(jap_text)
        jap_words = jap_text.split()
        for word in jap_words:
            if refnum_identify(word):
                # Ignore reference numbers that include math symbols
                if not any(char in word for char in math_symbols):
                    # Ignore digits combined with measurement units
                    includes_unit = False
                    for unit in units:
                        if word.endswith(unit):
                            includes_unit = True
                    if not includes_unit:
                        segment.jap_refnums.append(word)

    return segments


def collect_Eng_refnums(segments):
    '''
    Function for extracting reference numbers from English text.
    '''

    # Ordinals to be ignored
    ordinals = ['1st', '2nd', '3rd', '4th', '5th',
                '6th', '7th', '8th', '9th', '10th',
                '11th', '12th', '13th', '14th', '15th',
                '16th', '17th', '18th', '19th', '20th']

    for segment in segments:
        eng_text = clean_string(segment.eng_text)
        eng_words = eng_text.split()
        for word in eng_words:
            if refnum_identify(word):
                if word not in ordinals:
                    segment.eng_refnums.append(word)

    return segments


def refnum_identify(substring):
    '''
    Function for identifying substrings that contain at least one letter
    and at least one number. These are treated as reference numbers.
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
    Japanese typically contains no whitespace as word delimiters,
    so, in order to extract reference number substrings, all of the
    Japanese characters have to be removed first.

    Based on jp_regex.py.
    https://github.com/olsgaard/Japanese_nlp_scripts/
        blob/master/jp_regex.py
    Copyright (c) 2014-2015, Mads Sørensen Ølsgaard
    All rights reserved. Released under BSD3 License.

    Regular expression unicode blocks collected from:
    http://www.localizingjapan.com/blog/2012/01/20/
        regular-expressions-for-japanese-text/
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
    jap_text = re.sub(kanji, ' ', jap_text)
    jap_text = re.sub(hiragana_full_width, ' ', jap_text)
    jap_text = re.sub(katakana_full_width, ' ', jap_text)
    jap_text = re.sub(katakana_half_width, ' ', jap_text)
    jap_text = re.sub(radicals, ' ', jap_text)
    jap_text = re.sub(symbols_punct, ' ', jap_text)
    jap_text = re.sub(misc_symbols, ' ', jap_text)
    jap_text = re.sub(alphanum_full_width, ' ', jap_text)

    return jap_text


def clean_string(text):
    '''
    Function for removing punctuation chars etc. from a string.
    '''
    clean_text = re.sub('[,.;:/?*"+=!_@#$<>()\[\]]', ' ', text)
    return clean_text
