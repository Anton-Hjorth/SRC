import numpy as np
import time
set_ = input(': ')
setting = f'{set_}crypt'

danish_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']

def poly_encrypt(key, text, alphabet):
    encrypted_text = ''
    alpha_to_cycle = alphabet

    clean_text = ''.join(c for c in text if c.isalpha()).upper()

    key_repeated = key * (len(clean_text)//len(key)+1)
    index_count = 0
    for letter in clean_text:
        _alpha_to_cycle = list(np.roll(alpha_to_cycle,alphabet.index(key_repeated[index_count])))
        encrypted_text += alphabet[_alpha_to_cycle.index(letter)]
        index_count += 1
    return encrypted_text

def poly_decrypt(key, text, alphabet):
    decrypted_text = ''

    alpha_to_cycle = alphabet

    key_repeated = key * (len(text)//len(key)+1)
    index_count = 0
    for letter in text:
        _alpha_to_cycle = list(np.roll(alpha_to_cycle,alphabet.index(key_repeated[index_count])))
        decrypted_text += _alpha_to_cycle[alphabet.index(letter)]
        index_count += 1
    return decrypted_text

user_key = input('Key: ').upper()
user_text = input('Tekst: ').upper()

if setting == 'encrypt':
    print(poly_encrypt(user_key, user_text, danish_alpha))
elif setting == 'decrypt':
    print(poly_decrypt(user_key, user_text, danish_alpha))