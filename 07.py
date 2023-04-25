# Pedir que o usuário digite 5 números, criar uma tupla com esses números e retornar o primeiro elemento da tupla

numeros = []

for i in range(5):
        n = (input('Digite um numero: '))
        numeros.append(n)
        numeros += n

tnumeros = tuple(numeros)

print("O primeiro número da tupla é:", tnumeros[0])
