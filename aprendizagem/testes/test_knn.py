import unittest

from knn import Knn

class KnnTestCase(unittest.TestCase):
	self.knn = Knn(3)
	self.knn.elementos = [[[0, 0, 0, 0], 0], [[0, 0, 0, 1], 1], [[0, 0, 0, 2], 2], [[0, 0, 0, 0], 0]]

    def test_inicializa_k(self):
		esperado = 3
		knn = Knn(3)
		self.assertEqual(esperado, knn.k)

    def test_calcula_distancia_pontos_sobrepostos(self):
        esperado = 0.0
        vetor_1 = [1, 1, 1, 1]
		vetor_2 = [1, 1, 1, 1]
		resposta = self.knn.calcula_distancia(vetor_1, vetor_2)
		self.assertEqual(esperado, resposta)
	
	def test_calcula_distancia_igual_um(self):
        esperado = 1.0
        vetor_1 = [2, 1, 1, 1]
		vetor_2 = [1, 1, 1, 1]
		resposta = self.knn.calcula_distancia(vetor_1, vetor_2)
		self.assertEqual(esperado, resposta)
    
    def test_retorna_distancia(self):
        esperado = 0.0
		elemento = [0.0, [1, 2, 3, 4]]
		resposta = self.knn.retorna_distancia(elemento)
		self.assertEqual(esperado, resposta)

    def test_get_vizinhos_corretos(self, centro_consulta) -> list:
        esperado = [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 1], 1]]
		resposta = self.knn.get_vizinhos([[0, 0, 0, 0], 0])
		self.assertEqual(esperado, resposta)

    def test_votacao_retorna_maximo(self):
        esperado = 0
		resposta = self.knn.votacao(self.knn.get_vizinhos([[0, 0, 0, 0], 0]))
		self.assertEqual(esperado, resposta)

    def test_treina_define_elementos(self):
        esperado = self.knn.elementos
		resposta = Knn(3).treina(self.knn.elementos)
		self.assertEqual(esperado, resposta)

    def test_prediz_valor_correto(self):
        esperado = 0
		resposta = self.knn.prediz([[0, 0, 0, 0], 0])
        self.assertEqual(esperado, resposta)

if __name__ == '__main__':
    unittest.main()