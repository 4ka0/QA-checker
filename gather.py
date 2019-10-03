#!/usr/bin/env python3

'''
Translate-toolkit used to parse TMX file.
http://docs.translatehouse.org/projects/translate-toolkit/en/latest/api/storage.html#module-translate.storage.tmx
'''

import sys
from translate.storage.tmx import tmxfile

'''
Object for each Japanese-English segment.
Includes actual segment text and variables for QA checks.
'''
class Segment():
    def __init__(self, jap="", eng="", japNums=[], engNums=[], missingNums = [], extraNums = [], doubleSpace = False, repeatedWord = False, unpairedSymbol = False, untranslatedSeg = False):
        self.jap = jap # Japanese text
        self.eng = eng # English text
        self.japNums = japNums # Numbers extracted from Japanese text
        self.engNums = engNums # Numbers extracted from English text
        self.missingNums = missingNums # Numbers missing from English text
        self.extraNums = extraNums # Extra numbers found in English text
        self.doubleSpace = doubleSpace # Flag = True if double spaces found
        self.repeatedWord = repeatedWord # Flag = True if repeated words found
        self.unpairedSymbol = unpairedSymbol # Flag = True if unpaired symbols found (parentheses etc.)
        self.untranslatedSeg = untranslatedSeg # Flag = True if no English text is found

'''
Function for gathering translations segments from a TMX file.
'''
def gatherSegments():

    file = sys.argv[-1] # Gets last command line argument (filename here)
    with open(file, 'rb') as f:
        tmx_file = tmxfile(f)

    segments = [] # List of Segment objects

    # Iterates oves TMX file and extracts text from segments.
    for node in tmx_file.unit_iter():
        jap = node.getsource()
        eng = node.gettarget()
        segment = Segment(jap, eng)
        segments.append(segment)

    return segments