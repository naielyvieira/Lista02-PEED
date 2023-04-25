numeros = []

# digitar 10 números e adiciona à lista usando o laço for
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# multiplicar cada elemento da lista por 2 e cria uma nova lista
novos_numeros = [x * 2 for x in numeros]

# exibe os resultados 
print("Números digitados:", numeros) #lista dos nnumeros digitados
print("Números multiplicados por 2:", novos_numeros) # lista dos numeros *2
