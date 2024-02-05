# =========================================== #
# Kata project: number2french
# check_data script: examine if input is a list of ints
# Marc Haraoui - created on 05/02/2024
# =========================================== #

def examine(input):
    if not isinstance(input, list):
        raise ValueError("Input is not a list")
    elif input == []:
        raise ValueError("Input is empty")
    else:
        for data in input:
            if not isinstance(data, int):
                raise ValueError("Input values are not integers")
        return True

# Quick test to see if everything works
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],              # This should work
        "This will not work",   # Not a list 
        [],                     # Empty list
        [1, 2.0, 3]             # List has non-integer values
    ]

    for case in test_cases:
        try: 
            output = examine(case)
            print(f"Testing input {case}: Passed")
        except ValueError as e:
            print(f"Testing input {case}: Failed - '{e}'")