print('Descubra se p número é par ou ímpar...')
try:
    number = input('Digite um número inteiro: ')
    number_int = int(number)
    
    even_or_odd = number_int % 2 == 0
    even_odd_txt = 'Ímpar'

    if even_or_odd:
        even_odd_txt = 'Par'

    print(f'O número {number_int} é: {even_odd_txt}')
except:
    print('O número precisa ser inteiro!')