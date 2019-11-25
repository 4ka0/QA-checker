Script for performing basic QA checks on a tmx file of a Japanese to English translation.

Checks for the following issues:
- Untranslated segments
- Inconsistent numbers
- Consecutive spaces
- Leading spaces
- Trailing spaces
- Repeated words
- Repeated two-word combinations
- Unpaired symbols
- Leading capitalization
- Inconsistent ending punctuation
- Fullwidth characters in target

Takes three arguments to execute from the command line:
python3 checker.py yourfile.tmx

Results sent to stdout
