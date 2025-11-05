def criar_grafo():
    matriz = []
    vertices = []
    
    return matriz, vertices

def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        
        for linha in matriz:
            linha.append(0)
        
        nova_linha = [0] * (len(matriz)+ 1)
        matriz.append(nova_linha)
        
    return matriz, vertices

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
    
    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1
        
    return matriz, vertices


def remover_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        i = vertices.index(vertice)
        for linha in matriz:
            linha.pop(i)
        matriz.pop(i)
        vertices.remove(vertice)
        
    return matriz, vertices

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0
            
    return matriz, vertices


def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        return matriz[i][j] == 1
    
    return False


def vizinhos(matriz, vertices, vertice):
    if vertice in vertices:
        i = vertices.index(vertice)
        lista_vizinhos = []
        for j in range(len(vertices)):
            if matriz[i][j] == 1:
                lista_vizinhos.append(vertices[j])
        return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}
    
    for i in vertices:
        if not nao_direcionado:
            grau_saida = sum(matriz[vertices.index(i)])
            grau_entrada = sum(matriz[j][vertices.index(i)] for j in range(len(vertices)))
                
            grau_total = grau_entrada + grau_saida
            graus[i] = {"saida": grau_saida, "entrada": grau_entrada, "total": grau_total}
        else:
            grau = sum(matriz[vertices.index(i)])
            graus[i] = grau
            
    return graus


def percurso_valido(matriz, vertices, caminho):
    for k in range(len(caminho) - 1):
        u = caminho[k]
        v = caminho[k + 1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return
    
    lista_vizinhos = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {lista_vizinhos}")

def exibir_grafo(matriz, vertices): 
    print (vertices) 
    for i in range(len(vertices)):
        print(vertices[i], matriz[i])

def main():
    matriz, vertices = criar_grafo()
    direcionado = str(input("O grafo é direcionado? (Sim/Não): "))
    
    if direcionado.lower() == "sim":
        direcionado = False
    else:
        direcionado = True

    while True:
        caso = int(input("\nEscolha a ação que deseja realizar:\n1 - Mostrar o Grafo\n2 - Inserir vértice\n3 - Inserir aresta\n4 - Remover vértice\n5 - Remover aresta\n6 - Verificar existência de aresta\n7 - Calcular grau dos vértices\n8 - Verificar percurso válido\n9 - Listar vizinhos do vértice\n0 - Sair\n"))
        match caso:
            case 1:
                exibir_grafo(matriz, vertices)
                
            case 2:
                vertice = input("\nDigite o vértice que deseja inserir: ")
                matriz, vertices = inserir_vertice(matriz, vertices, vertice)
                
            case 3:
                origem = input("\nDigite a origem da aresta: ")
                destino = input("\nDigite o destino da aresta: ")
                matriz, vertices = inserir_aresta(matriz, vertices, origem, destino, direcionado)
                
            case 4:
                vertice = input("\nDigite o vértice que deseja remover: ")
                matriz, vertices = remover_vertice(matriz, vertices, vertice)
                
            case 5:
                origem = input("\nDigite a origem da aresta que deseja remover: ")
                destino = input("\nDigite o destino da aresta que deseja remover: ")
                matriz, vertices = remover_aresta(matriz, vertices, origem, destino, direcionado )

            case 6:
                origem = input("\nDigite a origem da aresta: ")
                destino = input("\nDigite o destino da aresta: ")
                
                if existe_aresta(matriz, vertices, origem, destino):
                    print("\nA aresta existe.")
                else:
                    print("\nA aresta não existe.")
                    
            case 7:
                print(grau_vertices(matriz, vertices))
            case 8:
                caminho = str(input("\nDigite o caminho separado por vírgulas(sem espaços): ")).split(",")
                
                if percurso_valido(matriz, vertices, caminho):
                    print("\nO percurso é válido.")
                else:
                    print("\nO percurso não é válido.")  
            case 9:
                vertice = input("\nDigite o vértice que deseja listar os vizinhos: ")
                listar_vizinhos(matriz, vertices, vertice)
            case 0:
                break

            case _:
                print("\nOpção inválida.") 


if __name__ == "__main__":
    main()
