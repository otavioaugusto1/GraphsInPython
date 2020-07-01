#Gerador de grafos completos

class Grafos:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        self.gerarGrafo()
    def gerarGrafo(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j:
                    self.grafo[i].append(j)
    def show(self):
        for i in range(self.vertices):
            print("{}:".format(i),end=" ")
            for j in self.grafo[i]:
                print(j,end=" ")
            print(" ")
grafoCompleto = Grafos(5)
grafoCompleto.show()
                
