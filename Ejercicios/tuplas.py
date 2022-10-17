from colorama import Fore


def tups():
    print("Vamos a crear una tupla con un elemento")
    tup = ("I",)
    print(tup)
    print()
    print("Vammos a ver de que tipo es ")
    print(type(tup))
    print(Fore.YELLOW+"Para añadir elementos a un tupla se debe crear una lista y despues convertirla en tupla" + Fore.WHITE)
    lista = list(tup)
    lista.append("r")
    lista.append("o")
    lista.append("n")
    lista.append("h")
    lista.append("a")
    lista.append("c")
    lista.append("k")
    tup = tuple(lista)
    print(tup)
    print()

    print(Fore.YELLOW+"Vamos a separar la tupla en dos diferentes" + Fore.WHITE)
    tupla1 = tup[0:4]
    print(tupla1)
    tupla2 = tup[4:8]
    print(tupla2)
    print()
    print(Fore.YELLOW+"Vamos a crear una tupla nueva apartir de dos" + Fore.WHITE)
    tup3 = tupla1+tupla2
    print(tup3)
    print()

    print(Fore.YELLOW+"Vamos a comprobar si son la misma" + Fore.WHITE)
    if tup == tup3:
        print(True)
    print()
    print(Fore.YELLOW+"Vamos a comprobar que tienen el mismo numeros de elementos" + Fore.WHITE)
    contar1 = len(tupla1)
    contar2 = len(tupla2)
    print(contar1)
    print(contar2)
    print(contar1+contar2)
    if contar1+contar2 == len(tup):
        print(True)
    print()
    print(Fore.YELLOW+"Imprimir el indice  de h" + Fore.WHITE)
    print(tup3.index("h"))
    print()
    print(Fore.YELLOW+"Vamos a comparar las letrtas con las de tup3" + Fore.WHITE)
    letras = ["a", "b", "c", "d", "e"]
    for letra in letras:
        if letra in tup3:
            print(letra, True)
        else:
            print(letra, False)
    print()
    print(Fore.YELLOW+"Cuantas veces aparece cada letra en la tupla" + Fore.WHITE)
    for letra in letras:
        print(letra, tup3.count(letra))


# tuplas()
