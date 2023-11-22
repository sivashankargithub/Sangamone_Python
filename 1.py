list1=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
traid1=[]
traid2=[]
len1=len(list1)
len2=len(list2)
for j in range(0,len1,1):    
    p1=list1[j]**2
    for i in range(0,len2,1):    
        p2=list2[i]**2
        p3=(p1+p2)**0.5
        p33=int(p3)
        diff=p3-p33
        if diff==0:
            print("is traid")
            temp1=[list1[j],list2[i],p33]
            traid1.append(temp1)
print(traid1)

for i in range(0,len(traid1)-1,1):
    s1=traid1[i][0]+traid1[i][1]+traid1[i][2]
    s2=traid1[i+1][0]+traid1[i+1][1]+traid1[i+1][2]
    if(s1!=s2):
        traid2.append(traid1[i])
print()
print(traid2)

traid3=[]
for i in range(0,len(traid2)-2,1):
    s1=traid2[i][0]+traid1[i][1]+traid1[i][2]
    s2=traid2[i+2][0]+traid1[i+2][1]+traid1[i+2][2]
    if(s1!=s2):
        traid3.append(traid2[i])
print()
print(traid2)





