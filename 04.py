# pede ao usuário para digitar 5 números e cria um conjunto com esses números
numeros = set()
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.add(numero)

print("O conjunto de números é:", numeros)

# pede ao usuário para escolher um número e o remove do conjunto
numero_remover = int(input("Digite um número para remover do conjunto: "))
if numero_remover in numeros:
    numeros.remove(numero_remover)
    print("O número", numero_remover, "foi removido do conjunto.")
    print("O conjunto de números atualizado é:", numeros)
else:
    print("O número", numero_remover, "não está presente no conjunto.")

