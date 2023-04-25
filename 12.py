# Criar uma lista vazia para armazenar os nomes
nomes = []

# Pedir ao usuário para digitar 3 nomes
for i in range(3):
    nome = input("Digite o nome {}: ".format(i+1))
    nomes.append(nome)

# Criar uma tupla com os nomes
tupla_nomes = tuple(nomes)

# Verificando se o nome 'Maria' está presente na tupla
if 'Maria' in tupla_nomes:
    print("O nome 'Maria' está presente na tupla.")
else:
    print("O nome 'Maria' não está presente na tupla.")

# para que o codigo reconheca o nome 'Maria' em letra minuscula substituir a linha 13 por if 'maria'.lower() in [nome.lower() for nome in tupla_nomes]: