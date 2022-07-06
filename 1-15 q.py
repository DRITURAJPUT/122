#1.	Python program to add two numbers
'''a1 = (input("enter 1st number"))
b2 = (input("enter 2st number"))
c = a1 + b2
print ('sum of:',c)
#or
a1 = float(input("enter 1st number"))
b2 = float(input("enter 2st number"))
c = a1 + b2
print ('sum of:',c)'''
#2.	Maximum of two numbers in Python
'''
a=6
b=9
if a>9:
    print('a is greater')
if b>a:
    print('b is greater')
else:
    print('both are wrong')
'''
#3.	Python Program for factorial of a number
'''
n=5
fact=1
i=1
while (i<=n):
    fact=fact*i
    i=i+1
    print("factorial=",fact)
    '''
#4.	Python Program for simple interest.
'''
p=float(input("enter the P amount"))
t=float(input("enter the t time"))
r=float(input("enter the r rate"))

simple_intrest=(p*t*r)/100

print ("simple_intrest is :", simple_intrest)'''


#5.	Python Program for compound interest
'''p=float(input("enter the P amount"))
t=float(input("enter the t time"))
r=float(input("enter the r rate"))

compound_intrest=p*(pow((1+r/100),t))

print ("compound_intrest is :", compound_intrest)'''
#6.	Python Program to check Armstrong Number
'''
num =153
sum = 0
i = num
while i >= 1:
   digit = i % 10
   sum =sum + digit ** 3
   i=i// 10
if num == sum:
   print(num,"is an Armstrong number")
else:   
   print(num,"is not an Armstrong number")
'''


#7.	Python Program for Program to find area of a circle


#8.	Python program to print all Prime numbers in an Interval
'''
num = int(input("enter your number"))
i=2
for i in range(2,num+1):
    if num%2 ==0:
        print (num,"is not a prime number")
    else:
        print(num,"is a prime number")

lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)

'''


#9.	Python program to check whether a number is Prime or not

lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for x in range(lower,upper+1):
    if x>1:
        for i in range(2,x):
            if (x%i)==0:
                break
        else:
            print(x)

#10.	Python Program for n-th Fibonacci number
'''
def Fibonacci(n):
   if n<0:
      print("Fibbonacci can't be computed")
   # First Fibonacci number
   elif n==1:
      return 0
   # Second Fibonacci number
   elif n==2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)
# main
n=10
print(Fibonacci(n))
'''
#11.	Python Program for How to check if a given number is Fibonacci number?
'''
n=int(input('enter number'))
x=0
y=1
z=0

while z<=n:
    x = y
    y = z
    z = x + y
    if z==n:
        print('it is Fibonacci number',z)

else:
 print('it is not Fibonacci number',z)
'''
#12.	Python Program for n\’th multiple of a number
# in Fibonacci Series
'''
def find(k, n):
   f1 = 0
   f2 = 1
   i =2;
   #fibonacci recursion
   while i!=0:
      f3 = f1 + f2;
      f1 = f2;
      f2 = f3;
      if f2%k == 0:
         return n*i
      i+=1
   return
# multiple of which number
n = 5;
# number
k = 4;
'''
print("Position of nth multiple of k in""Fibonacci Series is:"
#13.	Program to print ASCII Value of a character in python





#14.	Python Program for Sum of squares of first n natural numbers
'''
sum=0
i=1
while(i<=10):
    sum=sum+(i%10)*(i%10)
    i=i+1
print("sum of:",sum)
#15.	Python Program for cube sum of first n natural numbers
sum=0
i=1
while(i<=10):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i+1
print("sum of:",sum)
'''

# area of circle
'''
a=int(input('enter the radius'))
pie=3.14
area=pie*a*a
print ('area of circle',area)
'''
















