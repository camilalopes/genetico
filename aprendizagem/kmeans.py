import random as rand
import copy

class Kmeans():
    k = 2
    # Representação do tipo elemento, classe
    elementos: list = []
    centroids: list = []

    def __init__(self, k):
        self.k = k

    def calcula_distancia(self, vetor_1, vetor_2) -> float:
        distancia = 0.0
        for i in range(len(vetor_1)):
            distancia += (vetor_1[i] - vetor_2[i]) ** 2
        return distancia ** (1/2)
    
    def retorna_distancia(self, elemento) -> float:
        return elemento[0]

    def inicializa_centroids(self) -> None:
        self.centroids = []
        for i in range(self.k):
            self.centroids.append(copy.deepcopy(self.elementos[rand.randint(0, len(self.elementos)-1)]))
            self.centroids[i][1] = i

    def cria_grupos(self) -> None:
        for i in range(len(self.elementos)):
            distancias: list = []
            for centroid in self.centroids:
                distancia = self.calcula_distancia(self.elementos[i][0], centroid[0])
                distancias.append([distancia, centroid])
            distancias.sort(key=self.retorna_distancia)
            self.elementos[i][1] = distancias[0][1][1]
        
    def calcula_centroids(self) -> None:
        dimensao = len(self.elementos[0][0])
        soma = [[0]*dimensao]*self.k
        count = [0]*self.k
        for elem in self.elementos:
            grupo = elem[1]
            count[grupo] += 1
            for dim in range(dimensao):
                soma[grupo][dim] += elem[0][dim]
        
        for i in range(self.k):
            if count[i] == 0:
                continue
            novo_elemento = []
            for j in range(dimensao):
                novo_elemento.append(soma[i][j]/count[i])
            self.centroids[i][0] = copy.deepcopy(novo_elemento)

    def set_elementos(self, elementos) -> None:
        for elem in elementos:
            self.elementos.append([elem, -1])

    def agrupa(self, qt_iteracoes) -> list:
        self.inicializa_centroids()
        print(self.centroids)
        for _ in range(qt_iteracoes):
            self.cria_grupos()
            self.calcula_centroids()
        return self.elementos