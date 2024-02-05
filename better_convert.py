# =========================================== #
# Kata project: number2french
# better_convert script: takes an int and translates it to a french in string (With the help of ChatGPT)
# Marc Haraoui - created on 05/02/2024
# =========================================== #

class Number2French:
    def __init__(self):
        self.units = {
            0: 'zéro', 1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre',
            5: 'cinq', 6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf',
            10: 'dix', 11: 'onze', 12: 'douze', 13: 'treize',
            14: 'quatorze', 15: 'quinze', 16: 'seize'
        }
        self.tens = {
            20: 'vingt', 30: 'trente', 40: 'quarante', 50: 'cinquante',
            60: 'soixante', 70: 'soixante-dix', 80: 'quatre-vingts', 90: 'quatre-vingt-dix'
        }
        self.big = {
            100: 'cent', 1000: 'mille'
        }

    def translate2french(self, number):
        if number in self.units:
            return self.units[number]

        elif number < 20:
            return 'dix-' + self.units[number - 10]

        elif number < 70:
            base = number - number % 10
            if number % 10 == 0:
                return self.tens[base]
            else:
                return self.tens[base] + '-et-' + self.units[number % 10] if number % 10 == 1 else self.tens[base] + '-' + self.units[number % 10]

        elif number < 80:
            return 'soixante-' + self.translate2french(number - 60)

        elif number < 100:
            if number == 80: return 'quatre-vingts'
            return 'quatre-vingt-' + self.translate2french(number - 80)

        elif number < 1000:
            first_value = int(str(number)[0])
            if number % 100 == 0:
                return self.units[first_value] + ' cent' if first_value == 1 else self.units[first_value] + ' cents'
            else:
                return self.units[first_value] + ' cent ' + self.translate2french(number % 100)

        elif number < 1000000:
            factor = number // 1000
            remainder = number % 1000
            if factor == 1:
                prefix = 'mille'
            else:
                prefix = self.translate2french(factor) + ' mille'
            if remainder == 0:
                return prefix
            else:
                return prefix + ' ' + self.translate2french(remainder)
            
# Quick test to see if everything works
if __name__ == "__main__":
    converter = Number2French()

    # 0 to 99
    print(converter.translate2french(0))      # zéro
    print(converter.translate2french(22))     # vingt-deux
    print(converter.translate2french(71))     # soixante-et-onze

    # 100 to 999
    print(converter.translate2french(131))    # cent-trente-et-un
    print(converter.translate2french(231))    # deux-cent-trente-et-un
    print(converter.translate2french(700))    # sept-cents

    # 1k to 9999
    print(converter.translate2french(1000))   # mille 
    print(converter.translate2french(1999))   # mille-neuf-cent-quatre-vingt-dix-neuf
    print(converter.translate2french(6000))   # six-milles
    print(converter.translate2french(9871))   # neuf-mille-huit-cent-soixante-et-onze 

    # 10k to 999999
    print(converter.translate2french(20000))  # vingt-milles 
    print(converter.translate2french(91820))  # quatre-vingt-onze-mille-huit-cents
    print(converter.translate2french(999999)) # neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf
