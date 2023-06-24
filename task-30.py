vowels = 0
consonants = 0
vowels_set = set('aeiou')
consonants_set = set('bcdfghjklmnpqrstvwxyz')

phrase = input('Введите любую фразу на английском: ')
for i in range(len(phrase)):
    if phrase[i] in vowels_set:
            vowels += 1
    if phrase[i] in consonants_set:
            consonants += 1

print(f'В строке {vowels} гласных и {consonants} согласных')