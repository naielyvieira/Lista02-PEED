# criar uma lista vazia e adicionar 10 números digitados pelo usuário utilizando um loop for

# Criando uma lista vazia
numeros = []

# Pedindo para o usuário digitar 10 números e adicionando-os à lista
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Imprimindo a lista de números
print("A lista de números é:", numeros)