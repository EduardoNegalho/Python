print('Bem-Vindo a calculadora aritmética')
print('*' * 34 + '\n')

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operator = input('Digite o operador (+ - * /): ')

    numbers_is_valid = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)

        numbers_is_valid = True
    except:
        numbers_is_valid = None

    if numbers_is_valid is None:
        print('Um ou ambos os números digitado está inválido')
        continue

    operators_valid = '+-*/'

    if operator not in operators_valid:
        print('Operador inválido!')
        continue

    if len(operator) > 1:
        print('Digite apenas um operador')
        continue

    print('\nCalculando...')

    if operator == '+':
        print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')

    if operator == '-':
        print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')

    if operator == '*':
        print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')

    if operator == '/':
        print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')


    # 
    option = input('\nQuer continuar? [s]sim / [n]não: ').lower()

    if option == 'n':
        print('Saindo da calculadora...')
        break