#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def output_results(segments):
"""
Function for outputting results.
"""

    print("\n****************\nRESULTS:\n")

    errors_found_overall = False

    for segment in segments:

        if segment.error_found == True:

            print("ERROR FOUND IN THE FOLLOWING SEGMENT.")
            print("JAPANESE TEXT:")
            print(segment.jap_text)
            print("ENGLISH TEXT:")
            print(segment.eng_text)
            print("ERROR:")

            # Results for missing numbers
            if len(segment.missing_nums) > 0:
                missing_nums_string = build_error_string(segment.missing_nums)
                if len(segment.missing_nums) > 1:
                    print("MISSING NUMBERS FOUND: " + missing_nums_string)
                else:
                    print("MISSING NUMBER FOUND: " + missing_nums_string)
                errors_found_overall = True

            # Results for extra numbers
            if len(segment.extra_nums) > 0:
                extra_nums_string = build_error_string(segment.extra_nums)
                if len(segment.extra_nums) > 1:
                    print("EXTRA NUMBERS FOUND: " + extra_nums_string)
                else:
                    print("EXTRA NUMBER FOUND: " + extra_nums_string)
                errors_found_overall = True

            # Results for double-spaces
            if segment.double_space_found == True:
                print("DOUBLE-SPACE FOUND.")
                errors_found_overall = True

            # Results for repeated words
            if segment.repeated_word_found == True:
                print("REPEATED WORDS FOUND: " + str(segment.repeated_words))
                errors_found_overall = True

            # Results for unpaired symbols
            if segment.unpaired_symbol_found == True:
                unpaired_symbol_string = build_error_string(segment.unpaired_symbols)
                if len(segment.unpaired_symbols) > 1:
                    print("POSSIBLE UNPAIRED SYMBOLS FOUND: " + unpaired_symbol_string)
                else:
                    print("POSSIBLE UNPAIRED SYMBOL FOUND: " + unpaired_symbol_string)
                errors_found_overall = True

            print("\n")

    if errors_found_overall == False:
        print("NO ERRORS FOUND.")


"""
Function for building a single string from given list of elements.
E.g. building a single string from all ints in the missing_nums list of a given segment.
"""
def build_error_string(error_list):
	error_string = ""
	for item in error_list:
		error_string = error_string + str(item) + ", "
	# Remove final unnecessary comma
	error_string = error_string[0:-2]
	return error_string
