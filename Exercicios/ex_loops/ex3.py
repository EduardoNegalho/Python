frase = 'eduardo marques negalho'

i = 0

qtd_letra_mais_apareceu = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_letra_mais_apareceu < qtd_atual:
       qtd_letra_mais_apareceu = qtd_atual
       letra_que_apareceu_mais_vezes =  letra_atual

    i += 1

print(f'A letra que mais apareceu foi "{letra_que_apareceu_mais_vezes}", apareceu {qtd_letra_mais_apareceu}x')