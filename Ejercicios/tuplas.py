def tups():
    tup=("I",)
    print (tup)
    print(type(tup))
    print("Para añadir elementos a un tupla se debe crear una lista y despues convertirla en tupla")
    lista=list(tup)
    lista.append("r") 
    lista.append("o")
    lista.append( "n")
    lista.append( "h")
    lista.append( "a")
    lista.append( "c")
    lista.append( "k")
    tup=tuple(lista)
    print(tup)
    tupla1=tup[0:4]
    print(tupla1)
    tupla2=tup[4:8]
    print(tupla2)

    tup3=tupla1+tupla2
    print(tup3)
    if tup==tup3:
        print( True)

    contar1=len(tupla1)
    contar2=len(tupla2)
    print(contar1)
    print(contar2)
    print(contar1+contar2)
    if contar1+contar2==len(tup):
        print( True)

    print(tup3.index("h"))

    letras = ["a", "b", "c", "d", "e"]
    for letra in letras:
        if letra in tup3:
            print(letra,True)
        else:
            print(letra,False)
    print()
    # cuantas veces aparece cada letra en tup3
    for letra in letras:
        print(letra,tup3.count(letra))
        
    


#tuplas()