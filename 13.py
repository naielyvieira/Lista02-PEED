# Criar um dicionário vazio
nomes = {}

# Pedir ao usuário para digitar as chaves e valores usando o loop
while True:
    chave = input("Digite uma chave (ou digite 'sair' para encerrar): ")
    if chave == 'sair':
        break
    valor = input("Digite um valor: ")
    nomes[chave] = valor

# Verificando se a chave 'profissão' está presente no dicionário
if 'profissão' in nomes:
    print("A chave 'profissão' está presente no dicionário.\n", nomes)
else:
    print("A chave 'profissão' não está presente no dicionário.\n", nomes)
