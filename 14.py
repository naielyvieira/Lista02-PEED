numeros = set() # set() é usado para criar um conjunto, é uma coleção não ordenada de elementos únicos e imutáveis
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.add(num)
print(numeros)
if 3 in numeros:
    print("O número 3 está presente no conjunto!")
else:
    print("O número 3 não está presente no conjunto.")
