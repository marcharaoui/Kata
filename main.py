# =========================================== #
# Kata project: number2WORD
# Main script
# Marc Haraoui - created on 05/02/2024
# =========================================== #

import argparse
from check_data import examine
from convert_to_french import Int2French
from convert_to_english import Int2English
from convert_to_spanish import Int2Spanish

# =============== Parameters ================ #

complete_data = {}

# =========================================== #

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Converter')
    parser.add_argument('--language',
                        help    = 'insert language(s) to convert to (default is french)',
                        choices = ["french", "english", "spanish"],
                        nargs   = '+',
                        type    = str,
                        default = ["french"])
    parser.add_argument('--number',
                        help    = 'insert integer(s) to be converted (between 0 and 999 999)',
                        nargs   ='+', 
                        type    = int,
                        default = [0, 21, 71, 101, 9999, 12345, 999900])

    args = parser.parse_args()

    # Chosen languages
    print(f"Languages chosen: {args.language}")

    # Dataset checkup
    input = args.number
    examine(input) # Check if input is a list of ints
    
    # Preparing the data dictionary
    complete_data["input"] = input
    for lang in args.language:
        complete_data[lang] = []

        # Creating the language objects
        if lang == "french":
                converter = Int2French()  
        elif lang == "english":
                converter = Int2English()
        elif lang == "spanish":
                converter = Int2Spanish()
        else: raise ValueError("No language to convert to!")

        # Convert one int at a time
        for int_data in input:
                complete_data[lang].append(converter.translate(int_data)) # Converting numbers and storing results

    # Print input and outputs
    print(complete_data) 
