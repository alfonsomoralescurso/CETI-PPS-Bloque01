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

    # else  absurdo añadido para hacer prueba coverage
    ## se puede borrar
    else:
        print("Cadena vacía")
        res = False

    # if  absurdo añadido para hacer prueba coverage
    ## se puede borrar
    if cadena == "torero":
        print("testing")    

    return res

## para pruebas coverage: función que no se usa..
def invierte():
    print("hola")
    x = 3 

