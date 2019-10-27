Lightweight script for performing various QA checks on a tmx file, specifically Japanese to English translations of patent texts (namely my own translation work).

Targets the following issues:
  - Double spaces
  - Untranslated segments
  - Unpaired symbols (such as parentheses, square brackets, braces, and double quotation marks)
  - Repeated words (single words such as "the the" and also two-word combinations such as "for the for the")
  - Consistency between numbers in source and target segments (i.e. missing or extra numbers in the target segment)
  - Consistency between component reference numbers (alphanumerical combinations such as "100a" and "240B", which often appear in patent texts after components)

Run from the command line with the following (results sent to stdout):
`python3 QA-checker.py yourfile.tmx`
