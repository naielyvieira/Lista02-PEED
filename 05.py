# Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo

grafo = {}

# pede ao usuário para digitar os vértices e as arestas do grafo
num_vertices = int(input("Digite o número de vértices do grafo: "))
for i in range(num_vertices):
    vertice = input("Digite o nome do vértice " + str(i+1) + ": ")
    grafo[vertice] = set()

num_arestas = int(input("Digite o número de arestas do grafo: "))
for i in range(num_arestas):
    aresta = input("Digite os nomes dos dois vértices que formam a aresta " + str(i+1) + " separados por um espaço: ")
    v1, v2 = aresta.split()
    if v1 in grafo and v2 in grafo:
        grafo[v1].add(v2)
        grafo[v2].add(v1)
    else:
        print("Erro: um dos vértices não está presente no grafo.")

print("O grafo resultante é:", grafo)