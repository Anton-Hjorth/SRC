import numpy as np
from frekvens_brydning import calculate_frequencies


encrypted_input = input('Krypteret tekst (polyalfabetisk: )')
key_length = input('Key længde: ')


def retrieve_substring_mono_alphabet(text, key_length):
    substring_mono_alpha = ''