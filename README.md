Program for performing various QA checks on a Jap>Eng TMX file.

Checks for the following issues:
  - Inconsistent numbers (missing or extra numbers)
  - Double spaces etc.
  - Repeated words
  - Unpaired symbols such as parentheses
  - Untranslated segments

Takes three arguments to execute from the command line:
  python3 QA-checker.py <your tmx file>

Results sent to stdout.
