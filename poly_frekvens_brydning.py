import numpy as np

print(list('gsggs'))
encrypted_input = input('Krypteret tekst (polyalfabetisk): ')
key_length = int(input('Key længde: '))




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
    index_substring_tuples = []
    #substring_mono_alpha = text[start_index:len(text):key_length]
    #for letter in substring_mono_alpha:
    #    letter_indexes.append(start_index*key_length)
    #print(letter_indexes)

    for index, letter in enumerate(text[start_index:len(text):key_length]):
        substring_mono_alpha += letter
        letter_indexes.append(start_index+index*key_length)
        index_substring_tuples.append((letter,start_index+index*key_length))
    print('Letter indexes:',letter_indexes)
    return substring_mono_alpha, letter_indexes, index_substring_tuples

def calculate_frequencies(text):
    frequencies = {}
    clean_text = ''.join(c for c in text if c.isalpha()).upper()
    for letter in set(clean_text):
        percentage = round(((clean_text.count(letter)/len(clean_text)) * 100),2)
        frequencies[letter] = percentage
    for i in list(frequencies_danish.keys()):
        if i not in list(frequencies.keys()):
            frequencies[i] = 0.0
    print('Frekvenser: ',{k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)})
    return {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}

def match_fequencies(text, text_freq, danish_freq):
    solved_text = ''

    for letter in text:            
        solved_text += list(danish_freq.keys())[list(text_freq.keys()).index(letter)]

    return solved_text

solved_complete_string = ' ' * len(encrypted_input)
#for start_index in range(len(encrypted_input)//key_length):
for start_index in range(key_length):
    print(f'{start_index} of {len(encrypted_input)-1} total')
    substring_mono_alpha, letter_indexes, index_substring_tuples = retrieve_substring_mono_alphabet(encrypted_input, key_length, start_index)
    frequencies = calculate_frequencies(substring_mono_alpha)
    solved_sub_string = match_fequencies(substring_mono_alpha, frequencies, frequencies_danish)
    print('substring',substring_mono_alpha)
    print('(de)crypted substring',solved_sub_string)
    #print(list('j'+solved_complete_string*len(encrypted_input)+'j'))
    #print(index_substring_tuples[0])

    for i in range(len(solved_sub_string)):
        #print('solved_complete indtil videre:',list(solved_complete_string)[letter_indexes[i]])
        #print('Length:',len(list(solved_complete_string)))
        #print('letter_indexes current:',letter_indexes[i])
        tmp_arr = (list(solved_complete_string))
        tmp_arr[letter_indexes[i]] = solved_sub_string[i]
        solved_complete_string = ''.join(tmp_arr)
    #print(solved_complete_string)
    print('--------------------------------------------------')
print(solved_complete_string)
#print(string[0:len(string):2])