import re

text = input()
pattern = r'(?P<s>[@|#])([A-Za-z]{3,})(?P=s){2}([A-Za-z]{3,})(?P=s)'

all_words = re.findall(pattern, text)
mirrored_words = {}

for match in all_words:
    first_word = match[1]
    second_word = match[2]
    if second_word == first_word[::-1]:
        mirrored_words[first_word] = second_word

if all_words:
    print(f"{len(all_words)} word pairs found!")
else:
    print("No word pairs found!")

if mirrored_words:
    print("The mirror words are:")
    print(', '.join(f"{key} <=> {value}" for key, value in mirrored_words.items()))
else:
    print('No mirror words!')
