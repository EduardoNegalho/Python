# num = 1

# while num <= 10:
#     if num % 2 == 0:
#         print(f'{num} é par')
#     else:
#         print(f'{num} é ímpar')

#     num += 1

# print('Encerrado...')

amount_lines = 5
amount_columns = 5

line = 1

while line <= amount_lines:
    column = 1

    while column <= amount_columns:
        print(f'{line=} {column=}')
        column += 1
    
    line += 1