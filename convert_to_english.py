# =========================================== #
# Kata project: number2word
# convert_to_english script: take an int and translates it to english in string
# Marc Haraoui - created on 14/02/2024
# =========================================== #

from language import Lang

# =========================================== #

class Int2English(Lang):
    def __init__(self):
        # 0 to 19 have no rules and are the following
        self.units = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
            14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }

        self.tens = {
            20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
        }

    def translate(self, number):
        if number in self.units:
            return self.units[number]
        
        elif number < 100:
            remainder = number % 10
            base = number - remainder
            return self.tens[number] if remainder == 0 else self.tens[base] + '-' + self.units[remainder]

        elif number < 1000:
            first_value = number // 100
            remainder   = number % 100
            if remainder == 0:
                return self.units[first_value] + ' hundred'
            hundred_str = ' hundred and ' if first_value == 1 else ' hundred '
            return self.units[first_value] + hundred_str + self.translate(remainder)

        elif number < 1000000:
            first_value = number // 1000
            remainder   = number % 1000
            if remainder == 0:
                return self.translate(first_value) + ' thousand'
            return self.translate(first_value) + ' thousand ' + self.translate(remainder)


# Quick test to see if everything works
if __name__ == "__main__":
    test_cases = [0, 22, 71, 131, 231, 700, 1000, 1999, 9871, 60001, 80000, 200000, 999900]
    converter = Int2English()

    for case in test_cases:
        output = converter.translate(case)
        print(f"{case}: {output}")