from collections import defaultdict 

#Amigo do facebook
#Vértice ou pessoa
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade


#Grafo
class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def addLigacao(self,p1,p2):
        self.grafo[p1.getNome()].append(p2)
        self.grafo[p2.getNome()].append(p1)
    def show(self,nome):
        for amigo in self.grafo[nome]:
            print(amigo.getnome())
g = Grafo()
p1= Pessoa("Maria",20)
p2= Pessoa("Joao",19)
p3= Pessoa("Josue",24)
p4= Pessoa("Pietro",20)