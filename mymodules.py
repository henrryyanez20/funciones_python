#!/usr/bin/env python
'''
Módulos personalizados de HY
'''

__author__ = "HY"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import random


#CANTIDAD DE LETRAS
def cantidad_letras(texto):
    return len(texto)

#LISTA ALEATORIA
def lista_aleatoria(inicio, fin, cantidad):
    '''
    Debe ingresar varores de Inicio, Fin y cantidad de elementos.
    '''
    lista = [0]  * cantidad
    for i in range(cantidad):
        lista[i] = random.randint(inicio, fin)
    return lista
#    print(aleatorios)

#ORDENAR
def ordenar(numeros):
    numeros.sort(reverse=True)

#BUSCAR
def buscar(aleatorios):
    for i, valor in enumerate(aleatorios):
        aleatorios.count(valor)

#CONTAR
def contar(aleatorios):
    for i, valor in enumerate(aleatorios):
        aleatorios.count(valor)

#PROMEDIO
numeros = []
def promedio(numeros):
    len_value = len(numeros)
    sumatoria = 0

    if len_value != 0:
        for numero in numeros:
            sumatoria += numero
        prom_valores = sumatoria / len_value
        return prom_valores
    else:
        print("[*] La lista no tiene elementos, \npor favor ingresa valores")

