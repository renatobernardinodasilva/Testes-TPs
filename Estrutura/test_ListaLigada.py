import unittest
from ListaLigada import ListaLigada, ListaOrdenada

class TestListaLigada(unittest.TestCase):
    def setUp(self):
        self.lista = ListaLigada()

    def test_inserirFim(self):
        self.lista.inserirFim(1)
        self.lista.inserirFim(2)
        self.assertEqual(self.lista.inicio.numero, 1)
        self.assertEqual(self.lista.inicio.proximo.numero, 2)

    def test_inserirInicio(self):
        self.lista.inserirInicio(1)
        self.lista.inserirInicio(2)
        self.assertEqual(self.lista.inicio.numero, 2)
        self.assertEqual(self.lista.inicio.proximo.numero, 1)

    def test_inserir_apos(self):
        self.lista.inserirFim(1)
        self.lista.inserirFim(3)
        self.lista.inserir_apos(1, 2)
        self.assertEqual(self.lista.inicio.proximo.numero, 2)

    def test_delete_no(self):
        self.lista.inserirFim(1)
        self.lista.inserirFim(2)
        self.lista.delete_no(1)
        self.assertEqual(self.lista.inicio.numero, 2)
        with self.assertRaises(ValueError):
            self.lista.delete_no(3)

class TestListaOrdenada(unittest.TestCase):
    def setUp(self):
        self.lista = ListaOrdenada()

    def test_inserir(self):
        self.lista.inserir(3)
        self.lista.inserir(1)
        self.lista.inserir(2)
        self.assertEqual(self.lista.inicio.numero, 1)
        self.assertEqual(self.lista.inicio.proximo.numero, 2)
        self.assertEqual(self.lista.inicio.proximo.proximo.numero, 3)

if __name__ == '__main__':
    unittest.main()