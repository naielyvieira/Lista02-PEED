# criar tupla vazia
nomes = ()

# digitar 3 nomes e adiciona à tupla usando o laço for
for i in range(3):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes = nomes + (nome,)

# verifica quantas vezes o nome 'Maria' aparece na tupla
qtd_maria = nomes.count('Maria') + nomes.count('maria')
# usar .count() para contar dentro do loop, tanto em letra minuscula quanto maiuscula

# resultado 
print("Tupla de nomes:", nomes)
print("Quantidade de vezes que 'Maria' aparece na tupla:", qtd_maria)
