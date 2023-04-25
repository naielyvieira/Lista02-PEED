# Criar tupla com 3 nomes e depois substituir um deles
nomes = ()

# pede ao usuário para digitar 3 nomes e cria uma tupla com esses nomes
for i in range(3):
    nome = input("Digite um nome: ")
    nomes += (nome,)

# pede ao usuário para escolher um dos nomes e substituí-lo por outro nome
nome_antigo = input("Escolha um dos nomes digitados: ")
nome_novo = input("Digite o novo nome: ")
indice = nomes.index(nome_antigo)
nova_tupla = nomes[:indice] + (nome_novo,) + nomes[indice+1:]

print("A nova tupla de nomes é:", nova_tupla)