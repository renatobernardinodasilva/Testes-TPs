# test_tartarugas.py

import unittest
from main import Tartaruga, Recrutamento

class TestTartaruga(unittest.TestCase):
    def test_tartaruga_qualificada(self):
        t = Tartaruga("NovaTartaruga", 15, "espada", 30)
        self.assertEqual(t.is_qualificada(), True)

    def test_tartaruga_nao_qualificada_nome(self):
        t = Tartaruga("Leonardo", 20, "espada", 50)
        self.assertEqual(t.is_qualificada(), False)

    def test_tartaruga_nao_qualificada_arma(self):
        t = Tartaruga("NovaTartaruga", 20, "katana", 50)
        self.assertEqual(t.is_qualificada(), False)

    def test_tartaruga_nao_qualificada_idade(self):
        t = Tartaruga("NovaTartaruga", 14, "espada", 50)
        self.assertEqual(t.is_qualificada(), False)

    def test_tartaruga_nao_qualificada_radiacao(self):
        t = Tartaruga("NovaTartaruga", 20, "espada", 85)
        self.assertEqual(t.is_qualificada(), False)

class TestRecrutamento(unittest.TestCase):
    def test_listar_qualificadas(self):
        r = Recrutamento()
        t1 = Tartaruga("NovaTartaruga1", 20, "espada", 50)
        t2 = Tartaruga("NovaTartaruga2", 25, "arco", 70)
        t3 = Tartaruga("Leonardo", 20, "espada", 50)
        r.adicionar_tartaruga(t1)
        r.adicionar_tartaruga(t2)
        r.adicionar_tartaruga(t3)
        qualificadas = r.listar_qualificadas()
        self.assertEqual(len(qualificadas), 2)
        self.assertIn(t1, qualificadas)
        self.assertIn(t2, qualificadas)
        self.assertNotIn(t3, qualificadas)

if __name__ == '__main__':
    unittest.main()