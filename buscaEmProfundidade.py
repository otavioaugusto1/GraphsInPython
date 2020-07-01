#DFS

class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)] #compressão de lista
        self.visitados = [False] * vertices #Lista de tamanho 'vertices' com todosñvisitados
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
    def dfs(self, u):
        self.visitados[u-1] = True
        print("{} visitado".format(u))
        for i in range(1,self.vertices+1):
            if self.grafo[u-1][i-1] == 1 and self.visitados[i-1] == False:
                self.dfs(i)

p = Grafo(5)
p.add_aresta(1,4)
p.add_aresta(4,2)
p.add_aresta(4,5)
p.add_aresta(2,5)
p.add_aresta(5,3)
#p.show()
p.dfs(1)
