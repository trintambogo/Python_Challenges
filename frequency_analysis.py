from collections import Counter

print('Welcome to the Frequency Analysis App')

phrase = input('\nEnter a word or phrase to count the occurrence of each letter: ').lower()

word = []
for letter in phrase:
    if letter in 'abcdefghijklmnopqrstuvwxyz':
        word.append(letter)
        
new_phrase = ''.join(word)

occurences = {}

for key,value in Counter(new_phrase).items():
   
        occurences[key] = value

print('\nHere is the frequency analysis from key phrase: ')

sorted_dict = dict(sorted(occurences.items()))

for key,value in sorted_dict.items():
     print(f'{key}\t{value}\t  {round((value/sum(sorted_dict.values()))*100,2)}%') 
        
print(f'\nLetters ordered from highest occurrence to lowest: ')

