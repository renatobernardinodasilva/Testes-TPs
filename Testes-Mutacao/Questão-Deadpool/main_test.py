import math
import unittest

def dividir_altura(altura, cortes):
    partes = cortes + 1
    resultado = altura / partes
    return math.ceil(resultado)

class TestDividirAltura(unittest.TestCase):

    def test_dividir_altura(self):
        self.assertEqual(dividir_altura(1.60, 2), 1)
        self.assertEqual(dividir_altura(1.80, 2), 1)
        self.assertEqual(dividir_altura(2.00, 3), 1)
        self.assertEqual(dividir_altura(1.65, 1), 1)

if __name__ == '__main__':
    unittest.main()