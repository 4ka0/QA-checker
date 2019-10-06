#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for outputting results.
'''
def outputResults(segments):

    print("\n****************")
    print("RESULTS:")
    
    errorsFound = False

    for segment in segments:

        if len(segment.missingNums) > 0:
        
            errorsFound = True
            print("MISSING NUMBER(S):")
            print(segment.missingNums)
            print(segment.jap)
            print(segment.eng)
            print("\n")

    if errorsFound == False:
        print("No errors found.")