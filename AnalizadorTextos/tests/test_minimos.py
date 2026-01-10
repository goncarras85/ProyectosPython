import unittest
# Importamos tu archivo analizador.py
import analizador

class TestMinimos(unittest.TestCase):

    def test_contar_palabras(self):
        """Prueba que el conteo de palabras totales y únicas sea correcto"""
        entrada = ["hola", "mundo", "hola", "python"]
        # Llamamos a TU función tal cual la definimos
        resultado = analizador.contar_palabras(entrada)
        # Verificamos: (4 palabras en total, 3 únicas)
        self.assertEqual(resultado, (4, 3))

    def test_calcular_frecuencia(self):
        """Prueba que el diccionario de frecuencias se genere bien"""
        entrada = ["manzana", "pera", "manzana"]
        resultado = analizador.calcular_frecuencia(entrada)
        esperado = {"manzana": 2, "pera": 1}
        self.assertEqual(resultado, esperado)

    def test_anagrama_recursivo(self):
        """Prueba la lógica de la función recursiva de anagramas"""
        self.assertTrue(analizador.es_anagrama_recursivo("amor", "roma"))
        self.assertFalse(analizador.es_anagrama_recursivo("casa", "cosa"))

    def test_cifrado_cesar(self):
        """Prueba el desplazamiento básico del cifrado"""
        # 'a' + 1 = 'b'
        self.assertEqual(analizador.aplicar_cifrado(["a"], 1), ["b"])
        # 'z' + 1 = 'a' (circularidad)
        self.assertEqual(analizador.aplicar_cifrado(["z"], 1), ["a"])

    def test_ordenar_frecuencia(self):
        """Prueba el algoritmo de ordenación manual de mayor a menor"""
        frecuencias = {"poca": 1, "mucha": 10, "media": 5}
        resultado = analizador.ordenar_por_frecuencia(frecuencias)
        # El primer elemento debe ser el de mayor frecuencia (mucha, 10)
        self.assertEqual(resultado[0], ("mucha", 10))

if __name__ == "__main__":
    unittest.main()