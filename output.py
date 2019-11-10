#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore


def output_results(segments):
    '''
    Function for outputting QA check results.
    '''

    print(Fore.CYAN + '\nRESULTS:\n')

    errors_found_overall = False

    for segment in segments:

        if segment.error_found:

            # Results for untranslated segments
            if segment.untranslated_seg:
                print(Fore.RED + 'Untranslated segment found.')
                errors_found_overall = True

            # Results for consecutive spaces
            if segment.consecutive_space_found:
                print(Fore.RED + 'Consecutive spaces found.')
                errors_found_overall = True

            # Results for leading spaces
            if segment.leading_space_found:
                print(Fore.RED + 'Leading space found.')
                errors_found_overall = True

            # Results for trailing spaces
            if segment.trailing_space_found:
                print(Fore.RED + 'Trailing space found.')
                errors_found_overall = True

            # Results for leading capitalization
            if segment.capitalization_error_found:
                print(Fore.RED + 'Leading word not capitalized.')
                errors_found_overall = True

            # Results for repeated words
            if segment.repeated_word_found:
                repeated_word_string = list_string(segment.repeated_words)
                print(Fore.RED + 'Repeated words found: ' +
                      repeated_word_string)
                errors_found_overall = True

            # Results for trailing punctuation
            if segment.trailing_punctuation_error:
                print(Fore.RED + 'Trailing punctuation does not match.')
                errors_found_overall = True

            # Results for unpaired symbols
            if segment.unpaired_symbol_found:
                unpaired_symbol_string = list_string(segment.unpaired_symbols)
                if len(segment.unpaired_symbols) > 1:
                    print(Fore.RED + 'Unpaired symbols found: ' +
                          unpaired_symbol_string)
                else:
                    print(Fore.RED + 'Unpaired symbol found: ' +
                          unpaired_symbol_string)
                errors_found_overall = True

            # Results for missing numberss
            if len(segment.missing_nums) > 0:
                num_string = dict_string(segment.missing_nums)
                if ',' in num_string:
                    print(Fore.RED + 'Missing numbers found: ' + num_string)
                else:
                    print(Fore.RED + 'Missing number found: ' + num_string)
                errors_found_overall = True

            # Results for extra numberss
            if len(segment.extra_nums) > 0:
                num_string = dict_string(segment.extra_nums)
                if ',' in num_string:
                    print(Fore.RED + 'Extra numbers found: ' + num_string)
                else:
                    print(Fore.RED + 'Extra number found: ' + num_string)
                errors_found_overall = True

            '''
            Results for missing aplhanums
            if len(segment.missing_aplhanums) > 0:
                aplhanum_string = dict_string(segment.missing_aplhanums)
                if ',' in aplhanum_string:
                    print(
                        Fore.RED + 'Missing reference numbers found: ' +
                        aplhanum_string)
                else:
                    print(Fore.RED + 'Missing reference number found: ' +
                          aplhanum_string)
                errors_found_overall = True

            Results for extra aplhanums
            if len(segment.extra_aplhanums) > 0:
                aplhanum_string = dict_string(segment.extra_aplhanums)
                if ',' in aplhanum_string:
                    print(Fore.RED + 'Extra reference numbers found: ' +
                          aplhanum_string)
                else:
                    print(Fore.RED + 'Extra reference number found: ' +
                          aplhanum_string)
                errors_found_overall = True
            '''

            # Results for Asian characters and symbols
            if segment.asian_char_found:
                asian_char_string = list_string(segment.asian_chars)
                if len(segment.asian_chars) > 1:
                    print(Fore.RED + 'Asian characters found: ' +
                          asian_char_string)
                else:
                    print(Fore.RED + 'Asian character found: ' +
                          asian_char_string)
                errors_found_overall = True

            print(Fore.CYAN + 'Japanese:')
            print(Fore.RESET + segment.jap_text)
            print(Fore.CYAN + 'English:')
            print(Fore.RESET + segment.eng_text)
            print('\n')

    if not errors_found_overall:
        print(Fore.GREEN + '\nNo errors found.\n')


def list_string(error_list):
    '''
    Function for building a single string from a list.
    E.g. builds a single string from all ints in the
    missing_nums list of a given segment.
    '''
    error_string = ''
    for item in error_list:
        error_string = error_string + str(item) + ', '
    error_string = error_string.strip(', ')
    return error_string


def dict_string(error_list):
    '''
    Function for building a single string from a dict.
    E.g. builds a single string from all keys and values in the
    missing_aplhanums Counter object of a given segment.
    '''
    error_string = ''
    for item in error_list:
        item_count = error_list[item]
        for x in range(item_count):
            error_string = error_string + str(item) + ', '
    error_string = error_string.strip(', ')
    return error_string
