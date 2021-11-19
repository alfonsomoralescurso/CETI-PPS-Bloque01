# test.py

a = input("operando 1: ")
b = input("operando 2: ")

a = int(a)
b = int(b)


# Ejemplo uso funciones en otro fichero/mismo dir
"""
import calculadora
print(f"suma({a},{b}) = ", calculadora.suma(a,b))
"""

# Ejemplo donde se importan las funciones concretas
"""
from calculadora import suma, resta
print(f"suma({a},{b}) = ", suma(a,b))
print(f"resta({a},{b}) = ", resta(a,b))
"""

# Ejemplo donde se importan las funciones concretas y se renombran
"""
from calculadora import suma as miSuma
print(f"miSuma({a},{b}) = ", miSuma(a,b)) 
"""

# Usando un "paquete"
""" 
import paqueteTest.calcula
print(f"resta({a},{b}) = ", paqueteTest.calcula.resta(a,b))
"""

# Usando un "paquete" e importando la función
""" 
from paqueteTest.calcula import suma
print(f"suma({a},{b}) = ", suma(a,b)) 
"""

