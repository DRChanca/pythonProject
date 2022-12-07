#palindromo (que se lee igual de derecha que de izquierdas)
def palabraAlReves(x):
    return x[::-1]
def eliminar_espacios(x):
    return x.replace(" ","")
def saberSiPalindromo(x):
    aux= palabraAlReves(x)
    auxiliar= eliminar_espacios(aux)
    if(eliminar_espacios(x) == auxiliar):
        return True
    else:
        return False
print(saberSiPalindromo("san as"))