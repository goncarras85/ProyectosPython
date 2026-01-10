import unittest
import analizador

class TestExtra(unittest.TestCase):
    def test_recursividad_base(self):
        # Caso base 1 letra
        self.assertTrue(analizador.es_anagrama_recursivo("a", "a"))
        self.assertFalse(analizador.es_anagrama_recursivo("a", "b"))

    def test_ordenacion_manual(self):
        # Lista desordenada
        d = {"c": 1, "a": 5, "b": 3}
        esperado = [("a", 5), ("b", 3), ("c", 1)]
        self.assertEqual(analizador.ordenar_por_frecuencia(d), esperado)

    def test_cifrado_circular(self):
        # Desplazamiento mayor a 27 (vuelta completa + 1)
        self.assertEqual(analizador.aplicar_cifrado(["a"], 28), ["b"])
        # Desplazamiento negativo
        self.assertEqual(analizador.aplicar_cifrado(["b"], -1), ["a"])

if __name__ == "__main__":
    unittest.main()