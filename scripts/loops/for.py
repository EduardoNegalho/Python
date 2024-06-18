'''
-> Usa o for quando sabe quantas vezes terá que executar
o bloco de código
-> Continue: pula para a próxima iteração
-> Break: sai do laço
'''

name = 'Eduardo'

for letter in name:
    print(letter)

print('*' * 10 + '\n')

for i in range(21):
    if i % 10 == 0:
        print(f'Estou pulando o {i}...')
        i += 1
        continue

    if i % 2 == 0:
        print(f'{i} é par')
    else:
        print(f'{i} é ímpar')  

    if i == 19:
        print('Encerrando o laço aqui')
        break  