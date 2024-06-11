hour = input('Digite a hora em número inteiro: ')

try:
    hour_int = int(hour)

    if (hour_int >= 0 and hour_int <= 11):
        print('Bom dia!')
    elif (hour_int <= 17):
        print('Boa tarde!')
    elif (hour_int <= 23):
        print('Boa noite!')
    else:
        print('Hora inválida!')
except:
    print('A hora precisa ser um número inteiro')