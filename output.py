#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init
from colorama import Fore


def output_results(segments):
    '''
    Function for outputting QA check results.
    '''

    init() # To activate colored output on Windows OS

    print('\n****************\nRESULTS:\n')

    errors_found_overall = False

    for segment in segments:

        if segment.error_found == True:

            # Results for missing numbers
            if len(segment.missing_nums) > 0:
                missing_nums_string = list_string(segment.missing_nums)
                if len(segment.missing_nums) > 1:
                    print(Fore.RED + 'MISSING NUMBERS FOUND: ' + missing_nums_string)
                else:
                    print(Fore.RED + 'MISSING NUMBER FOUND: ' + missing_nums_string)
                errors_found_overall = True

            # Results for extra numbers
            if len(segment.extra_nums) > 0:
                extra_nums_string = list_string(segment.extra_nums)
                if len(segment.extra_nums) > 1:
                    print(Fore.RED + 'EXTRA NUMBERS FOUND: ' + extra_nums_string)
                else:
                    print(Fore.RED + 'EXTRA NUMBER FOUND: ' + extra_nums_string)
                errors_found_overall = True

            # Results for double-spaces
            if segment.double_space_found == True:
                print(Fore.RED + 'DOUBLE-SPACE FOUND.')
                errors_found_overall = True

            # Results for repeated words
            if segment.repeated_word_found == True:
                repeated_word_string = list_string(segment.repeated_words)
                print(Fore.RED + 'REPEATED WORDS FOUND: ' + repeated_word_string)
                errors_found_overall = True

            # Results for unpaired symbols
            if segment.unpaired_symbol_found == True:
                unpaired_symbol_string = list_string(segment.unpaired_symbols)
                if len(segment.unpaired_symbols) > 1:
                    print(Fore.RED + 'UNPAIRED SYMBOLS FOUND: ' + unpaired_symbol_string)
                else:
                    print(Fore.RED + 'UNPAIRED SYMBOL FOUND: ' + unpaired_symbol_string)
                errors_found_overall = True

            # Results for missing aplhanums
            if len(segment.missing_refnums) > 0:
                refnum_string = dict_string(segment.missing_refnums)
                if ',' in refnum_string:
                    print(Fore.RED + 'MISSING REFERENCE NUMBERS FOUND: ' + refnum_string)
                else:
                    print(Fore.RED + 'MISSING REFERENCE NUMBER FOUND: ' + refnum_string)
                errors_found_overall = True

            # Results for extra aplhanums
            if len(segment.extra_refnums) > 0:
                refnum_string = dict_string(segment.extra_refnums)
                if ',' in refnum_string:
                    print(Fore.RED + 'EXTRA REFERENCE NUMBERS FOUND: ' + refnum_string)
                else:
                    print('EXTRA REFERENCE NUMBER FOUND: ' + refnum_string)
                errors_found_overall = True

            print(Fore.CYAN + 'JAPANESE:')
            print(Fore.RESET + segment.jap_text)
            print(Fore.CYAN + 'ENGLISH:')
            print(Fore.RESET + segment.eng_text)
            print('\n')

    if errors_found_overall == False:
        print(Fore.GREEN + '\nNO ERRORS FOUND.\n')


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
    missing_refnums Counter object of a given segment.
    '''
    error_string = ''
    for item in error_list:
        item_count = error_list[item]
        for x in range(item_count):
            error_string = error_string + str(item) + ', '
    error_string = error_string.strip(', ')
    return error_string
