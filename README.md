# Honyaku checker

A command line script for performing basic QA checks on a tmx file of a Japanese to English translation.

### Checks for the following issues:

* Untranslated segments
* Inconsistent numbers
* Consecutive spaces
* Leading spaces
* Trailing spaces
* Repeated words
* Repeated two-word combinations
* Unpaired symbols
* Leading capitalization
* Inconsistent ending punctuation
* Fullwidth characters included in the target text

### Running the script

From the directory containing this script, terminal:
```
python3 main.py translation.tmx
```

### Prerequisites

* Python 3
* [colorama 0.4.3](https://pypi.org/project/colorama/)
* [translate-toolkit 2.5.0](https://pypi.org/project/translate-toolkit/)
* [pytest 5.4.1](https://docs.pytest.org/en/latest/getting-started.html) (for running the tests)

### Built using:

* Python 3.7.5
* Visual Studio Code 1.44.2
* macOS 10.14.6

### License

Licensed under the MIT License.
