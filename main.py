# =========================================== #
# Kata project: number2french
# Main script
# Marc Haraoui - created on 05/02/2024
# =========================================== #

from check_data import examine
from convert_data import Int2French

# =============== Parameters ================ #

results_list = [] 

# =========================================== #

if __name__ == "__main__":
    
    # Dataset checkup
    input = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
    examine(input) # Check if input is a list of ints

    # Create object 
    converter = Int2French()

    for int_data in input:
        str_data = converter.translate2french(int_data) # Convert ont int at a time
        results_list.append(str_data) # Store value in a list
    
    print(results_list) # Final results