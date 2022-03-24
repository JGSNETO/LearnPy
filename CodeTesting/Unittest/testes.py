import unittest

from atividades import comer

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudavel"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
            )
    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida= 'Pizza', eh_saudavel=False),
            'Estou comendo besteira'
        )

if __name__ == "__main__":
    unittest.main()

