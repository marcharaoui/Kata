# =========================================== #
# Kata project: number2french
# convert_data script: take an int and translates it to a french in string
# Marc Haraoui - created on 05/02/2024
# =========================================== #

class Int2French:
    def __init__(self):
        # 0 to 16 have no rules and are the following
        self.units = {
            0: 'zéro', 1: 'un', 2: 'deux', 3: 'trois', 4:'quatre',
            5: 'cinq', 6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf',
            10: 'dix', 11: 'onze', 12: 'douze', 13: 'treize',
            14: 'quatorze', 15:'quinze', 16:'seize'
        }

        # The rules behind tens
        self.tens = {
            20: 'vingt', 30: 'trente', 40: 'quarante', 50: 'cinquante',
            60: 'soixante', 70: 'soixante-dix', 80: 'quatre-vingts', 90: 'quatre-vingt-dix'
        }

        # The bigger numbers
        self.big = {
            100: 'cent', 1000: 'mille'
        }

    def translate2french(self, number):
        # For numbers between 0 and 99
        if len(str(number)) < 3: 
            if number in self.units:
                return self.units[number] 
            
            elif number < 20:
                return 'dix-' + self.units[number - 10] 
            
            elif number < 70:
                # 20-69 is vingt to soixante-neuf
                base = number - number % 10
                if number % 10 == 0:
                    return self.tens[base]
                else: 
                    return self.tens[base] + '-et-' + self.units[number % 10] if number % 10 == 1 else self.tens[base] + '-' + self.units[number % 10]
            
            elif number < 80:
                # 70-79 is soixante-dix to soixante-dix-neuf
                return 'soixante-et-' + self.translate2french(number - 60) if number % 10 == 1 else 'soixante-' + self.translate2french(number - 60)
            else:
                # 80-89 is quatre-vingt to quatre-vingt-neuf (note: 80 is 'quatre-vingts', but we handle 80 directly above)
                if number == 80: return 'quatre-vingts'
                return 'quatre-vingt-' + self.translate2french(number - 80) 
        
        # For numbers between 100 and 999
        elif len(str(number)) == 3 : 
            if number in self.big:
                return self.big[number] 
            elif str(number)[0] == '1':
                return 'cent-' + self.translate2french(number - 100)
            else:
                first_value = int(str(number)[0])
                return self.units[first_value] + '-cents' if number % 100 == 0 else self.units[first_value] + '-cent-' + self.translate2french(number - first_value*100)
            
        # for bigger numbers
        else:
            if number in self.big:
                return self.big[number] 
            pass


# Quick test to see if everything works
if __name__ == "__main__":
    converter = Int2French()
    print(converter.translate2french(0))     # zéro
    print(converter.translate2french(22))    # vingt-deux
    print(converter.translate2french(71))    # soixante-et-onze
    print(converter.translate2french(131))   # cent-trente-et-un
    print(converter.translate2french(231))   # deux-cent-trente-et-un
    print(converter.translate2french(700))   # sept-cents
    print(converter.translate2french(1001))  # mille 
