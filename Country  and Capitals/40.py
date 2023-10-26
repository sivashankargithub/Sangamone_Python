import random
randlist=[]
f1=open("Capitals.csv","r")
list1=f1.readlines()
len1=len(list1)
print(len1)
for i in range(0,10,1):
    randlist.append(random.randint(0,len1-1))
#print(randlist)
marks=[]
wrong=[]

country=[]
capital=[]
for i in range(0,len1,1):
    list2 = list1[i].split(",")
    country.append(list2[0])
    capital.append(list2[1].replace("\n",""))
#print(country)
#print(capital)
for i in range(0,10,1):
    response1=input("What is the capital of "+str(country[randlist[i]])+"?")
    if response1 == capital[randlist[i]]:
        marks.append(10)
    else:
        marks.append(0)
        wrong.append(i)
print(sum(marks))
