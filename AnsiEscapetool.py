#ANSI Escape sequences verwijder tool in Python
#Gemaakt door: Jens van den Hurk
#Datum: 17-03-2026

import re

def ANSI_EXTRACT(text):
    # Stap 1: converteer \033 naar echte escape characters
    text = text.replace("\\033", "\x1b")

    # Stap 2: verwijder alle ANSI escape sequences
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

text = input("Voer je tekst in met ANSI escape sequences:\n").strip() # strip() verwijdert eventuele extra spaties aan het begin of einde van de invoer

result = ANSI_EXTRACT(text)

print("\nDe tekst zonder ANSI escape sequences is:\n")
print(result)

if text == result:
    print("\nEr zijn geen ANSI escape sequences gevonden in de tekst.")