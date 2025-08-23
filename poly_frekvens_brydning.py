import numpy as np

encrypted_input = input('Krypteret tekst (polyalfabetisk): ')
key_length = int(input('Key længde: '))


danish_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']

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

def retrieve_substring_mono_alphabet(text, key_length, start_index):
    letter_indexes = []
    substring_mono_alpha = ''
    text = ''.join(c for c in text if c.isalpha()).upper()
    for index, letter in enumerate(text[start_index:len(text):key_length]):
        substring_mono_alpha += letter
        letter_indexes.append(start_index+index*key_length)
    return substring_mono_alpha, letter_indexes

def calculate_frequencies(text):
    frequencies = {}
    clean_text = ''.join(c for c in text if c.isalpha()).upper()
    for letter in set(clean_text):
        percentage = round(((clean_text.count(letter)/len(clean_text)) * 100),2)
        frequencies[letter] = percentage
    for i in list(frequencies_danish.keys()):
        if i not in list(frequencies.keys()):
            frequencies[i] = 0.0
    return {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}

def return_most_common(text_freq):
    return list(text_freq.items())[0][0]


def recreate_key():
    most_common_letter_shifts = []
    reconstructed_key = ''

    for start_index in range(key_length):
        substring_mono_alpha, letter_indexes = retrieve_substring_mono_alphabet(encrypted_input, key_length, start_index)
        text_frequencies = calculate_frequencies(substring_mono_alpha)
        most_common_letter  = return_most_common(text_frequencies)
        most_common_letter_shifts.append(danish_alpha.index(most_common_letter) - danish_alpha.index('E'))
        
        reconstructed_key += danish_alpha[most_common_letter_shifts[start_index]]
        print('frekvenser:',text_frequencies)
        print('Current substring:',substring_mono_alpha)
        print('Substring letter indexes in full string',letter_indexes)
        print('----------------------')
    return reconstructed_key

def decryption(key, text, alphabet):
    decrypted_text = ''

    alpha_to_cycle = alphabet

    key_repeated = key * (len(text)//len(key)+1)
    index_count = 0
    for letter in text:
        _alpha_to_cycle = list(np.roll(alpha_to_cycle,alphabet.index(key_repeated[index_count])))
        decrypted_text += _alpha_to_cycle[alphabet.index(letter)]
        index_count += 1
    return decrypted_text


reconstructed_key = recreate_key()
print(reconstructed_key)
print(decryption(reconstructed_key, encrypted_input, danish_alpha))