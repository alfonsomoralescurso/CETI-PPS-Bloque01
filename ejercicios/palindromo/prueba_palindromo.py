# prueba_palindromo.py

from palindromo.palindromo import esPalindromo

cadena = input("Frase a evaluar: ")

if esPalindromo(cadena):
    print("Es palíndromo!!")
else:
    print("No lo es ...")

print("123", esPalindromo(123))
print("123321", esPalindromo(123321))