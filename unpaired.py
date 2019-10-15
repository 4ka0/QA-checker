#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking for unpaired symbols such as quotation marks, brackets, parentheses, etc.
'''
def unpaired_symbol_check(segments):

    '''
    (logic similar to missing numbers)
    loop through string
        find starting symbols and add to list
        find ending symbols and add to list
    loop through starting symbol list
        look for coresponding ending symbol
        if found: remove starting symbol from starting symbol list
                : remove ending symbol from ending symbol list
        any remaining in starting symbol list = missing starting symbol
    loop through ending symbol list
        do opposite of above loop to find missing ending symbols

    starting symbols = (, [, {, <, ", '
    ending symbols = ), ], }, >, ", '
    '''

    # Dict containing starting symbols and their corresponding ending symbols
    starting_symbols = {"(":")", "[":"]", "{":"}", "<":">", "\"":"\"", "\'":"\'"}
    ending_symbols = {")":"(", "]":"[", "}":"{", ">":"<", "\"":"\"", "\'":"\'"}

    # BUG - doesn't find missing parenthesis in "(see Figs. (2, 3, 5, and 6)"

    # check for missing ending symbols
    for segment in segments:
        eng_text_copy = segment.eng_text
        # print("\n" + eng_text_copy)
        for symbol in starting_symbols:
            # print("Target symbol: " + symbol)
            # check to see if starting symbol is present
            if symbol in eng_text_copy:
                # print("Starting symbol found: " + symbol)
                # check to see if corresponding ending symbol is present
                if starting_symbols[symbol] in eng_text_copy:
                    # print("Ending symbol found: " + starting_symbols[symbol])
                    # ending symbol found = no error
                    # replace both symbols in copy with "@" so not searched again
                    eng_text_copy = eng_text_copy.replace(symbol, "@", 1)
                    eng_text_copy = eng_text_copy.replace(starting_symbols[symbol], "@", 1)
                else:
                    # print("Ending symbol not found: " + starting_symbols[symbol])
                    # ending symbol not found = error
                    # replace starting symbol in copy with "@" so not searched again
                    eng_text_copy = eng_text_copy.replace(symbol, "@", 1)
                    # add symbol to list of missing symbols
                    segment.missing_symbols.append(symbol)
                    # raise errors
                    segment.unpaired_symbol = True
                    segment.error_found = True
            # print("eng_text_copy: ")
            # print(eng_text_copy)



    return segments