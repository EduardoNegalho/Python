'''
-> Condicionais altera o fluxo do código de acordo
com o resultado de um teste lógico

-> Dois tipos de condicionais: 
    - IF, ELIF , ELSE
    - MATCH CASE
'''

num = 2

# Se a condição for TRUE executa este bloco:
if num < 10:
    print(f'{num} é menor que 10')
# Se a condição for 'IF' for FALSE e o 'ELIF' for TRUE executa este bloco:
elif num > 10:
    print(f'{num} é maior que 10')
# Se nenhuma das condições forem TRUE executa o ELSE
else:
    print(f'{num} é igual a 10')


'''
Match case avalia uma condições e executa o bloco correspondente 
'''
day_of_week = 5

match day_of_week:
    case 1:
        print('Segunda-Feira')
    case 2:
        print('Terça-Feira')
    case 3:
        print('Quarta-Feira')
    case 4:
        print('Quinta-Feira')
    case 5:
        print('Sexta-Feira')
    case 6:
        print('Sábado')
    case 7:
        print('Domingo')
    case _:
        print('Número inválido')