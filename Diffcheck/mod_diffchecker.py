def diff1(fname1,fname2):
    
    f1=open(fname1,"r")
    f2=open(fname2,"r")
    list1=f1.readlines()
    list2=f2.readlines()
    list3=[]
    list4=[]
    difflines=[]
    for i in range(0,4,1):
        if list1[i]!=list2[i]:
            list3.append(list1[i].replace("\n",""))
            list4.append(list2[i].replace("\n",""))
            difflines.append(i)
    lend=len(difflines)
    for j in range(0,lend,1):
        list5=list3[j].split(" ")
        list6=list4[j].split(" ")
        len5=len(list5)
        for i in range(0,len5,1):
            word1=list5[i]
            word2=list6[i]
            if word1!=word2:
                print("line",difflines[j],"word",i,word1," - ",word2)

