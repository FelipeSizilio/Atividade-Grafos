def criar_grafo():
    
    vertices = []
    arestas = []
    
    return vertices, arestas

def inserir_vertice(vertices, vertice):

    if vertice not in vertices:
        vertices.append(vertice)
        
    return vertices

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices and destino not in vertices:
        inserir_vertice(vertices, origem)
        inserir_vertice(vertices, destino)
    arestas.append([origem, destino])
    if nao_direcionado:
        arestas.append([destino, origem])
        
    return arestas

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    
    for aresta in arestas:
        if aresta == [origem, destino]:
            arestas.remove(aresta)
            break
        
    if nao_direcionado:
        for aresta in arestas:
            if aresta == [destino, origem]:
                arestas.remove(aresta)
                break
            
    return arestas

def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
    
    for aresta in arestas.copy():
        origem, destino = aresta
        if origem == vertice or destino == vertice:
            arestas.remove(aresta)
    
    return arestas

def existe_aresta(arestas, origem, destino):
    
    for aresta in arestas:
        if aresta == [origem, destino]:
            return True
    
    return False


def vizinhos(vertices, arestas, vertice):
    vizinhos = []
    
    for aresta in arestas:
        origem, destino = aresta
        if origem == vertice:
            vizinhos.append(destino)
            
    return vizinhos

def grau_vertices(vertices, arestas):
    
    graus = {}
    
    for vertice in vertices:
        grau_entrada = 0
        grau_saida = 0
        
        for aresta in arestas:
            origem, destino = aresta
            
            if origem == vertice:
                grau_saida += 1
            if destino == vertice:
                grau_entrada += 1
                
        graus[vertice] = {
            'entrada': grau_entrada,
            'saida': grau_saida,
            'total': grau_entrada + grau_saida
        }
        
    return graus

def percurso_valido(arestas, caminho):
    
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not existe_aresta(arestas, u, v):
            return False
        
    return True


def listar_vizinhos(vertices, arestas, vertice):
    list_vizinhos = vizinhos(vertices, arestas, vertice)

    print(f"Vizinhos de {vertice}: {list_vizinhos}")


def exibir_grafo(vertices, arestas):
    
    print("Vértices do grafo:")
    for vertice in vertices:
        print(vertice)
        
    print("\nArestas do grafo:")
    for aresta in arestas:
        origem, destino = aresta
        print(f"({origem} -> {destino})")

def main():
    vertices, arestas = criar_grafo()
    direcionado = str(input("O grafo é direcionado? (Sim/Não): "))
    
    if direcionado.lower() == "sim":
        direcionado = False
    else:
        direcionado = True

    while True:
        caso = int(input("\nEscolha a ação que deseja realizar:\n1 - Mostrar o Grafo\n2 - Inserir vértice\n3 - Inserir aresta\n4 - Remover vértice\n5 - Remover aresta\n6 - Verificar existência de aresta\n7 - Calcular grau dos vértices\n8 - Verificar percurso válido\n9 - Listar vizinhos do vértice\n0 - Sair\n"))
        match caso:
            case 1:
                exibir_grafo(vertices, arestas)
                
            case 2:
                vertice = input("\nDigite o vértice que deseja inserir: ")
                vertices = inserir_vertice(vertices, vertice)

            case 3:
                origem = input("\nDigite a origem da aresta: ")
                destino = input("\nDigite o destino da aresta: ")
                arestas = inserir_aresta(vertices, arestas, origem, destino, direcionado)

            case 4:
                vertice = input("\nDigite o vértice que deseja remover: ")
                arestas = remover_vertice(vertices, arestas, vertice)

            case 5:
                origem = input("\nDigite a origem da aresta que deseja remover: ")
                destino = input("\nDigite o destino da aresta que deseja remover: ")
                arestas = remover_aresta(arestas, origem, destino, direcionado)

            case 6:
                origem = input("\nDigite a origem da aresta: ")
                destino = input("\nDigite o destino da aresta: ")

                if existe_aresta(arestas, origem, destino):
                    print("\nA aresta existe.")
                else:
                    print("\nA aresta não existe.")
                    
            case 7:
                print(grau_vertices(vertices, arestas))
            case 8:
                caminho = str(input("\nDigite o caminho separado por vírgulas(sem espaços): ")).split(",")

                if percurso_valido(arestas, caminho):
                    print("\nO percurso é válido.")
                else:
                    print("\nO percurso não é válido.")
            case 9:
                vertice = input("\nDigite o vértice que deseja listar os vizinhos: ")
                listar_vizinhos(vertices, arestas, vertice)
            case 0:
                break

            case _:
                print("\nOpção inválida.") 



if __name__ == "__main__":
    main()
