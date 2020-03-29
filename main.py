#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script for performing basic QA checks on a tmx file of a Japanese to English translation.
Checks for the following issues:
    Untranslated segments
    Inconsistent numbers
    Consecutive spaces
    Leading spaces
    Trailing spaces
    Repeated words
    Repeated two-word combinations
    Unpaired symbols
    Leading capitalization
    Inconsistent ending punctuation
    Fullwidth characters in target
Takes three arguments to execute from the command line:
    python3 checker.py yourfile.tmx
Results sent to stdout.
'''

import sys

import verify
import gather
import untranslated
import digits
import spaces
import repeaters
import unpaired
import capitals
import punctuation
import characters
import output


def main():
    if verify.user_input_check(sys.argv):
        segments = gather.gather_segments(sys.argv[1])
        segments = untranslated.untranslated_check(segments)
        segments = digits.digit_check(segments)
        segments = spaces.consecutive_space_check(segments)
        segments = spaces.leading_space_check(segments)
        segments = spaces.trailing_space_check(segments)
        segments = repeaters.single_word_check(segments)
        segments = repeaters.double_word_check(segments)
        segments = unpaired.unpaired_symbol_check(segments)
        segments = capitals.leading_capital_check(segments)
        segments = punctuation.ending_punctuation_check(segments)
        segments = characters.asian_character_check(segments)
        output.output_results(segments)


if __name__ == '__main__':
    main()
