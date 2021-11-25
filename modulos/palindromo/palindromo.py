# palindromo.py

def esPalindromo(cadena):
    res = False
    if cadena:
        cadena = str(cadena)
        ## tener en cuenta mayúsculas
        cadena = cadena.lower()
        ## tener en cuenta espacios en blanco
        cadena = cadena.replace(" ", "")

        inv = cadena[::-1]
        if cadena == inv:
            res = True
    
    if cadena == "torero":
        print("testing")    
    return res

def testing():
    print("hola")
    x = 3

