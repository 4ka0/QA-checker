#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Function for checking for unpaired symbols such as quotation marks, brackets, parentheses, etc.
'''
def unpaired_symbol_check(segments):

    # Dict containing starting symbols and corresponding ending symbols
    starting_symbols = {"(":")", "[":"]", "{":"}", "<":">"}

    # Dict containing ending symbols and corresponding starting symbols
    ending_symbols = {")":"(", "]":"[", "}":"{", ">":"<"}

    for segment in segments:

        eng_text_copy = segment.eng_text
        
        # Look for starting symbols
        for symbol in starting_symbols:
        
            while symbol in eng_text_copy:
        
                if starting_symbols[symbol] in eng_text_copy:
                    # Ending symbol found, no error
                    # Replace both symbols in copy with "@" so not found again
                    eng_text_copy = eng_text_copy.replace(symbol, "@", 1)
                    eng_text_copy = eng_text_copy.replace(starting_symbols[symbol], "@", 1)
        
                else:
                    # Ending symbol not found, error
                    # Replace starting symbol in copy with "@" so not found again
                    eng_text_copy = eng_text_copy.replace(symbol, "@", 1)
                    segment.unpaired_symbols.append(symbol)
                    segment.unpaired_symbol_found = True
                    segment.error_found = True

        # Look for ending symbols, similar to above
        for symbol in ending_symbols:
        
            while symbol in eng_text_copy:
        
                if ending_symbols[symbol] in eng_text_copy:
                    eng_text_copy = eng_text_copy.replace(symbol, "@", 1)
                    eng_text_copy = eng_text_copy.replace(ending_symbols[symbol], "@", 1)
        
                else:
                    eng_text_copy = eng_text_copy.replace(symbol, "@", 1)
                    segment.unpaired_symbols.append(symbol)
                    segment.unpaired_symbol_found = True
                    segment.error_found = True

        # Look for double quotation marks, if found, should be multiple of 2
        if "\"" in eng_text_copy:
            if eng_text_copy.count("\"") % 2 != 0:
                segment.unpaired_symbols.append("\"")
                segment.unpaired_symbol_found = True
                segment.error_found = True

        # Look for single quotation marks, similar to above
        # BUG - picks up apostrophe marks as unpaired single quotations marks
        if "\'" in eng_text_copy:
            if eng_text_copy.count("\'") % 2 != 0:
                segment.unpaired_symbols.append("\'")
                segment.unpaired_symbol_found = True
                segment.error_found = True

    return segments