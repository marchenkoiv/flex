import time
import flex



def inputt():
    try:
        k = int(input())
    except (TypeError, ValueError):
        print ("You entered incorrect data! Enter again!")
        k=inputt()
    return k


start_time = time.time()
f=open('result.txt', 'w')
print("Do you want to use file(1) or console(2)?")
n=inputt()
str=" "
d={}
if n==2:
    print("Enter new string or 0 to finish")
    str=input()
    while str!="0":
        t=iscorrect(str)
        if t==1:
            print(" is correct")
        else:
            print(" is incorrect")
        print("Enter new string or 0 to finish")
        str=input()
elif n==1:
    start_time = time.time()
    try:
        file= open ('C:/Users/user/source/repos/generator/generator/voc.txt', 'r')
    except IOError as e:
        print(u'file is not exist')
    else:
        while True:
            line = file.readline()
            if not line:
                break
            iscorrect(line)
        file.close()
        print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("You entered incorrect number!")
a=0
b=0
with open('functions.txt','w') as i:
    for key,val in d.items():
        i.write('{}:{}\n'.format(key,val))
        a=a+val
        b=b+1
print(b," lines were correct")
print(a," functions were correct")
f.close()