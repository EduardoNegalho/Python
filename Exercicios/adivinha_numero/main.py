import random

print('-' * 43)
print('Bem-Vindo ao jogo de Adivinhação de Números')
print('Acerte o número entre 1 e 100')
print('-' * 43)

while True:
    print('Escolha a dificuldade do jogo')
    option = input('(F)Fácil - (M)Médio - (D)Difícil: ').lower()

    if option == 'f':
        chances = 20
        break
    elif option == 'm':
        chances = 15
        break
    elif option == 'd':
        chances = 10
        break
    else:
        print('Escolha da dificuldade inválida!\n')

print(f'Você terá {chances} rodadas')

random_number = random.randint(1, 100)
count = 1

while count <= chances:
    print(f'\nRodada: {count}')
    kick = input('Digite seu chute: ')

    try:
        kick_int = int(kick)
    except:
        print('Digite um chute válido')
        continue

    if kick_int == random_number:
        print('Parabéns você acertou')
        break

    if kick_int < random_number:
        print('Chute baixo')
    else:
        print('Chute alto')
    
    if count == chances:
        print('Você perdeu!')
        break
        
    count += 1

