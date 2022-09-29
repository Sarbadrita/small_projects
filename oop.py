#oop class and object concept
"""class computer:          #class created
    def work(self):         # method or funtion declared (self is here to pass object)
        print("hello")
ram = computer()            # We always need someone or a person or object to perform funtion hence object created "ram"
                            #of class computer

computer.work(ram)          # here ram is commanded to perform work funtion of computer class
ram.work()                  #prev line of code can also be written as this"""

#inner class __incomplete __(passing parameter in inner class)
"""class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self,brand,p):
            self.brand=brand
            self.p=p
        def show(self):
            print(self.brand,self.p)

s1=student('roop',2)

s1.show()
s2 = s1.laptop('hp', 'i8')"""

#inheritence & constructor
"""class A:
    def __init__(self):
        print('hello1')
    def feature1(self):
        print('feature1')
class B(A):
    def __init__(self):
        print('hello2')
    def feature2(self):
        print('feature2')

a1=B()                           #so by calling object of B we get the output of constructor in B not the one in A"""


# multiple inheritance and constructor
"""
class A:
    def __init__(self):
        print('hello1')
    def feature1(self):
        print('feature1')
class B:
    def __init__(self):
        print('hello2')
    def feature2(self):
        print('feature2')
class C(A,B):
    def __init__(self):
        print('hello3')
        super().__init__()           #using super().__init__() to get the output of super class also but now C has two
                                     # classes lets see which one is considerd by super()
    def feature2(self):
        print('feature3')

a1=C()                               #output is hello3 & hello1 hence its biased it considers the left most class
                                     # imported """


# operator overloadind (used to extend the capability of operator  as here we are adding object's properties
"""class Employee:
    def __init__(self,value,val1):
        self.value=value
        self.val1=val1

    def __add__(self, other):
        return self.value+other.value

emp1=Employee(12,34)
emp2=Employee(10,30)
print(emp1+emp2)"""

# advanced example of operator overloading (for explanation refer green spiral copy)
"""class Employee:
    def __init__(self,value,val1):
        self.value=value
        self.val1=val1

    def __add__(self, other):
        a= self.value+other.value
        b= self.val1+other.val1
        emp3=Employee(a,b)
        return emp3
emp1=Employee(12,34)
emp2=Employee(10,30)
emp3=emp1+emp2
print(emp3.val1)"""

# method overloading in python artificially
"""class B:

    def plus(self,a=None,b=None,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s
s1=B()
print(s1.plus(3))"""

# make your own iterator
"""class topTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
      if(self.num<=10):
         x=self.num
         self.num=self.num+2
         return x
      else:
          raise StopAsyncIteration

val=topTen()
for i in val:
    print(i)"""

# practice codechef
"""print('hello my life is fucked up')
x=int(input())
l=[]
c=0
for i in range(0,x):
    y=int(input())
    l.append(y)

for i in l:
    p=str(i)
    for k in p:
          if(k=='4'):
             c=c+1
    if(c>=1):
        print(c)
        c=0
    else:
        print(0)
        c=0"""
#2
"""print('hello to my fooked up life')
print('enter the length')
l=[]
x=int(input())
for i in range(0, x):
    y = int(input())
    l.append(y)
for j in l:
    for i in range(2,j-1):
        if(j%i==0):
            k=int(j/i)
            print(i,'',k)
            break
        else:
            print(1,'',j)
            break"""
#contest
"""x = int(input())
n = list(map(int, input().split()))
q = int(input())
temp=0
temp2=0
flag=0
for p in range(0, q):
    num2 = list(map(int, input().split()))
    flag=0
    temp=0
    for k in range(0,len(n),1):
        i = num2[0]
        j = num2[1]
        if (n[k] == i):
            temp = k
        if(flag!=1):
           if (n[k] == j):
              temp2 = k
              flag=1
    if(temp!=0 and flag==1):
       print(temp-temp2)
    else:
        print(-1)
#10
#2 1 3 3 2 1 3 1 2 1"""
#practice
"""x=int(input())
for i in range(0,x):
    n=list(map(int, input().split()))
    flag1=0
    flag2=0
    for j in range(0,len(n)):
        for k in range(0,len(n)):
            if(n[j]==n[k] and flag1==0 and j!=k):
                n[j]='*'
                n[k]='k'
                flag1=1

            if(n[j]==n[k]  and j!=k):
                flag2=1
    if(flag1==1 and flag2==1):
        print('YES')
    else:
        print('NO')"""

"""x = int(input())
i = 1
c = 0
for j in range(1, x):
    y = int(input())
    while True:
        if (y % 10 == 0 and i == 1):
            print(0)
            break
        i = i + 1
        if (y % 5 == 0 and y % 10 != 0):
            y = y * 2
            print(1)
            break
        if (y % 5 != 0 and y % 10 != 0):
            print(-1)
            break"""
#decorators          \\add features in the original function
"""def div(a,b):
    print(a/b)

def smart_div(func,a,b):        #taking function as a parameter ..ie div()
      if a < b:
          a, b = b, a
      return func(a, b)       # this is basically return "div(a,b)"


smart_div(div,2,4)  """

# \\\\\\\\\\\\\\\\\\\\\\decorators 2nd way\\\\\\\\\\\\\\\\\\\\\\\\\\
"""def div(a,b):
    print(a/b)

def smart_div(func):      
  def inner(a,b):
      if a < b:
          a, b = b, a
      return func(a, b)       
  return inner



div1=smart_div(div)   # a function can be stored in a variable ...which also works as the new function here div is 
                      # is binded (term from js) to div1 as we are storing ""smart_div with div"" in div1
div1(2,4)"""
# iterator
"""class A:
    def __init__(self):
        self.num=1
    def hello(self):               #creating next method in a normal method 
        val=self.num
        self.num= self.num+1 
        return val
a=A()
for i in range(0,10):
    print(a.hello())               # creating iter in normal method is not appropriate because... 
                                   # inn this way we need to call this a.hello() as many times we need 
                                # so to get a iterable object so that we can apply for loop on the object to access all
                                 # its elements we need to use __next__& __iter__"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\ right way\\\\\\\\\\\\\\\\\\\\\\\\\\
"""class A:
     def __init__(self):
         self.num=1
     def __iter__(self):          # makes the object iterable when we create a obj of A it will be iterable
         return self               # if we dont create iter it doesnt makes the object of class iterable
     def __next__(self):            # it gives TypeError: 'A' object is not iterable
         val=self.num
         self.num=self.num+1
         return val

values=A()
c=0
for i in values:
    print(i)
    c = c + 1
    if c==10:
        break

# __iter__,__next__ are used as these as these are called as soon as object is created
# iter makes the object iterable when object is used in for loop as (for i on obj)
  #it will keep on calling the __next__ method until and unless we want to break it
"""
#generator
"""def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq           #yield does the work of next() and iter() it returns all the values once stored in sq #
        n = n + 1                   # in iterable form

for i in topten():
    print(i)"""


