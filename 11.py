# Criar uma lista vazia
lista = []

# pedir ao usuário que digite 10 números
for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

# Retornar os elementos de índice par da lista
pares = []
for i in range(len(lista)):
    if i % 2 == 0:
        pares.append(lista[i])

# Imprimindo os elementos de índice par da lista
print("Elementos de índice par da lista:")
for elemento in pares:
    print(elemento)
#lembar que o indice é a posiçao na lista que o numero estar, e nao necessariamente ele mesmo ter o valor par, comecando a contagem do 0