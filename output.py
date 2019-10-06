#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for outputting results.
'''
def output_results(segments):

    print("\n****************")
    print("RESULTS:")
    
    errors_found = False

    for segment in segments:

        if len(segment.missing_nums) > 0:
        
            errors_found = True
            print("MISSING NUMBER(S):")
            print(segment.missing_nums)
            print(segment.jap_text)
            print(segment.eng_text)
            print("\n")

    if errors_found == False:
        print("No errors found.")