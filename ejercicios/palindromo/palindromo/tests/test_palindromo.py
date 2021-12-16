# test_palindromo.py

import unittest
from palindromo import esPalindromo

class TestPalindromo(unittest.TestCase):
    def test_01_sencillo(self):
        resultado = esPalindromo("ana")
        self.assertEqual(resultado, True)    
    
    def test_02_sencillo(self):
        self.assertEqual(esPalindromo("Anis"), False)

    def test_03_MAY(self):
        self.assertTrue(esPalindromo("Ana"))

    def test_04_espacios(self):
        self.assertTrue(esPalindromo("A luna ese anula"))

    def test_05_numero(self):
        self.assertTrue(esPalindromo("1234321"))

    def test_06_vacia(self):
        self.assertFalse(esPalindromo(""))

    # prueba absurda añadida para hacer prueba coverage
    ## se puede borrar
    def test_07_torero(self):
        self.assertFalse(esPalindromo("torero"))
