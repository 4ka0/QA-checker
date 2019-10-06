#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for outputting results.
'''
def output_results(segments):

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
                print("MISSING NUMBER FOUND: " + str(segment.missing_nums))
                errors_found_overall = True

            # Results for extra numbers
            if len(segment.extra_nums) > 0:
                print("EXTRA NUMBER FOUND: " + str(segment.extra_nums))
                errors_found_overall = True

            # Results for double-spaces
            if segment.double_space == True:
                print("DOUBLE-SPACE FOUND.")
                errors_found_overall = True

            print("\n")

    if errors_found_overall == False:
        print("NO ERRORS FOUND.")