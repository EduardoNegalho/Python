# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

try:
    # tenta executar
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")

except ZeroDivisionError:
    # executa caso ocorra um erro no try
    print("Erro: Não é possível dividir por zero.")
