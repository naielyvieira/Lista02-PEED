# Pedir para o usuario digitar 10 num, e depois remover todos os numeros pares.
numeros = []

for i in range (10):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

#criar um conjunto com os numeros

conjunto = set(numeros)

# remover os numeros pares
conjunto_sem_pares = {num for num in conjunto if num % 2 != 0}

#print conjunto sem numeros pares
print('O conjunto dos números que foram digitados sem os pares são: ',conjunto_sem_pares)
