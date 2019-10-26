Lightweight program for performing various QA checks on a tmx (translation memory exchange) file.

Targets the following issues:
  - Inconsistent numbers between source and target segments (i.e. missing or extra numbers in the target segment)
  - Alphanumerical combinations such as "100a" and "240B", which often appear as reference numbers in Japanese patent texts)
  - Repeated words (single words such as "the the" and two-word combinations such as "and the and the")
  - Unpaired symbols such as parentheses, square brackets, braces, and double quotation marks
  - Double spaces
  - Untranslated segments

Takes three arguments to execute from the command line:
  python3 QA-checker.py yourfile.tmx

Results sent to stdout.

Note:
This program has been designed for and tested with only Jap>Eng translations of patent texts, namely my own translation work.
