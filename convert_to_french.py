# =========================================== #
# Kata project: number2word
# convert_to_french script: take an int and translates it to french in string
# Marc Haraoui - created on 05/02/2024
# =========================================== #

from language import Lang

# =========================================== #

class Int2French(Lang):
    def __init__(self):
        # 0 to 16 have no rules and are the following
        self.units = {
            0: 'zéro', 1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre',
            5: 'cinq', 6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf',
            10: 'dix', 11: 'onze', 12: 'douze', 13: 'treize',
            14: 'quatorze', 15: 'quinze', 16: 'seize'
        }

        # The rules behind tens
        self.tens = {
            20: 'vingt', 30: 'trente', 40: 'quarante', 50: 'cinquante',
            60: 'soixante', 70: 'soixante-dix', 80: 'quatre-vingts', 90: 'quatre-vingt-dix'
        }

    def translate(self, number, noCardinal=True):
        if number in self.units:
            return self.units[number]

        elif number < 20:
            return 'dix-' + self.units[number - 10]

        elif number < 70:
            base = number - number % 10
            if number % 10 == 0: return self.tens[base]
            return self.tens[base] + '-et-' + self.units[number % 10] if number % 10 == 1 else self.tens[base] + '-' + self.units[number % 10]

        elif number < 80:
            return 'soixante-et-' + self.translate(number - 60) if number % 10 == 1 else 'soixante-' + self.translate(number - 60)
        
        elif number < 100:
            if number == 80 : return 'quatre-vingts' if noCardinal else 'quatre-vingt'
            return 'quatre-vingt-' + self.translate(number - 80)

        elif number < 1000:
            first_value = number // 100
            remainder   = number % 100
            if remainder == 0:
                if first_value == 1: return 'cent'  
                return self.units[first_value] + '-cents' if noCardinal else self.units[first_value] + '-cent'
            else:
                return 'cent-' + self.translate(number % 100) if first_value == 1 else self.units[first_value] + '-cent-' + self.translate(number % 100)

        elif number < 1000000:
            factor = number // 1000
            remainder = number % 1000
            if factor == 1:
                prefix = 'mille'
            else:
                prefix = self.translate(factor, noCardinal=False) + '-mille'
            if remainder == 0: return prefix
            return prefix + '-' + self.translate(remainder)
            
# Quick test to see if everything works
if __name__ == "__main__":
    test_cases = [0, 22, 71, 131, 231, 700, 1000, 1999, 60001, 9871, 80000, 200000, 999900]
    converter = Int2French()

    for case in test_cases:
        output = converter.translate(case)
        print(f"{case}: {output}")
