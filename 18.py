# cria um dicionário vazio
dicionario = {}

# pede ao usuário para digitar as chaves e valores do dicionário
for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor {i+1}: ")
    dicionario[chave] = valor

print(dicionario)
# adicionar uma nova chave e valor ao dicionário
cidade = input("Digite a cidade em que você nasceu: ")
dicionario['cidade'] = cidade

# exibe o dicionário na tela
print("Dicionário:", dicionario)
