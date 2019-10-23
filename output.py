#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def output_results(segments):
    '''
    Function for outputting QA check results.
    '''

    print('\n****************\nRESULTS:\n')

    errors_found_overall = False

    for segment in segments:

        if segment.error_found == True:

            # Results for missing numbers
            if len(segment.missing_nums) > 0:
                missing_nums_string = list_string(segment.missing_nums)
                if len(segment.missing_nums) > 1:
                    print('MISSING NUMBERS FOUND: ' +
                        missing_nums_string)
                else:
                    print('MISSING NUMBER FOUND: ' +
                        missing_nums_string)
                errors_found_overall = True

            # Results for extra numbers
            if len(segment.extra_nums) > 0:
                extra_nums_string = list_string(segment.extra_nums)
                if len(segment.extra_nums) > 1:
                    print('EXTRA NUMBERS FOUND: ' + extra_nums_string)
                else:
                    print('EXTRA NUMBER FOUND: ' + extra_nums_string)
                errors_found_overall = True

            # Results for double-spaces
            if segment.double_space_found == True:
                print('DOUBLE-SPACE FOUND.')
                errors_found_overall = True

            # Results for repeated words
            if segment.repeated_word_found == True:
                repeated_word_string = \
                    list_string(segment.repeated_words)
                print('REPEATED WORDS FOUND: ' + repeated_word_string)
                errors_found_overall = True

            # Results for unpaired symbols
            if segment.unpaired_symbol_found == True:
                unpaired_symbol_string = \
                    list_string(segment.unpaired_symbols)
                if len(segment.unpaired_symbols) > 1:
                    print('POSSIBLE UNPAIRED SYMBOLS FOUND: ' +
                        unpaired_symbol_string)
                else:
                    print('POSSIBLE UNPAIRED SYMBOL FOUND: ' +
                        unpaired_symbol_string)
                errors_found_overall = True

            # Results for missing aplhanums
            if len(segment.missing_alphanums) > 0:
                alphanum_string = dict_string(segment.missing_alphanums)
                if len(segment.missing_alphanums) > 1:
                    print('MISSING ALPHANUMS FOUND: ' + alphanum_string)
                else:
                    print('MISSING ALPHANUM FOUND: ' + alphanum_string)
                errors_found_overall = True

            # Results for extra aplhanums
            if len(segment.extra_alphanums) > 0:
                alphanum_string = dict_string(segment.extra_alphanums)
                if len(segment.extra_alphanums) > 1:
                    print('EXTRA ALPHANUMS FOUND: ' + alphanum_string)
                else:
                    print('EXTRA ALPHANUM FOUND: ' + alphanum_string)
                errors_found_overall = True

            print('JAPANESE TEXT:')
            print(segment.jap_text)
            print('ENGLISH TEXT:')
            print(segment.eng_text)
            print('\n')

    if errors_found_overall == False:
        print('NO ERRORS FOUND.')


def list_string(error_list):
    '''
    Function for building a single string from a list.
    E.g. builds a single string from all ints in the
    missing_nums list of a given segment.
    '''
    error_string = ''
    for item in error_list:
        error_string = error_string + str(item) + ', '
    # Remove final unnecessary comma
    error_string = error_string[0:-2]
    return error_string


def dict_string(error_list):
    '''
    Function for building a single string from a dict.
    E.g. builds a single string from all keys and values in the
    missing_alphanums Counter object of a given segment.
    '''
    error_string = ''
    for item in error_list:
        error_string = error_string + str(item) + ' (x' + \
            str(error_list[item]) + '), '
    # Remove final unnecessary comma
    error_string = error_string[0:-2]
    return error_string
