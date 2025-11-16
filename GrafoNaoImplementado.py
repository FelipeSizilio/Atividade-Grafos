def criar_grafo():
    
    grafo= {}
    return grafo

def inserir_vertice(grafo, vertice):

    for key in grafo:
        if key == vertice:
            raise Exception("Vértice já existe no grafo.")

    grafo[vertice] = []
    
    return grafo

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    
    if (origem not in grafo) or (destino not in grafo):
        raise Exception("A origem ou o destino nao existem no grafo.")
    
    for key in grafo:
        if key == origem:
            grafo[origem].append(destino)
        if nao_direcionado:
            if key == destino:
                grafo[destino].append(origem)
                
    return grafo
           
def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        return "Vértice não existe no grafo."                    

def listar_vizinhos(grafo, vertice):                              
    vizinhos = []
    for key in grafo:
        if key == vertice:
            vizinhos.append(grafo[vertice])
    
    return print(f"Vizinhos de {vertice}: {vizinhos[0]}")

def exibir_grafo(grafo):
    for key in grafo:
        print(f"\n{key}: {grafo[key]}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    
    if origem not in grafo:
        raise Exception("A origem nao existe no grafo.")
    else:
        if destino in grafo[origem]:
            grafo[origem].remove(destino)
        else: raise Exception("A aresta nao existe no grafo.")
        
    if nao_direcionado:
        if destino in grafo:
            if origem in grafo[destino]:
                grafo[destino].remove(origem)
                
    return grafo

def remover_vertice(grafo, vertice, nao_direcionado=True):
    
    if vertice not in grafo:
        raise Exception("O vértice não existe no grafo.")
    
    for key in grafo:
        if vertice in grafo[key]:
            grafo[key].remove(vertice)
            
    grafo.pop(vertice)
    print("\nVértice removido com sucesso.")
    return grafo

def existe_aresta(grafo, origem, destino):
    if origem in grafo:
        if destino in grafo[origem]:
            return True
              
    return False

def grau_vertices(grafo):
    graus = {}
    
    for v in grafo:
        graus[v] = {'in': 0, 'out': 0, 'total': 0}
        graus[v]['out'] = len(grafo[v])
        for u in grafo:
            if v in grafo[u]:
                graus[v]['in'] += 1
        graus[v]['total'] = graus[v]['in'] + graus[v]['out']
        
    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    
    for i in range(len(caminho)-1):
        origem = caminho[i]
        destino = caminho[i+1]
        if not existe_aresta(grafo, origem, destino):
            return False
    
    return True

def busca_por_largura(grafo, inicio):
    fila = []
    visitados = []
    
    fila.append(inicio)
    print(f"\nOrdem de visitação a partir do vértice {inicio}:")
    
    while fila != []:
        vertice_atual = fila.pop(0)
        print("\nBuscando vizinhos do vértice:", vertice_atual)
        
        if vertice_atual not in visitados:
            visitados.append(vertice_atual)
            vizinhos_atual = vizinhos(grafo, vertice_atual)
            
            print(f"\nVizinhos encontrados: {vizinhos_atual}")
            
            for vizinho in vizinhos_atual:
                if vizinho not in fila and vizinho not in visitados:
                    fila.append(vizinho)
                    
            print("\nFila atual:", fila)
            print("\nVértices visitados até o momento:", visitados)
                    
    return visitados

def busca_por_largura_menor_caminho(grafo, inicio, destino):
    fila=[inicio]
    visitados=[]
    
    while fila != []:
        vertice_atual = fila.pop(0)
        
        if destino in fila:
            print(f"Menor caminho encontrado de {inicio} até {destino}: {visitados + [destino]}")
            return
        
        visitados.append(vertice_atual)
        vizinhos_atual = vizinhos(grafo, vertice_atual)
        
        for vizinho in vizinhos_atual:
            if vizinho == destino:
                print(f"Menor caminho encontrado de {inicio} até {destino}: {visitados + [destino]}")
                return
            if vizinho not in fila and vizinho not in visitados:
                fila.append(vizinho)
#     1. Inserir a estrutura com vértice inicial e caminho na fila
# 2. Iniciar a lista de visitados vazia
# 3. Enquanto a fila não estiver vazia:
# a. Retirar o primeiro item da fila
# b. verificar se o vértice do item retirado é o destino
# i. Retornar o caminho caso seja
# c. Marcar vértice como visitado
# d. Obter os vizinhos do vértice
# e. Para cada vizinho:
# i. Verificar se o vizinho não está na fila
# ii. Verificar se o vizinho já não foi visitado
# iii. Caso ambos sejam falso, adicionar estrutura com
# vizinho e caminho atualizado na Fila
# 4. Retornar vazio



def main():
    grafo = criar_grafo()
    direcionado = str(input("O grafo é direcionado? (Sim/Não): "))
    
    if direcionado.lower() == "sim":
        direcionado = False
    else:
        direcionado = True

    while True:
        caso = int(input("\nEscolha a ação que deseja realizar:\n1 - Mostrar o Grafo\n2 - Inserir vértice\n3 - Inserir aresta\n4 - Remover vértice\n5 - Remover aresta\n6 - Verificar existência de aresta\n7 - Calcular grau dos vértices\n8 - Verificar percurso válido\n9 - Listar vizinhos do vértice\n10 - Busca por largura\n11 - Busca por menor caminho\n0 - Sair\n"))
        match caso:
            case 1:
                exibir_grafo(grafo)
                
            case 2:
                vertice = input("\nDigite o vértice que deseja inserir: ")
                grafo = inserir_vertice(grafo, vertice)
                
            case 3:
                origem = input("\nDigite a origem da aresta: ")
                destino = input("\nDigite o destino da aresta: ")
                grafo = inserir_aresta(grafo, origem, destino, direcionado)
                
            case 4:
                vertice = input("\nDigite o vértice que deseja remover: ")
                grafo = remover_vertice(grafo, vertice, direcionado)
                
            case 5:
                origem = input("\nDigite a origem da aresta que deseja remover: ")
                destino = input("\nDigite o destino da aresta que deseja remover: ")
                grafo = remover_aresta(grafo, origem, destino, direcionado )

            case 6:
                origem = input("\nDigite a origem da aresta: ")
                destino = input("\nDigite o destino da aresta: ")
                
                if existe_aresta(grafo, origem, destino):
                    print("\nA aresta existe.")
                else:
                    print("\nA aresta não existe.")
                    
            case 7:
                print(grau_vertices(grafo))
            case 8:
                caminho = str(input("\nDigite o caminho separado por vírgulas(sem espaços): ")).split(",")
                
                if percurso_valido(grafo, caminho):
                    print("\nO percurso é válido.")
                else:
                    print("\nO percurso não é válido.")  
            case 9:
                vertice = input("\nDigite o vértice que deseja listar os vizinhos: ")
                listar_vizinhos(grafo, vertice)
            case 10:
                inicio = input("\nDigite o vértice de início da busca por largura: ")
                busca_por_largura(grafo, inicio)
            case 11:
                inicio = input("\nDigite o vértice de início da busca pelo menor caminho: ")
                destino = input("Digite o vértice de destino da busca pelo menor caminho: ")
                busca_por_largura_menor_caminho(grafo, inicio, destino)
            case 0:
                break

            case _:
                print("\nOpção inválida.") 
        
            

if __name__ == "__main__":
    main()

