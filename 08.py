# Criar um dicionário vazio, digitar as chaves e valores desse dicionário e retornar o valor da chave 'idade'
# Criando um dicionário vazio
dicionario = {}

# Pedindo para o usuário digitar as chaves e valores do dicionário
chave1 = input("Digite a chave 1: ")
valor1 = input("Digite o valor 1: ")
dicionario[chave1] = valor1

chave2 = input("Digite a chave 2: ")
valor2 = input("Digite o valor 2: ")
dicionario[chave2] = valor2

chave3 = input("Digite a chave 3: ")
valor3 = input("Digite o valor 3: ")
dicionario[chave3] = valor3

# Retornando o valor da chave 'idade'
idade = dicionario['idade']
print("O valor da chave 'idade' é:", idade)