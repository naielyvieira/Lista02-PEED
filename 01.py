 # Peça para o usuário digitar 5 números e crie uma lista com esses números. Em seguida, peça para o usuário digitar mais um número e adicione esse número à lista.

numeros = []

# pede ao usuário para digitar 5 números e adiciona à lista
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(numeros)

# pede ao usuário para digitar mais um número e adiciona à lista
novo_numero = int(input("Digite mais um número: "))
numeros.append(novo_numero)

print("A lista de números é:", numeros)