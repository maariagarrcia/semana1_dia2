import random

def sets():
    sample_list_1 = [random.randint(0,100) for _ in range(80)]
    print(sample_list_1)
    set1=set(sample_list_1)
    print(len(set1))
    sample_list_2=[]
    for i in range(80):
        sample_list_2.append(random.randint(0,100))
    print(sample_list_2)

    set2=set(sample_list_2)
    print(len(set2))
    set3=[]

    #si el elemento de set1 no esta en set2 lo añade a set3
    for i in set1:
        if i not in set2:
            set3.append(i)
    print(set3)
            

sets()