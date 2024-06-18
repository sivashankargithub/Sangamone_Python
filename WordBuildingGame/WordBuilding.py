import random
words=[]
temp=[]
lastchar1=""
lastChar2=""
f1=open("dictionary.txt","r")
words=[i.replace("\n","") for i in f1.readlines()]
len2=len(words)
index2=random.randrange(0,len2+1)
computerChoice=words[index2]
lastChar2=computerChoice[-1]
words.remove(computerChoice)
print("computer :", computerChoice)
while True:
    userChoice=input("user : ")
    print(lastChar2)
    if userChoice in words and userChoice.startswith(lastChar2):
        lastChar1=userChoice[-1]
        temp=list(filter(lambda x: x.startswith(lastChar1), words))
        len1=len(temp)
        index1=random.randrange(0,len1+1)
        computerChoice=temp[index1]
        lastChar2=computerChoice[-1]
        print("computer :", computerChoice)
        words.remove(userChoice)
        words.remove(computerChoice)
    else:
        print("The word is not correct")
        print("Computer Wins")
        break
