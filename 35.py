import datetime as dt
f1=open("Holidays.txt","r")
temp1=f1.readlines()
len1=len(temp1)
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
list1=[]
list2=[]
list3=[]

for i in range(0,len1,1):
    temp2=temp1[i].split(",")
    list1.append(temp2)
    print(list1)
    list2.append(temp2[1].replace("\n",""))
    year1=int(list1[i][7:11])
    month1=list1[i][3:6]
    day1=int(list1[i][0:2])
    month2=months.index(month1)+1
    date1=dt.datetime(year1,month2,day1)
    list3.append(date1)
date2=dt.datetime.now()

for i in range(0,len1,1):
    if list3[i]>date2:
        print(list2[i], list3[i])
