from Ejercicios import dicc
from Ejercicios import sts
from Ejercicios import tups

import helpers
from colorama import Fore
import menu
def mostrar_resultado(descripcion, resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW,resultado, Fore.WHITE)

def diccs():
    mostrar_resultado("Diccinario:",dicc())
    
def sets():
    mostrar_resultado("Sets:",sts())

def tuplas():
    mostrar_resultado("Tuplas:",tups())

def inicio():
    finalizar= False
    helpers.clear() #Limpia la terminal

    while (not finalizar):
        opcion = menu.menu()
        if opcion==1:
            tups()

        elif opcion==2:
            sets()

        elif opcion==3:
            diccs()

    print(Fore.GREEN  + "Nos vemos otro dia :)")
    print(Fore.WHITE)



inicio()