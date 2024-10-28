from collections import namedtuple
import csv

#  Año,Nombre,Frecuencia,Género
#  2002,ALEJANDRO,8020,Hombre
#  2002,PABLO,5799,Hombre

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        lista = [FrecuenciaNombre(int(año),nombre,int(frecuencia),genero)
                 for año,nombre,frecuencia,genero in lector]
    return lista

def filtrar_por_genero(lista, genero):
    lista_genero = [registro for registro in lista if registro.genero == genero]
    return lista_genero

def calcular_nombres(lista, genero = None):
    conjunto_nombres = {registro.nombre for registro in lista if registro.genero == genero or genero==None}
    return conjunto_nombres

def calcular_top_nombres_de_año(lista, año, max=10, genero=None):
    lista = [(registro.nombre, registro.frecuencia) for registro in lista
             if genero == registro.nombre or genero == None and registro.año == año]
    lista.sort(key = lambda r:r[1], reverse=True)
    return lista[:max]

def calcular_nombres_ambos_generos(lista):
    Hombre = {registro.nombre for registro in lista if registro.genero == "Hombre"}
    Mujer = {registro.nombre for registro in lista if registro.genero == "Mujer"}
    ambos_generos = {registro.nombre for registro in lista
                     if registro.nombre in Hombre and registro.nombre in Mujer}
    return ambos_generos

def calcular_nombres_compuestos(lista, genero=None):
    conjunto = {registro.nombre for registro in lista if " " in registro.nombre}
    return conjunto
