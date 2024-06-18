'''
-> O loop while é usado quando não se sabe quantas iterações 
terá que executar
-> Deve sempre controlar o while para que não gere 
um loop infinito
-> Continue: pula para a próxima iteração
-> Break: sai do laço
'''

count = 1

while count <= 100:

    if count % 10 == 0:
        print(f'Estou pulando o {count}...')
        count += 1
        continue

    if count % 2 == 0:
        print(f'{count} é par')
    else:
        print(f'{count} é ímpar')  

    if count == 99:
        print('Encerrando o laço aqui')
        break  
    
    count +=1
else:
    print('Fim do laço while')