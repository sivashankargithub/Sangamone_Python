def shuffle1(listA):
    import random
    list1 = listA
    list2 = []
    len1 = len(list1)
    for i in range(0,len1,1):
        len1 = len(list1)
        rand1 = random.randint(0,len1-1)
        list2.append(list1[rand1])
        list1.remove(list1[rand1])
    return list2

