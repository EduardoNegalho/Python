first_name = input('Digite seu primeiro nome: ')
# first_name = 'eduardo'
size_name = len(first_name)

if size_name >= 3:
    if size_name <= 4:
        print('Seu nome é curto!')
    elif size_name <= 7:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Nome inválido')
