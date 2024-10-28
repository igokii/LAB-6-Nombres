from nombres import *

def test_leenombres(ruta):
    lista = leer_frecuencias_nombres(ruta)
    print("TEST de la función 'leer_frecuencias_nombres'\n")
    print(f"leídos {len(lista)} registros.")
    print("///Mostrando los 3 primeros:")
    print(lista[:3], '\n')
    print("///Mostrando los 3 últimos:")
    print(lista[-3:], '\n')
def test_filtrarporgenero(lista):
    print("TEST de la función 'filtrar_por_genero'\n")
    print(f"    - Número de registros para Hombre: {len(filtrar_por_genero(lista, "Hombre"))}")
    print(f"    - Número de registros para Mujer: {len(filtrar_por_genero(lista, "Mujer"))}")
def test_calcularnombres(lista):
    print("TEST de 'calcular_nombres'")
    ambos = sorted(list(calcular_nombres(lista)))
    mujer = sorted(list(calcular_nombres(lista, 'Mujer')))
    hombre = sorted(list(calcular_nombres(lista, 'Hombre')))
    print(f"    - Ambos géneros (total: {len(ambos)}): {ambos[:8]}")
    print(f"    - Mujeres (total: {len(mujer)}): {mujer[:8]}")
    print(f"    - Hombres (total: {len(hombre)}): {hombre[:8]}")
def test_calculartopnombresdeaño(lista):
    pass
def test_calcularnombresambosgeneros(lista):
    print("TEST de 'calcular_nombres_ambos_generos':")
    lista = sorted(list(calcular_nombres_ambos_generos(lista)))
    print(f"Primeros nombres comunes (de {len(lista)}): {lista[:10]}")
def test_calcularnombrescompuesto(lista):
    print("TEST de 'calcular_nombres_compuestos':")
    lista = sorted(list(calcular_nombres(lista)))
    print(f"Primeros nombres compuestos (de {len(lista)}): {lista[:10]}")

ruta = "data/frecuencias_nombres.csv"
lista = leer_frecuencias_nombres(ruta)

test_leenombres(ruta)
print("\n####################################################### \n")
test_filtrarporgenero(lista)
print("\n####################################################### \n")
test_calcularnombres(lista)
print("\n####################################################### \n")
test_calculartopnombresdeaño(lista)
print("\n####################################################### \n")
test_calcularnombresambosgeneros(lista)
print("\n####################################################### \n")
test_calcularnombrescompuesto(lista)