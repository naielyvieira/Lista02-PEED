grafo = {}

# digitar os vértices do grafo
vertices = input("Digite os vértices do grafo separados por espaço: ").split()

# conjunto vazio para armazenar as arestas
arestas = set()

# digitar as arestas do grafo
while True:
    aresta = input("Digite uma aresta do grafo (ou digite 'fim' para encerrar): ")
    if aresta == "fim":
        break
    else:
        aresta = tuple(aresta.split())
        if len(aresta) != 2 or aresta[0] not in vertices or aresta[1] not in vertices:
            print("Aresta inválida! Digite novamente.")
        else:
            arestas.add(aresta)

# cria o grafo a partir dos vértices e arestas
for v in vertices:
    grafo[v] = set()

for u, v in arestas:
    grafo[u].add(v)
    grafo[v].add(u)

# exibe o grafo atual
print("Grafo atual:")
for v in vertices:
    print(v, ":", grafo[v])

# digitar a aresta a ser excluída
while True:
    aresta = input("Digite uma aresta a ser excluída do grafo (ou digite 'fim' para encerrar): ")
    if aresta == "fim":
        break
    else:
        aresta = tuple(aresta.split())
        if len(aresta) != 2 or aresta[0] not in vertices or aresta[1] not in vertices:
            print("Aresta inválida! Digite novamente.")
        elif aresta not in arestas:
            print("Aresta não encontrada no grafo! Digite novamente.")
        else:
            arestas.remove(aresta)
            grafo[aresta[0]].remove(aresta[1])
            grafo[aresta[1]].remove(aresta[0])
            print("Aresta removida do grafo com sucesso!")

# grafo atualizado
print("\nGrafo atualizado:")
for v in vertices:
    print(v, ":", grafo[v])
