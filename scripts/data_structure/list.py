'''
- Listas são usadas para armazenar 1 ou mais valores em apenas uma variável
- lista usa notação de []
- Listas são indexadas começando do indice 0
- Recomanda-se usar apenas um tipo de dado dentro da list

-> Métodos:
    - append: Adiciona um item ao final
    - insert: Adiciona um item no índece escolhido
    - pop: Remove do final ou do índece escolhido
    - del: apaga um índice ou a lista
    - clear: limpa a lista
    - extend: estende a lista
    - + : concatena listas
'''

#         0   1   2   3
store = [10, 20, 30, 40]
#        -4  -3  -2  -1 

# ACESSANDO
print(store[0])
print(store[-1])

# ADICIONANDO
store.append(50)
print(store)
store.insert(0, 5)
print(store)

# REMOVENDO
store.pop()
print(store)
del store[2]
print(store)
# store.clear()

# CONCATENANDO LISTAS
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)