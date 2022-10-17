from colorama import Fore
def dicc():
    dict1 = {"Penelope": 178, "Arnau": 172, "Marta": 175}
    print(Fore.YELLOW +"Imprimir las  claves" +Fore.WHITE, dict1.keys())
    print()
    print(Fore.YELLOW+"Imprimir los valores"+Fore.WHITE, dict1.values())
    print()
    print(Fore.YELLOW+"Imprimir los items"+Fore.WHITE, dict1.items())
    print()

    dict1["height"] = " "
    print(Fore.YELLOW+"Añadir una clave"+Fore.WHITE, dict1)

    print()

    del dict1["height"]
    print(Fore.YELLOW+"Eliminar una clave"+Fore.WHITE, dict1)
    print()
    word_freq = {'love': 25, 'conversation': 1, 'every': 6, "we're": 1, 'plate': 1, 'sour': 1, 'jukebox': 1, 'now': 11, 'taxi': 1, 'fast': 1, 'bag': 1, 'man': 1, 'push': 3, 'baby': 14, 'going': 1, 'you': 16, "don't": 2, 'one': 1, 'mind': 2, 'backseat': 1, 'friends': 1, 'then': 3, 'know': 2, 'take': 1, 'play': 1, 'okay': 1, 'so': 2, 'begin': 1, 'start': 2, 'over': 1, 'body': 17, 'boy': 2, 'just': 1, 'we': 7, 'are': 1, 'girl': 2, 'tell': 1, 'singing': 2, 'drinking': 1, 'put': 3, 'our': 1, 'where': 1, "i'll": 1, 'all': 1, "isn't": 1, 'make': 1, 'lover': 1, 'get': 1, 'radio': 1, 'give': 1, "i'm": 23, 'like': 10, 'can': 1, 'doing': 2, 'with': 22, 'club': 1, 'come': 37, 'it': 1, 'somebody': 2, 'handmade': 2, 'out': 1, 'new': 6, 'room': 3, 'chance': 1, 'follow': 6, 'in': 27, 'may': 2, 'brand': 6, 'that': 2,
                 'magnet': 3, 'up': 3, 'first': 1, 'and': 23, 'pull': 3, 'of': 6, 'table': 1, 'much': 2, 'last': 3, 'i': 6, 'thrifty': 1, 'grab': 2, 'was': 2, 'driver': 1, 'slow': 1, 'dance': 1, 'the': 18, 'say': 2, 'trust': 1, 'family': 1, 'week': 1, 'date': 1, 'me': 10, 'do': 3, 'waist': 2, 'smell': 3, 'day': 6, 'although': 3, 'your': 21, 'leave': 1, 'want': 2, "let's": 2, 'lead': 6, 'at': 1, 'hand': 1, 'how': 1, 'talk': 4, 'not': 2, 'eat': 1, 'falling': 3, 'about': 1, 'story': 1, 'sweet': 1, 'best': 1, 'crazy': 2, 'let': 1, 'too': 5, 'van': 1, 'shots': 1, 'go': 2, 'to': 2, 'a': 8, 'my': 33, 'is': 5, 'place': 1, 'find': 1, 'shape': 6, 'on': 40, 'kiss': 1, 'were': 3, 'night': 3, 'heart': 3, 'for': 3, 'discovering': 6, 'something': 6, 'be': 16, 'bedsheets': 3, 'fill': 2, 'hours': 2, 'stop': 1, 'bar': 1}

    

    word_freq2={}
    # ordenar de  manera ascendete las  claves del diccinario
    print(Fore.YELLOW+"Ordenar de manera ascendente las claves del diccionario:"+Fore.WHITE)
    for key in sorted(word_freq.keys()):
        word_freq2[key]=word_freq[key]
    print(word_freq2)
    print()
    word_freq2={}
    print(Fore.YELLOW+"Ordenar de manera ascendente las claves del diccionario:"+Fore.WHITE)
    # ordenar de manera ascendente los valores del diccionario con su clave y valor
    for key, value in sorted(word_freq.items(), key=lambda item: item[1]):
        word_freq2[key]=value
    print(word_freq2)






    

#diccionarios()
