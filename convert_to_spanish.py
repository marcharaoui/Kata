# =========================================== #
# Kata project: number2word
# convert_to_spanish script: take an int and translates it to spanish in string
# Marc Haraoui - created on 15/02/2024
# =========================================== #

from language import Lang

# =========================================== #

class Int2Spanish(Lang):
    def __init__(self):
        # 0 to 29 have no rules and are the following
        self.units = {
            0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro',
            5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve',
            10: 'diez', 11: 'once', 12: 'doce', 13: 'trece', 
            14: 'catorce', 15: 'quince', 16: 'dieciséis', 17: 'diecisiete',
            18: 'dieciocho', 19: 'diecinueve', 20: 'veinte', 21: 'veintiuno', 
            22:'veintidós', 23: 'veintitrés', 24: 'veinticuatro', 25: 'veinticinco',
            26: 'veintiséis', 27: 'veintisiete', 28: 'veintiocho', 29: 'veintinueve'
        }

        self.tens = {
            30: 'treinta', 40: 'cuarenta', 50: 'cincuenta',
            60: 'sesenta', 70: 'setenta', 80: 'ochenta', 90: 'noventa'
        }

    def translate(self, number):
        if number in self.units:
            return self.units[number]
        
        elif number < 100:
            remainder = number % 10
            base = number - remainder
            return self.tens[number] if remainder == 0 else self.tens[base] + ' y ' + self.units[remainder]

        elif number < 1000:
            first_value = number // 100
            remainder   = number % 100
            if remainder == 0:
                if first_value == 1: return 'cien'
                elif first_value == 5: return 'quinientos'  # 500 is a special word
                elif first_value == 7: return 'setecientos' # 700 is a special word
                elif first_value == 9: return 'novecientos' # 900 is a special word
                else: return self.units[first_value] + 'cientos'
            else:
                if first_value == 1: return 'ciento ' + self.translate(remainder) 
                elif first_value == 5: return 'quinientos '  + self.translate(remainder) 
                elif first_value == 7: return 'setecientos ' + self.translate(remainder) 
                elif first_value == 9: return 'novecientos ' + self.translate(remainder) 
                else: return self.units[first_value] + 'cientos ' + self.translate(remainder)

        elif number < 1000000:
            first_value = number // 1000
            remainder   = number % 1000
            if remainder == 0:
                return 'mil' if first_value == 1 else self.translate(first_value) + ' mil'
            return 'mil ' + self.translate(remainder) if first_value == 1 else self.translate(first_value) + ' mil ' + self.translate(remainder)

# Quick test to see if everything works
if __name__ == "__main__":
    test_cases = [0, 20, 22, 33, 70, 131, 231, 700, 1000, 1999, 9871, 60001, 80000, 200000, 999900]
    converter = Int2Spanish()

    for case in test_cases:
        output = converter.translate(case)
        print(f"{case}: {output}")