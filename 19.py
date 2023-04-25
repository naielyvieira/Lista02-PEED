# lista vazia
numeros = []

# digitar os numeros
for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# cria um conjunto com os números digitados
conjunto = set(numeros)

print(numeros)

# verifica quantos elementos estão no conjunto
num_elementos = len(conjunto)

# resultado
print(f"O conjunto tem {num_elementos} elementos.")
