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
        for i in range(0, self.k):
            self.centroids.append(copy.deepcopy(self.elementos[rand.randint(0, len(self.elementos)-1)]))
            self.centroids[i][1] = i

    def cria_grupos(self) -> None:
        for elem in self.elementos:
            distancias: list = []
            for centroid in self.centroids:
                distancia = self.calcula_distancia(elem[0], centroid[0])
                distancias.append([distancia, elem])
            distancias.sort(key=self.retorna_distancia)
            elem[1] = distancias[0][1][1]
        
    def votacao(self, vizinhos) -> str:
        classes = {}
        for v in vizinhos:
            if v[1] in classes.keys():
                classes[v[1]] += 1
            else:
                classes[v[1]] = 1
        mais_votado = max(classes.keys(), key=(lambda i: classes[i]))
        return mais_votado

    def set_elementos(self, elementos) -> None:
        for elem in elementos:
            self.elementos.append([elem, -1])

    def prediz(self, centro_consulta) -> str:
        vizinhos = self.get_vizinhos(centro_consulta)
        classe = self.votacao(vizinhos)
        return classe
