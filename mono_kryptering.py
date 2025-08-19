import numpy as np
import time

setting = 'encrypt'

danish_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']

def mono_encrypt(text, alphabet):

    random_alpha_key = np.random.permutation(alphabet)
    formatted_text = (((text.replace(' ','')).replace('.','')).replace(',','')).replace('"','').upper()
    clean_text = ''.join(c for c in text if c.isalpha()).upper()
    
    encrypted_text = ''
    for letter in clean_text:
        encrypted_text += random_alpha_key[alphabet.index(letter)]
    return encrypted_text, ''.join(random_alpha_key)

def mono_decrypt(alphabet, key, text):
    decrypted_text = ''
    for letter in text:
        decrypted_text += alphabet[key.index(letter)]
    return decrypted_text

if setting == 'encrypt':
    text_to_encrypt = input('Hvad skal krypteres: ')
    encrypted_text, alpha_key = mono_encrypt(text_to_encrypt, danish_alpha)

    print('Key:')
    print(alpha_key)
    print('Tekst:')
    print(encrypted_text)

elif setting == 'decrypt':
    key = input('Key: ')
    text = input('Krypteret tekst: ')
    decrypted_text = mono_decrypt(danish_alpha, key, text)
    print('Tekst: ')
    print(decrypted_text)

