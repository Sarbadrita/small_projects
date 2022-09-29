#----
"""def fib(n):
    a=0
    b=1
    if n<=0 :
        print("not possible")
    elif n==1 :
        print(a)
    else :
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

x=int(input("Enter the lenght"))
fib(x)"""
#factorial using recursion
"""def fact(n):
    if n==0 :
        return 1
    else :
        return n*fact(n-1)

result=fact(7)
print(result)"""

#application of lambda and filter , filter filtrates the kind of value u want, from for ex- a list
"""nums=[1,2,3,4,5,6,7,8,10]
ev=list(filter(lambda n:n%2==0,nums)) #filter format is filter(funtion,iterable)
print(ev)"""

#map changes the value of the list according to your desire
"""nums=[2,5,6,4,9]
d=list(map(lambda n:n+2,nums)) #changing each value by addind 2 to each one
print(d)"""

#decorators are used to add some specification to a funtion without changing the orignal funtion
"""def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if (a<b):
            a,b = b,a
        return func(a,b)
    return inner
div1=smart_div(div)
div1(4,5)"""
#special jon program
"""def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)

jony=fact(4)
print("jonylovz",jony+45)"""
#opening and searchin files
"""fhand = open('demo.txt')
count=0
print('\nWrite the starting word of the line you want to search\n')
var=input()
for line in fhand:
    if line.startswith(var): #can also be written as [if line.startswith('Email-'):
        print(line)"""
#searching by any word
"""fhand = open('demo.txt')
count=0
print('\nWrite any word of the line you want to search\n')
var=input()
for line in fhand:
    line= line.rstrip()
    if line.find(var)== -1:
        continue
    print(line)"""
#oop
"""class demo:
    def __init__(self,age,gen):  #passing 3 parameter in init funtion
        self.age= age            #assigning the value passed through parameter to the object
        self.gen= gen
        print("hello")
    def databio(self):
        print("->",self.age,self.gen)

f1=demo(21,"male")  # decalaring values while creating objects cz whenever we create a object it automatically calls- 
                      # the init funtion hence we need to declare the values of parameters here !
f2=demo(20,"female")

f1.databio()
f2.databio()"""


'''class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())'''

'''def Enter_choice():
    print("{:>60}".format("-->> Enter Your Choice <<--\n"))
    print(" 1. Update Name ")
    print(" 2. Update Email ")
    print(" 3. Update Phone No.")
    print(" 4. Update Address")
    print(" 5. Change Password")

    cho=input("Enter Your Choice Here")
    return cho
a= Enter_choice()
Enter_choice()
print(a)'''

f = open('STORY.TXT', 'r')
data = f.read()
c1 = 0
c2 = 0
for i in data:
        if i[0] == "a" or i[0] == "A":
                c1+=1
        elif i[0] == "m" or i[0] == "M":
                c2+= 1
print(c1)
print(c2)