import random
from colorama import Fore
def sts():
    sample_list_1 = [random.randint(0,100) for _ in range(80)]
    print(Fore.YELLOW+"Vamos a crear un set con 80 numeros aleatorios entre 0 y 100"+Fore.WHITE,sample_list_1)

    set1=set(sample_list_1)
    print(Fore.YELLOW+"Ahora vamos a poner la longitud del set 1"+Fore.WHITE, len(set1))

    sample_list_2=[]
    for i in range(80):
        sample_list_2.append(random.randint(0,100))
    print(Fore.YELLOW+"Vamos a crear otro set con 80 numeros aleatorios entre 0 y 100 pero con una lista vacia"+Fore.WHITE,sample_list_2)

    set2=set(sample_list_2)
    print(Fore.YELLOW+"Ahora vamos a poner la longitud del set 2"+Fore.WHITE, len(set2))
    print()
    set3=[]

    
    for i in set1:
        if i not in set2:
            set3.append(i)
    print(Fore.YELLOW+"Ahora vamos a crear un set 3 con los elementos que no estan en el set 2"+Fore.WHITE, print(set3))
    print()
    set4=[]
    for i in set2:
        if i not in set1:
            set4.append(i)
    print(Fore.YELLOW+"Ahora vamos a crear un set 4 con los elementos que no estan en el set 1"+Fore.WHITE, print(set4))
    print()
    set5=set1.intersection(set2)
    print("Ahora vamos a crear un set 5 con los elementos que estan en el set 1 y en el set 2",print(set5))
    print("Vamos a primir la longitud de los sets")
    print(len(set1),len(set2),len(set3),len(set4),len(set5))
    print("Ahora vamos a crear un set 6 con los elementos que estan en el set 1 o en el set 2 pero no en ambos",set1.symmetric_difference(set2))


    set3=set(set3)
    set4=set(set4)
    set5=set(set5)
    set6=set3.update(set5)
    print("Vamos a imprimir el set 6")
    print(set6)

    #Check if set1 and set6 are equal.
    if set1==set6:
        print(True)
    else:
        print(False)
    
    print("Vamos a comprobar si el set 1 contiene el set 2 y el set 3")
    if set1.issubset(set2):
        print(True)
    else:
        print(False)

    if set1.issubset(set3):
        print(True)
    else:
        print(False)


    set7=set3.union(set4,set5)
    set8=set7.union(set1,set2)
    #Using the Python Set union method, aggregate set3, set4, and set5. Then aggregate set1 and set2





    if set7==set8:
        print(True)
    else:
        print(False)
    
    print("Eliminar el primer elemento de la lista set1")
    set1.pop()
    print(set1)


    list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
    for i in list_to_remove:
        if i in set1:
            set1.remove(i)
    print(set1)


sts()