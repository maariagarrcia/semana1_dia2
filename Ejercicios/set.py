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

     


    for i in set1:
        if i not in set2:
            set3.append(i)
    print(set3)
    set4=[]
    for i in set2:
        if i not in set1:
            set4.append(i)

    print(set4)
 
    set5=set1.intersection(set2)
    print(set5)

    print(len(set1),len(set2),len(set3),len(set4),len(set5))
    set1.symmetric_difference(set2)

    set6=set
    set3=set(set3)
    set4=set(set4)
    set5=set(set5)
    set6=set3.update(set5)
    
    print(set6)

    #Check if set1 and set6 are equal.
    if set1==set6:
        print(True)
    else:
        print(False)
    
    #Check if set1 contains set2 using the Python Set issubset method. Then check if set1 contains set3.
    if set1.issubset(set2):
        print(True)
    else:
        print(False)
    if set1.issubset(set3):
        print(True)
    else:
        print(False)

    set7=set3.union(set4,set5)
    set8=set1.union(set2)
    if set7==set8:
        print(True)
    else:
        print(False)
    
    set1.pop()
    print(set1)


    list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
    for i in list_to_remove:
        if i in set1:
            set1.remove(i)
    print(set1)


#sets()