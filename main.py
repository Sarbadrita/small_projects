
"""def add_sub(x,y):
    if(x>y):
       c =x+y
       d =x-y
       print(c)
       print(d)
    else:
        c=x+y
        print(c)
a=int(input())
b=int(input())
add_sub(a,b)"""

#passing many parameters at a time
"""def add(l):
 c=0
 for j in l:

    c=c+j

 print(c)

lst=[]

n=int(input("enter length"))
for j in range(0,n):
    temp=int(input("enter no"))
    lst.append(temp)
add(lst)"""


"""def printReverseFloyd(n):
    curr_val = int(n * (n + 1) / 2)
    for i in range(n + 1, 1, -1):
        for j in range(i, 1, -1):
            print(curr_val, end="  ")
            curr_val -= 1

        print("")


n = int(input()
printReverseFloyd(n)"""

"""n,m=map(int,input().split())
arr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happ=0
print (sum([(i in A) - (i in B) for i in arr]))"""