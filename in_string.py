def check_vowels():
    nombre = input("Ingrese un nombre: ")
    nombre = nombre.lower()
    vocales = ["a", "e", "i", "o", "u"]
    for vocal in vocales:
        print(f"Contiene {vocal}: {vocal in nombre}")
