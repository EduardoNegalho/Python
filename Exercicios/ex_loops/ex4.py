# Crie um jogo de adivinhação de palavras

import random

print('-' * 44)
print('Bem-Vindo ao Jogo de Adivinhação de Palavras')
print('-' * 44)

words = ['computador', 'garrafa', 'celular', 'livro']
words_index = random.randint(0, len(words) - 1)
word_secret = words[words_index]
correct_letter = ''

count = 1

print(f'\nA palavra secreta tem {len(word_secret)} caracteres')
print(len(word_secret) * '_')

while True:
    print(f'\nRodada: {count}')
    letter_typed = input('Digite uma letra: ')

    if len(letter_typed) > 1:
        print('Digite apenas uma letra!')
        count += 1
        continue

    if not letter_typed:
        print('Você deve digitar uma letra!')
        count += 1
        continue

    if letter_typed in  word_secret:
        correct_letter += letter_typed

    formated_letter = ''

    for letter in word_secret:
        if letter in correct_letter:
            formated_letter += letter
        else:
            formated_letter += '_'

    print(formated_letter)

    if formated_letter == word_secret:
        print('\nParabéns você ganhou!!')
        print(f'A palavra era: {word_secret}')
        break

    count += 1