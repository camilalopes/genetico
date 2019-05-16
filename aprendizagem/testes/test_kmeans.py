import unittest

from kmeans import Kmeans

class KmeansTestCase(unittest.TestCase):
	self.kmeans = Kmeans(2)
	self.kmeans.elementos = [[[0, 0, 0, 0], 0], [[0, 0, 0, 1], 1], [[0, 0, 0, 2], 2], [[0, 0, 0, 0], 0]]

    def test_inicializa_k(self):
		esperado = 3
		kmeans = Kmeans(3)
		self.assertEqual(esperado, kmeans.k)

    def test_calcula_distancia_pontos_sobrepostos(self):
        esperado = 0.0
        vetor_1 = [1, 1, 1, 1]
		vetor_2 = [1, 1, 1, 1]
		resposta = self.kmeans.calcula_distancia(vetor_1, vetor_2)
		self.assertEqual(esperado, resposta)
	
	def test_calcula_distancia_igual_um(self):
        esperado = 1.0
        vetor_1 = [2, 1, 1, 1]
		vetor_2 = [1, 1, 1, 1]
		resposta = self.kmeans.calcula_distancia(vetor_1, vetor_2)
		self.assertEqual(esperado, resposta)
    
    def test_retorna_distancia(self):
        esperado = 0.0
		elemento = [0.0, [1, 2, 3, 4]]
		resposta = self.kmeans.retorna_distancia(elemento)
		self.assertEqual(esperado, resposta)

    def test_set_elementos(self):
        esperado = self.kmeans.elementos
		resposta = Kmeans(3).set_elementos(self.kmeans.elementos)
		self.assertEqual(esperado, resposta)

    def test_prediz_valor_correto(self):
        esperado = 0
		resposta = self.kmeans.prediz([[0, 0, 0, 0], 0])
        self.assertEqual(esperado, resposta)

if __name__ == '__main__':
    unittest.main()