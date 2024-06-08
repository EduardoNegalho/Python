# option_entrace = 'entrar'
# password = '123456'

# password_user = '123456'

# if (option_entrace == 'entrar' and password == password_user):
#     print('Entrada confirmada!')

print('Operador "and"')
# Só é True quando todas as avaliações forem True
print(True and True)
print(True and False)
print(False and True)
print(True and 0 and 1) # operação de curto circuito


print('\nOperador "or"')
# Só é True quando pelo menos uma das avaliações forem True
print(True or True)
print(True or False)
print(False or False)
print(False or 0 or '1') # operação de curto circuito

print('\nOperador "not"')
# Usado para inverter expressões
print(not(True and True))
print(not(False or False))