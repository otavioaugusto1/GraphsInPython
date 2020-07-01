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

p = Grafo(3)
 # p.add_aresta(1,2)
p.show()
print(p.tem_ligacao(1,2))