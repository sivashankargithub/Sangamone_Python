import mod_find1 as mf

s1="Dear $2name, please make the insurance payment"
s2=s1
list2=s2.split("$")
print(list2[1])

f1=open("list1.txt","r")
list1=f1.readline().split(", ")
print(list1)

position=mf.find1(s1)
content1=list1[position-1]
print(content1)
