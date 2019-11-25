# -*- coding: utf-8 -*-

from colorama import Fore
import xml.etree.ElementTree as ET


class Segment():
    '''
    Used to create an object for each source-target segment.
    Includes actual segment text and numerous variables for QA checks.
    '''

    def __init__(self,
                 source_text,  # String, source text
                 target_text,  # String, target text
                 source_lang,  # String, source language
                 target_lang,  # String, target language
                 source_nums,  # List, digits extracted from source text
                 target_nums,  # List, digits extracted from target text
                 error_found,  # Boolean, True if any errors are found
                 missing_nums,  # Dict, numbers missing from target text
                 extra_nums,  # Dict, extra numbers found in target text
                 consecutive_space_found,  # Boolean, True if found
                 leading_space_found,  # Boolean, True if found
                 trailing_space_found,  # Boolean, True if found
                 capitalization_error_found,  # Boolean, True if found
                 trailing_punctuation_error,  # Boolean, True if found
                 repeated_word_found,  # Boolean, True if found
                 repeated_words,  # List, repeated words if found
                 unpaired_symbol_found,  # Boolean, True if found
                 unpaired_symbols,  # List, unpaired symbols if found
                 untranslated_seg,  # Boolean, True if no target text is found
                 asian_char_found,  # Boolean, True if found in target text
                 asian_chars):  # List of Asian chars found in target text

        self.source_text = source_text
        self.target_text = target_text
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.source_nums = source_nums
        self.target_nums = target_nums
        self.error_found = error_found
        self.missing_nums = missing_nums
        self.extra_nums = extra_nums
        self.consecutive_space_found = consecutive_space_found
        self.leading_space_found = leading_space_found
        self.trailing_space_found = trailing_space_found
        self.capitalization_error_found = capitalization_error_found
        self.trailing_punctuation_error = trailing_punctuation_error
        self.repeated_word_found = repeated_word_found
        self.repeated_words = repeated_words
        self.unpaired_symbol_found = unpaired_symbol_found
        self.unpaired_symbols = unpaired_symbols
        self.untranslated_seg = untranslated_seg
        self.asian_char_found = asian_char_found
        self.asian_chars = asian_chars


def gather_segments(file):
    '''
    Function for gathering translation segments from a tmx file.
    '''

    segments = []  # To be used as a list of Segment objects

    '''
    Attempt to open the tmx file given by the user.
    If it doesn't exist, an error message is output and the program quits.
    '''
    try:
        with open(file, 'rb') as tmx_file:
            tree = ET.parse(tmx_file)
    except FileNotFoundError as fnf_error:
        print(Fore.RED + str(fnf_error))
        quit()
    else:
        '''
        Basic tmx structure:
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE tmx SYSTEM "tmx11.dtd">
        <tmx version="1.1">
            <header srclang="JA" ... />
            <body>
            <tu>
                <tuv lang="JA">
                    <seg>日本語日本語日本語</seg>
                </tuv>
                <tuv lang="EN-US" ... >
                    <seg>English English English</seg>
                </tuv>
            </tu>
        '''
        root = tree.getroot()
        header = root.find('./header')
        source_lang = header.get('srclang')
        segments = []

        # Look at each 'tu' node
        for tu in root.iter('tu'):

            target_lang = ''
            source_text = ''
            target_text = ''

            # Any children present? Should be 2 'tuv' nodes
            if len(tu) > 0:

                for child in tu:

                    # Only look at 'tuv' children
                    if child.tag == 'tuv':

                        # Get language
                        lang = child.get('lang')

                        # Set target language if appropriate
                        if lang != source_lang:
                            target_lang = lang

                        # Any children present? Should be 1 'seg' node
                        if len(child) > 0:

                            for subchild in child:

                                # Only look at 'seg' child nodes
                                if subchild.tag == 'seg':

                                    '''
                                    Source or target text?
                                    Check if text exists.
                                    If not, assign empty string
                                    to avoid 'None' being assigned.
                                    '''
                                    if target_lang == '':
                                        if subchild.text:
                                            source_text = subchild.text
                                        else:
                                            source_text = ''
                                    else:
                                        if subchild.text:
                                            target_text = subchild.text
                                        else:
                                            target_text = ''

            segment = Segment(source_text,
                              target_text,
                              source_lang,
                              target_lang,
                              [],  # source_nums
                              [],  # target_nums
                              False,  # error_found
                              {},  # missing_nums
                              {},  # extra_nums
                              False,  # consecutive_space_found
                              False,  # leading_space_found
                              False,  # trailing_space_found
                              False,  # capitalization_error_found
                              False,  # trailing_punctuation_error
                              False,  # repeated_word_found
                              [],  # repeated_words
                              False,  # unpaired_symbol_found
                              [],  # unpaired_symbols
                              False,  # untranslated_seg
                              False,  # asian_char_found
                              [])  # asian_chars

            segments.append(segment)

        return segments
