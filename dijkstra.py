#será utilizada uma heap(minHeap), pois sempre optará por o menor valor para seguir
from collections import defaultdict
import heapq

#min heap
class MinHeap:
    def __init__(self):
        self._queue = []
        self._indice = 0
    def insere(self, item, prioridade):
        heapq.heappush(self._queue, (-prioridade,self._indice,item))
        self._indice +=1
    def remover(self):
        return heapq.heappop(self._queue)[-1]
    
    def GetTamanho(self):
        return len(self._queue)

#grafo
class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
        self.vertices = {}
    
    def addAresta(self, origem,destino, valor):
        self.grafo[origem].append((destino, valor))
        self.vertices[origem] = origem
        self.vertices[destino] = destino
    
    def dijkstra(self,origem, destino):
        
        #obtenho o número de vértices
        numeroDeVertices = len(self.vertices)

        #estimativas de menor custo
        p = [None for i in range(numeroDeVertices)]

        #Estimativa de origem é 0
        p[origem]= 0

        #constrói a min heap
        minHeap = MinHeap()

        #insere a origem na min heap
        minHeap.insere(origem, 0)

        #enquanto o tamanho da fila for maior que 0
        while minHeap.GetTamanho() > 0:
            # remove da fila de prioridades
            u = minHeap.remover()

            # percorre os adjacentes de 'u'
            for arestas in self.grafo[u]:
                #obtém o vértice adjacente e o custo
                v, custo = arestas
                #relaxamento
                if p[v] is None or p[v] > p[u] + custo:
                    #atualiza a estimativa de custo
                    p[v] = p[u] + custo

                    #insere na fila de prioridades
                    minHeap.insere(v,p[v])
        #retorna o custo do menor caminho
        return p[destino]

g = Grafo()
g.addAresta(0,1,1)
g.addAresta(0,3,3)
g.addAresta(0,4,10)
g.addAresta(1,2,5)
g.addAresta(2,4,1)
g.addAresta(3,2,2)
g.addAresta(3,4,6)
print(g.dijkstra(0,4))