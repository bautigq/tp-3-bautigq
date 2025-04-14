def verificar_vocales(nombre):
  nombre = nombre.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
        contiene = vocal in nombre
        print(f"Contiene {vocal}: {contiene}")
nombre_ingresado = input("Ingresa un nombre: ")
verificar_vocales(nombre_ingresado)
