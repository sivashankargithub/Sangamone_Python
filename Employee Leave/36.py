names1=[]
country=[]
from_date=[]
to_date=[]
duration=[]
leave_type=[]

f1=open("Leave1.csv","r")
list1=f1.readlines()

len1=len(list1)
for i in range(1,len1,1):
    list2=list1[i].split(",")
    names1.append(list2[1])
    country.append(list2[3])
    from_date.append(list2[4])
    to_date.append(list2[5])
    duration.append(int(list2[6]))
    leave_type.append(list2[7].replace("\n",""))
#print(leave_type)

temp1=set(names1)
names2=list(temp1)
names2.sort()
#print(names2)
len2=len(names2)

'''for j in range(0,len2,1):
    total=0
    for i in range(0,len1-1,1):
        if names1[i]==names2[j]:
            total=total+duration[i]
            print(from_date[i],to_date[i],duration[i],leave_type[i])
    print(names2[j],"has taken a total of",total,"leaves")
    print()'''

print("-----------US Dashboard------------")
print()
names_us=[]
for i in range(0,len1-1,1):
    if country[i]=="US":
        names_us.append(names1[i])
#print(names_us)

temp1=set(names_us)
names2=list(temp1)
names2.sort()
len2=len(names2)

for j in range(0,len2,1):
    total=0
    for i in range(0,len1-1,1):
        if names1[i]==names2[j]:
            total=total+duration[i]
            print(from_date[i],to_date[i],duration[i],leave_type[i])
    print(names2[j],"has taken a total of",total,"leaves")
    print()

print("----------UK Dashboard-----------")
print()
names_uk=[]
for i in range(0,len1-1,1):
    if country[i]=="UK":
        names_uk.append(names1[i])
#print(names_uk)

temp1=set(names_uk)
names2=list(temp1)
names2.sort()
len2=len(names2)

for j in range(0,len2,1):
    total=0
    for i in range(0,len1-1,1):
        if names1[i]==names2[j]:
            total=total+duration[i]
            print(from_date[i],to_date[i],duration[i],leave_type[i])
    print(names2[j],"has taken a total of",total,"leaves")
    print()

print("-------------UAE Dashboard-------------")
print()
names_uae=[]
for i in range(0,len1-1,1):
    if country[i]=="UAE":
        names_uae.append(names1[i])
#print(names_uae)

temp1=set(names_uae)
names2=list(temp1)
names2.sort()
len2=len(names2)

for j in range(0,len2,1):
    total=0
    for i in range(0,len1-1,1):
        if names1[i]==names2[j]:
            total=total+duration[i]
            print(from_date[i],to_date[i],duration[i],leave_type[i])
    print(names2[j],"has taken a total of",total,"leaves")
    print()

print("-------------India Dashboard------------")
print()
names_in=[]
for i in range(0,len1-1,1):
    if country[i]=="IN":
        names_in.append(names1[i])
#print(names_in)

temp1=set(names_in)
names2=list(temp1)
names2.sort()
len2=len(names2)

for j in range(0,len2,1):
    total=0
    for i in range(0,len1-1,1):
        if names1[i]==names2[j]:
            total=total+duration[i]
            print(from_date[i],to_date[i],duration[i],leave_type[i])
    print(names2[j],"has taken a total of",total,"leaves")
    print()


