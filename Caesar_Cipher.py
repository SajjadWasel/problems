letters = 'abcdefghijklmnopqrstuvwxyz'

letter_array = []

for i in letters:
    letter_array.append(i)

left_shift = int(input())
word = input('').lower()


word_array = []

for i in word:
    word_array.append(i)

rearrange = ''



for i in word:
    if i in letters: 
        num_of_word = letter_array.index(i) - left_shift
        main_letter = letter_array[num_of_word]
        rearrange = rearrange + main_letter
    else:
        rearrange = rearrange + ' '

print(rearrange)
