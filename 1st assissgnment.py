#1.	Write a program to check whether a person is eligible for voting or not. (Accept age from user)
'''
age=int(input('enter your num'))
if age>=18:
    print('he eligible for voting')
else:
    print('he is not eligible')
'''

#2.	Write a program to check whether a number entered by user is even or odd
'''
n=int(input('enter your num'))
if n%2==0:
    print('num is even')
else:
    print('the provided num is odd')

'''
#3.	Write a program to check whether a number is divisible by 7 or not
'''
n=int(input('enter your num'))
if n%7==0:
    print('num is divided by 7')
else:
    print('num is not divided by 7')
'''


#4.	Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
'''
n=int(input('enter your num'))
if n %5==0:
    print('hello')
else:
    print('bye')
'''

#5.	Write a program to accept percentage from the user and display the grade according to the following criteria:
'''
n=int(input('enter your num'))
if n>=80:
    print('a grade')
if n>=60:
    print('b grade')
elif n>=40:
    print('c grade')
else:
    print('fail')
'''
#6.	Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.
'''
day=int(input('enter the name 1-7'))
if day==1:
    print(day,"is sunday")
elif day==2:
    print(day,"is monday")
elif day==3:
    print(day,"is Tuesday")
elif day==4:
    print(day,"is wednesday")
elif day==5:
    print(day,"is Thursday")
elif day==6:
    print(day,"is friday")
elif day==7:
    print(day,"is saturday")
    '''

#8.	Write a program to check whether a number (accepted from user) is positive or negative
'''
n=int(input('enter your number'))
if n>0:
    print('num is positive')
elif n==0:
    print('num is zero or negative')
else:
    print('num s negative')
'''
#9.	Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
'''
n=int(input('enter your number'))
if n%2==0:
    if n%3==0:
     print('num is divided by 2 and divided by 3')
elif n%3==0:
         print("num is divided by 3 and not by 2")
elif n%2==0:
        print("num is divided by 2")
else:
       print('not divided by 2 or not by 3')
'''

#10.	Write a program to find the largest number out of three numbers excepted from user
'''
num1= float(input('enter your num'))
num2= float(input('enter your num'))
num3= float(input('enter your num'))
if num1>num2 and num1>num3:
    largest = num1
if num2>num1 and num2>num3:
    largest = num2
else:
    largest = 3
    print('The largest num is:',largest)
 
num1=4
num2= 6
num3=9

if num1>num2 and num1>num3:
    print('The largest num is:',num1)
if num2>num1 and num2>num3:
    print('The largest num is:', num2)
else:
    print('The largest num is:',num3)
'''
#11.	Accept the age of 4 people and display the oldest one.
'''
age1=12
age2=24
age3=56
age4=60
if age1>age2 and age1>age3 and age1>age4:
    oldest = age1
elif age2>age1 and age2>age3 and age2>age4:
    oldest = age2
elif age3> age1 and age3 > age2 and age3 > age4:
     oldest = age3
elif age4 > age1 and age4 > age3 and age4 > age2:
     oldest = age4
     print("The oldest age:",oldest )
'''
#12.	Create simple calculator Add, Sub, Mul, dev takes two numbers from user.
'''
a=4
d=5
c=a+d
print(c)
a=4
d=5
c=a*d
print(c)

a=4
d=5
c=a%d
print(c)

a=4
d=5
c=a-d
print(c)

def add(a,b):
    total=a+b
    return total
def sub(a,b):
    sub=a-b
    return sub
print(add(2,7))
print(sub(3,6))
'''

#13.	Write a Python program to count the number of even and odd numbers from a series of numbers
'''
num=[1,2,3,4,5,6,7,8,9]
count_odd=0
count_even=0
for x in num:
      if x%2==0:
            count_even+=1
      else:
           count_odd+=1
print('num of even num:',count_even)
print('num of even num:',count_odd)


num=(1,2,3,4,5,6,7,8,9)
odd_list =[]
even_list =[]
for i in num:
    if i%2==0:
        even_list.append(i)
else:
      odd_list.append(i)
print("num of even num:",(even_list))
print("num of even num:", (odd_list))
'''
#14.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
for i in range(6):
     if i==3:
      continue
     print(i)
'''


#15.	Write a program in Python to display the Factorial of a number.
'''
num=int(input("enter your num"))
fact=1
for i in range( 1,num+1):
        fact =fact*i
print("the fact is:",fact)

num=int(input("enter your num"))
fact=1
i=1
while i<=num:
    fact=fact*i
    print("fact nunm is:",fact)
    i=i+1

import math
def factorial(x):
    return math.factorial(x)
print(factorial(5))
'''

#16.	Write a program in Python to reverse a word.
'''
a='loveisblind'
str=""
x=len(a)
y=0

while y<x:
    str+=a[x-1]
    x=x-1
print(str)
'''

#list reverse
'''
a=[1,2,4,6]
list=[]
x=len(a)
y=0

while x>y:
    list.append(a[x-1])
    x=x-1
print(list)
'''




#17.	Write a Python program to reverse a number.
'''
num=1233
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print('reverse num is:',rev)

num=1233
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print('sum num is:',sum)
'''
#18.	Write a program to print n natural number in descending order using a while loop
'''
i=10
while i>=1:
    print('natural num is:',i)
    i=i-1

i=1
while i<=10:
    print('natural num is:',i)
    i=i+1
'''




#19.	Write a python program to print the square of all numbers from 0 to10
'''
num=10
i=1
while i<=num:
    print(i**2)
    i=i+1
    
    
for i in range(1,num+1):
    print(i**2)

def square(i):
    return i**2
print(square(6))
print(square(5))
print(square(4))
print(square(5))
'''


#20.	Write a python program to find the sum of all even numbers from 0to10
'''
num=10
i=1
sum=0
while i<=num:
    if i%2==0:
     sum=sum+i
    i=i+1
print('sum of even num is:',sum)
    


num=10
i=1
sum=0
while i<=num:
  if i%2 !=0:
    sum=sum+i
  i=i+1
print('sum of odd num is:',sum)


num=12
sum=0
for i in range(1,num+1):
    if i%2==0:
     sum=sum+i
print('sum of even num:',sum)
'''

'''
list=[1,2,3,4,5]
sqr=[i**2 for i in list]
print(sqr)

list=[1,2,3,4,5]
for i in list:
     sqr=i**2
     print(sqr)
i=1
while i<=len(list):
    sqr=i**2
    print(sqr)
    i=i+1
'''
'''
num=[10,2,3,4,5,6]
largest_num=num[0]
for i in num:
    if i>largest_num:
     largest_num=i
    print(largest_num)
'''
'''
num=[10,2,3,4,5,6]
max_num=max(num)
print(max_num)
numbers=[2,6,7,8,9,15,20]
num=[]
while num !=20:
    num.append(numbers)
    numbers=[2,6,7,8,9,15,20]
    print('max number is:',max(numbers))
'''
'''
n=int(input("enter your num"))
fact=1
i=1
while i<=n:
    fact=fact*i

    i=i+1
print(fact,end=" ")
'''

#max number
'''
list=[11,12,2,8,10]
x=0
for i in list:
    if i>x:
        x=i

print (x)
#min number

list=[100,12,2,8,1]
x=list[1]
for i in list:
    if i<x:
        x=i
print (x)
'''
a=(lambda x,y:y+x)
print(a(3,5))