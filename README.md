# Kata
Kata: number to word converter

## Introduction

This work is done on Python and the goal is to take a list of int numbers and to translate them using a list of strings. 
The input and results are stored in a dictionary.  

## How to use
This is a Python package that has the following scripts:
- **main.py:** This script is the main script, it takes an input dataset and will output the final result. To do so, it uses the other scripts,
- **check_data.py:** This script checks if the dataset has the right structure and types. It needs to be a list of ints,
- **language.py:** This script represents an abstract class that helps define common interface to control different language classes,
- **convert_to_french.py:** This script takes a number, analyses it in french and outputs the corresponding string values,
- **convert_to_english.py:** This script takes a number, analyses it in english and outputs the corresponding string values.

Open a terminal in the project directory, and run the following command line: `python main.py`.

You can also add input arguments concerning the language(s) and number(s) desired. An example of this would be: `python main.py --language english --number 5 21 1945 5555 957398`.

### Additional information
The Kata project isan open-source project, free for anyone to use and explore. 

So far, it can convert numbers to french and english. However, there are no obstacles in adding additional languages, go nuts!

Finally, it can convert any integer between the values of 0 and 999 999. Of course, it is possible to improve it in order to reach even larger numbers, the sky is the limit!

### Tested on
Python 3.10.6
