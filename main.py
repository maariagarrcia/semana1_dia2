from Ejercicios import dicc
from Ejercicios import sets
from Ejercicios import tuplas

import helpers
from colorama import Fore
import menu
def mostrar_resultado(descripcion, resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW,resultado, Fore.WHITE)

def diccs():
    mostrar_resultado("Diccinario:",dicc())
    
def sets():
    mostrar_resultado("Sets:",sets())

def tuplas():
    mostrar_resultado("Tuplas:",tuplas())

def inicio():
    helpers.clear() #Limpia la terminal
    opcion = menu.menu()
    if opcion==1:
        tuplas()

    elif opcion==2:
        sets()
    
    elif opcion==3:
        diccs()

    print(Fore.GREEN  + "Nos vemos otro dia :)")
    print(Fore.WHITE)



inicio()