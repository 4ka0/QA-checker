#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Program for performing various QA checks on a Jap>Eng tmx file.
Checks for the following issues:
    Inconsistent numbers (missing or extra numbers)
    Double spaces etc.
    Repeated words
    Unpaired symbols such as parentheses
    Untranslated segments
Takes three arguments to execute from the command line:
    python3 checker.py yourfile.tmx
Results sent to stdout.
'''


import verify
import gather
import untranslated
import numbers
import spaces
import repeaters
import unpaired
import capitals
import punctuation
import characters
import refnums
import output


if __name__ == "__main__":

    if verify.user_input_check():

        # Gather Japanese and English translation segments.
        segments = gather.gather_segments()

        # Run checks
        segments = untranslated.untranslated_check(segments)
        segments = numbers.missing_number_check(segments)
        segments = numbers.extra_number_check(segments)
        segments = spaces.consecutive_space_check(segments)
        segments = spaces.leading_space_check(segments)
        segments = spaces.trailing_space_check(segments)
        segments = repeaters.single_word_check(segments)
        segments = repeaters.double_word_check(segments)
        segments = unpaired.unpaired_symbol_check(segments)
        segments = capitals.leading_capital_check(segments)
        segments = punctuation.ending_punctuation_check(segments)
        segments = characters.jap_character_check(segments)
        # segments = refnums.refnum_check(segments)

        # Output final results
        # output.output_results(segments)
