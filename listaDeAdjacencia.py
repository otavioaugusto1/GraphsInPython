class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(vertices)]
    def add_aresta(self,u,v):
        self.grafo[u-1].append(v-1)
    def tem_ligacao(self,u,v):
        if v in self.grafo[u]:
            return True
        return False
    def show(self):
        for i in range(self.vertices):
            print("{}:".format(i+1),end=" ")
            for j in self.grafo[i]:
                print("{} ->".format(j+1), end= " ")
            print(" ")
listaDeAd = Grafo(5)
listaDeAd.add_aresta(1,2)
listaDeAd.show()