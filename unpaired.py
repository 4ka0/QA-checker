#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def unpaired_symbol_check(segments):
    """
    Function for checking for unpaired symbols such as quotation marks,
    brackets, and parentheses.
    """

    symbol_pairs = {"(":")", "[":"]", "{":"}"}

    """
    Dict containing number of instances of each symbol
    Key = symbol, value = number of instances of that symbol
    """
    symbol_counts = {}

    for segment in segments:

        """
        Count instances of each symbol and add to dictionary
        Key = symbol, value = number of instances of that symbol
        start_symbol = "(", for example
        end_symbol = ")", for example
        """
        for start_symbol in symbol_pairs:
            end_symbol = symbol_pairs[start_symbol]
            symbol_counts[start_symbol] = segment.eng_text.count(start_symbol)
            symbol_counts[end_symbol] = segment.eng_text.count(end_symbol)

        # Compare instances of start and end symbols (should match)
        for start_symbol in symbol_pairs:
            start_symbol_count = symbol_counts[start_symbol]
            end_symbol = symbol_pairs[start_symbol]
            end_symbol_count = symbol_counts[end_symbol]
            if start_symbol_count != end_symbol_count:
                segment.unpaired_symbols.append(start_symbol + end_symbol)
                segment.unpaired_symbol_found = True
                segment.error_found = True

        # Look for double quotation marks, if found, should be multiple of 2
        if "\"" in segment.eng_text:
            if segment.eng_text.count("\"") % 2 != 0:
                segment.unpaired_symbols.append("\"\"")
                segment.unpaired_symbol_found = True
                segment.error_found = True

        # Look for single quotation marks, similar to above
        # BUG - PICKS UP APOSTROPHE MARKS AS UNPAIRED SINGLE QUOTATIONS MARKS
        # start single quote always preceded by space " \'"
        if "\'" in segment.eng_text:
            if segment.eng_text.count("\'") % 2 != 0:
                segment.unpaired_symbols.append("\'\'")
                segment.unpaired_symbol_found = True
                segment.error_found = True

    return segments
