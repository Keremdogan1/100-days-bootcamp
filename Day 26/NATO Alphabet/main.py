""" import pandas

letter_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(letter_data_frame.to_dict())

user_input = input("Write a word/sentence to convert to NATO alphabet format: ").upper()
list_of_input = [letter for letter in user_input]

phonetic_code_list = []

for letter in list_of_input:
        for (index, row) in letter_data_frame.iterrows():
            if row.letter == letter:
                phonetic_code_list.append(row.code)

print(phonetic_code_list) """

import pandas 
letter_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dic[letter] for letter in word] 
print(output_list)