Program for performing various QA checks on a Jap>Eng TMX file.

Checks for the following issues:
  - Inconsistent numbers (missing numbers or extra numbers)
  - Double spaces etc.
  - Repeated words
  - Unpaired symbols such as parentheses
  - Untranslated segments

Takes three arguments to execute from the command line:
python3 main.py file.tmx
Results sent to stdout.
