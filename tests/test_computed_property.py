import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from bwgi_project.core.computed_property import computed_property

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @computed_property('x', 'y', 'z')  # 'z' não existe ainda
    def magnitude(self):
        """Calcula a magnitude do vetor. Docstring de teste."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

class TestComputedProperty(unittest.TestCase):
    def test_magnitude_calculo(self):
        v = Vetor(3, 4)
        self.assertEqual(v.magnitude, 5.0)  # Deve calcular corretamente

    def test_docstring_preservada(self):
        self.assertEqual(Vetor.magnitude.__doc__, "Calcula a magnitude do vetor. Docstring de teste.")

    def test_dependencia_inexistente_ignorada(self):
        v = Vetor(3, 4)
        _ = v.magnitude  # Cacheia o valor
        v.z = 100  # Criando a dependência inexistente
        self.assertEqual(v.magnitude, 5.0)  # Não deve alterar o valor cacheado pois z não é usado no cálculo
