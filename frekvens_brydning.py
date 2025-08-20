import numpy as np
import time

encrypted_input = input('Krypteret tekst (monoalfabetisk): ').upper()
decrypted_input = input('Klartekst (valgfrit): ').upper()

frequencies_danish = {
    'E': 16.70,
    'R': 7.61,
    'N': 7.55,
    'D': 7.24,
    'T': 7.03,
    'A': 6.01,
    'S': 5.67,
    'I': 5.55,
    'L': 4.85,
    'G': 4.56,
    'O': 4.14,
    'M': 3.40,
    'K': 3.07,
    'V': 2.88,
    'F': 2.27,
    'H': 1.88,
    'U': 1.85,
    'B': 1.41,
    'P': 1.33,
    'J': 1.11,
    'Å': 1.03,
    'Æ': 0.93,
    'Ø': 0.84,
    'Y': 0.72,
    'C': 0.29,
    'W': 0.02,
    'X': 0.02,
    'Z': 0.02,
    'Q': 0.01
}


def calculate_frequencies(text):
    frequencies = {}
    clean_text = ''.join(c for c in text if c.isalpha()).upper()
    for letter in set(clean_text):
        percentage = round(((clean_text.count(letter)/len(clean_text)) * 100),2)
        frequencies[letter] = percentage
    for i in list(frequencies_danish.keys()):
        if i not in list(frequencies.keys()):
            frequencies[i] = 0.0

    return {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)} #Måde at sorterer efter value størrelse
    

def match_fequencies(text, text_freq, danish_freq):
    #print(danish_freq)
    #print(text_freq)
    solved_text = ''
    fem_første_da = list(danish_freq.keys())[:5]
    fem_første_te = list(text_freq.keys())[:5]
    print(fem_første_te, fem_første_da)
    for letter in text:
        #solved_text += list(danish_freq.keys())[list(text_freq.keys()).index(letter)]
        if letter in fem_første_te:
            
            solved_text += fem_første_da[fem_første_te.index(letter)]
        solved_text += letter
    print(solved_text)


if decrypted_input == '':
    match_fequencies(encrypted_input, calculate_frequencies(encrypted_input), frequencies_danish)
else:
    match_fequencies(encrypted_input, calculate_frequencies(encrypted_input), calculate_frequencies(decrypted_input))