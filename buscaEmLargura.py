#BSF
class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)] #compressão de lista
# Na linha a cima será [0,0,0,0,0]... Pois o 'vértices' gerará uma lista de 0´s
    def add_aresta(self,u,v):
        self.grafo[u-1][v-1]= 1
        self.grafo[v-1][u-1] = 1
    def show(self):
        for i in self.grafo:
            for j in i:
                print(j,end=" ")
            print(" ")
    def tem_ligacao(self, u, v):
        if self.grafo[u-1][v-1] == 1:
            return True
        return False
    def bsf(self,v):
        #Cria a lista de vizinhos e todos falsos
        visitados = [False] * self.vertices
        # marca 'v' como visitado
        visitados[v-1] = True
        #insere na fila
        fila = [v-1]
        print('{} visitado'.format(v))
        #enquanto a fila não for vazia:
        while len(fila):
            #obtém o elemento da fila
            v = fila[0]
            # para cada vértice 'u' adjacente a 'v':
            for u in range(self.vertices):
                #verifica se existe coneção
                if self.grafo[v][u] == 1:
                    #verifica se 'u' não foi visitado:
                    if visitados[u] == False:
                        # marca 'u' como visitado
                        visitados[u] = True
                        #insere 'u' na fila:
                        fila.append(u)
                        #imprime o elemento visitado:
                        print('{} visitado'.format(u+1))
            #remove 'v' da fila
            fila.pop(0)

p = Grafo(10)
p.add_aresta(1,2)
p.add_aresta(1,3)
p.add_aresta(1,4)
p.add_aresta(2,5)
p.add_aresta(3,6)
p.add_aresta(3,7)
p.add_aresta(4,8)
p.add_aresta(5,9)
p.add_aresta(6,10)
p.bsf(1)