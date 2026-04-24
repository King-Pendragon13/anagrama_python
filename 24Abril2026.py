"""Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama."""

def son_anagramas(palabra1: str, palabra2: str) -> bool:
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()
    
    if p1 == p2:
        return False
    
    return sorted(p1) == sorted(p2)


# Pedir datos al usuario
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Mostrar resultado
if son_anagramas(palabra1, palabra2):
    print("Son anagramas")
else:
    print("No son anagramas")