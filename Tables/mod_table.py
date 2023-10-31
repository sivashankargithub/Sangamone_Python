def table2(infile,outfile):
    f1=open(infile,"r")
    f2=open(outfile,"w")
    def table1(num1,num2):
        mul=0
        for j in range(num1,num2+1,1):  
            for i in range(1,11,1):
                mul=(j,i,i*j)
                print(mul)
                f2.write(str(mul))
                f2.write("\n")
            print()
            f2.write("\n")
    
    c1=f1.readline().replace("\n","")
    list1=c1.split(" ")
    start=int(list1[0])
    end=int(list1[1])
    table1(start,end)
