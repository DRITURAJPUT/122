#list multiple iteam, ordered, changable,mutable,duplicate values

# Negative indexing
'''
list=['A','F,','E','V']
print(list[1])
print(list[-1])
print(list[-1::-2])
print(list[-1:])
print(list[:-1])
print(list[:1])
print(list[1::-3])
'''
# change item value
'''
list=['apple','banana','orange']
list[1]='water'
print(list)
'''

#change range of item value
'''
list=['apple','banana','orange','lemon']
list[1:]=['barry','watermelon']
print(list)
'''
# insert new item
'''
list=['apple','banana','orange']
list.insert(2,'pineapple')
print (list)
'''
# append function
'''
list=['apple','banana','orange']

list.append('Pineapple')
print(list)
'''

#extend list
'''
list_1=['apple','banana','orange']
list_2=['1','carrot','lemon']
list_1.extend(list_2)
print(list_1)
'''
# and any itrable
'''
list_1=['apple','banana','orange']
tuple_2=('1','carrot','lemon')
list_1.extend(tuple_2)
print(list_1)
'''

#remove specified item
'''
list_1=['apple','banana','orange']

list_1.remove('orange')
print(list_1)
'''

#the pop method remove the specified index
'''
list_1=['apple','banana','orange']
list_1.pop(2)
print(list_1)
'''

#loop list
'''
list_1=['apple','banana','orange']
for x in list_1:
    print(x,end=' * ')
'''

# loop through index nimber
'''
list_1=['apple','banana','orange']
for i in range(len(list_1)):
    print(list_1[i])
print (len(list_1))
'''

# using a while loop
'''
list_1=['apple','banana','orange']
i=0
while i< len(list_1):
    print(list_1[i])
    i=i+1
for i in range (len(list_1)):
    print ('index',i,'=',list_1[i])
'''


# list comprehension() it sort the syntax
'''
list_1=['apple','banana','orange']
[print(x) for x in list_1]
'''

# second type of com
#old one
'''
list_1=['apple','banana','orange']
list_2=[]
for x in list_1:
    if 'orange'in x:
        list_2.append(x)
print (list_2)
'''
# new one'
'''
list_1=['apple','banana','orange']
list_2 =[x for x in list_1 if x =='apple']
print (list_2)
list_2 =[x for x in list_1 if x !='apple']
print (list_2)

list_2 =[x for x in list_1 if'apple' in x]
print (list_2)
list_2 =[x for x in list_1 if'apple' not in x]
print (list_2)
'''
#comprehension iterable for
'''
list=[x for x in range(10) ]
print(list)
list=[x for x in range(10) if x < 5 ]
print(list)
'''
###
'''
list =['x','a','a','d',]
list_1=[i if i!='a' else 'x' for i in list]

print (list_1)
'''
# sort list alphanumarically
'''
list=['cpple','banana','orange']
list.sort()
print(list)
'''
# sort number
'''
list=[1,2,3,5,2,4,3]
list.sort()
print('short the list',list)
# sort desending
list.sort(reverse=True)
print('desending order',list)
'''

#customize sort function
'''
def myfun(n):
    return abs(n-50)
list=[100,200,60,50,40]
list.sort(key=myfun)
print(list)


list=['apple','ORANGE']
list.sort(key=str.upper)
print(list)
'''
#copy list
'''
list=['apple','ORANGE']
n_list = list.copy()
print(n_list)
'''
#join ()
'''
list_1=['apple','ORANGE']
list_2=[1,2,3,4,]
list_3 = list_1 + list_2
print(list_3)'''
'''
list_1=['apple','ORANGE']
list_2=[1,2,3,4,]
for x in list_2:
    list_1.append(x)
    print(list_1)'''

#q1	Python program to interchange first and last elements in a list.
# Swap function
'''
list=[2,5,3,1,7,5]
u=list[0]
list[0]=list[-1]
list[-1]=u
print(list)
'''

#17.Python program to swap two elements in a list
# 2 and 4
'''
list=[2,8,3,1,7,5]
x= list[1]
list[1]=list[3]
list[3]=x
print(list)
'''
#18.	Python | Ways to find length of list
'''
l=[1,2,3,4,5]
print(len(l))
'''

# 19.	Python | Ways to check if element exists in list
'''
x=str(input('enter'))
list=['a','b','c','d']
list1=[]
for i in list:

    if x in i:
        list1.append(i)
        print(list1)
        break
    elif x not in i:
        print('value not found')
        break
'''
#20.	Different ways to clear a list in Python.
'''
list=[1,2,4,6,7,]
print('list before clear:',list)
list.clear()
print('list after clear:',list)'''

#21.	Python | Reversing a List
'''
list=['ram', 'is', 'a', 'good','boy',1,2,3]
print('list before reverse:',list)
list.reverse()
print('list after reverse:',list)'''

#22.	Python program to find sum of elements in list
'''list=[1,2,4,6,7,]
total=0
i=1
for i in range(len(list)):
    total= total+len(list)
print("sum of all elements:",total)'''
#23.	Python | Multiply all numbers in the list
'''
def multiplyList(myList) :
	result = 1
	for x in myList:
		result = result * x
	return result
list1 = [1, 2, 3]

print(multiplyList(list1))
or
import math
list=[1,2,3,4,5]
result =math.prod(list)
print(result)

'
#or
from functools import reduce
list=[1,2,3,4,5]
result = reduce ((lambda x, y: x * y), list)
print(result)
'''

#24.	Python program to find smallest number in a list
'''
list = [1,2,3,4,5]
print("smallest number:",min(list) )

def min():
    list=[100,12,2,8,1]
    min=list[0]
    for a in list:
        if a<min:
         min=a
    print(min)
min()
#or
list=[100,12,2,8,1]
x=list[0]
for i in list:
    if i<x:
        x=i
print (x)
'''
#25.	Python program to find largest number in a list
'''
list = [1,2,3,4,5]
print("largest number:",max(list) )

print([[]]*5)

list=[11,12,2,8,10]
x=0
for i in list:
    if i>x:
        x=i

print (x)
'''

#while loop

'''
l


NumList = []
Number = int(input("Please enter element length in list "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element "))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))
'''





#26.	Python program to find second largest n a list
'''
list=[1,2,3,4,5,]
new_list= set (list)
new_list.remove(max(new_list))
print(max (new_list))
#or
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Second largest element is:", list1[-2])
'''
#or
'''
def secondlargest():
    secondlargest=0
    list1=[1,2,3,4,5,6,7]
    for i in range(len(list1)):
        if i>secondlargest:
            secondlargest=i
    print("The second largest no is:",secondlargest)
secondlargest()
'''
#or
'''
def secondmax(list):
    sublist = [x for x in list if x < max(list)]
    return max(sublist)

if __name__ == '__main__':
    list = [10, 20, 4, 45, 99]
    print(secondmax(list))

The condition if __name__ == ‘__main__’ is used in a
Python program to execute the code inside the if statement only when the program is executed directly by the Python interpreter. When the code in the file is imported as a module the code inside the if statement is not executed.
'''

#27	Python program to find N largest elements from a list
'''
list = [1,2,3,4,5,6]
N = 2
list.sort()
print(list[-N:])
#or
def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    print(final_list)
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
Nmaxelements(list1, N)


'''
#28.	Python program to print even numbers in a list
'''
list = [1,2,3,4,5,6]
for x in list:
    if x%2==0:
     print(x, end =" ")
     '''
#or
'''
list = [1,2,3,4,5,6]
i=1
while i<=len(list):
    if i%2==0:
     print(i)
    i=i+1

n=5
fact=1
i=1
while i <=5:
    fact=fact*i
    i=i+1
print(fact)
'''
'''
n=int(input('enter your number'))
count=0
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
     print("prime number")
else:
   print("not prime number")
'''

#29.Python program to print odd numbers in a List
'''
list = [1,2,3,4,5,6]
new_list=[]
for x in list:
    if x % 2==1:
     new_list.append(x)
print(new_list, end =" ")
'''

#30.	Python program to print all even numbers
# in a range
'''
a=1-20
for i in range(1,20+1):
    if (i%2==0):
        print(i)
'''

#31.	Python program to print all odd numbers in a range
'''a=1-10
for i in range(1,20+1):
    if (i%2==1):
        print(i)
'''
#32.	Python program to print positive numbers in a list
'''
a=[1,3,-4,-4,5,5]
for i in a:
    if i >=0:
     print("positive num:",i)
        #or

list1 = [-10, 21, -4, -45, -66, 93]
i=0
while(i < len(list1)):
    if list1[i] >= 0:
        print(list1[i], end = " ")
    i += 1
'''
#or
'''
list=[1,3,-7,-8,-9,0]
x=[num for num in list if num >= 0]
print("positive numberin the list:",*x)
'''
#33.	Python program to print negative numbers in a list
'''
list=[1,3,-7,-8,-9,0]
x=[num for num in list if num < 0]
print("positive numberin the list:",*x)'''
'''

'''
#34.	Python program to print all positive numbers in a range
'''
a= -4,10
i=1
for i in range(-4,10):
    if i >=0:
        print("positive num:",i)
   '''

#35.	Python program to print all negative numbers in a range
'''
a= -3,5
i=1
for i in range(-3,5):
    if i <0:

     print("negative num:",i)
     '''


#36.	Remove multiple elements from a list in Python
'''
list = [1,2,3,4,5,6]
for i in list:
    if i%2==0:
        list.remove(i)
print('modified list:',list)
'''



#37.	Python – Remove empty List from List
'''
list = [1,2,3,4,5,[],6]

list.remove([])
print('Update list:',list)
'''

#38.	Python | Cloning or Copying a list
'''
list = [1,2,3,4,5,6]
n=list.copy()
print('copied list:',n)
'''
#39.	Python | Count occurrences of an element in a list
'''
list = [1,2,3,4,5,6]
n= list.count(3)
print('num frequency of 3 in list:',n)
'''

#40.	Python | Remove empty tuples from a list
'''
list = [1,2,3,4,(),(),5,6]
list=[t for t in list if t]
print(list)
#41.	Python | Program to print duplicates from a list of integers
list = [1,2,3,4,5,6,6,4]
print(" the orignal list is:",list)
res=[]
[res.append(x) for x in list if x not in res]
print ('list after removing duplicate:',res)
#or
list = [1,2,3,4,5,6,6,4]
print('The first list is:',list)
m=list(set(list))
print("The list after removing duplicate:",m)
'''
#42.	Python program to find Cumulative sum of a list
'''
list = [1,2,3,4,5,6,6,4]
l=len(list)
i=0
j=0
while i<l:
    j=j+list[i]
    i=i+1

print(j)

new_list=[]
j=0
for i in list:
    j=j+i

print('comulative sum:',j)
'''




'''
#or
def Cumulative(l):
   new = []
   cumsum = 0
   for element in l:
      cumsum += element
      new.append(cumsum)
   return new
lists = [10, 20, 30, 40, 50]
print ("New list:",Cumulative(lists))
def comulative(l):
    new=[]
    j=0
    for i in l:
        j=j+i
        new.append(j)
    return new
list=[1,2,3,4,5,6,7]
print('new list:', comulative(list))
'''



#43.	Python | Sum of number digits in List
'''
list = [1,2,3,4,5,6,6,4]
total=0
i=1
for i in range(len(list)):
    if i<=(len(list)):
      total =total+i
    i=i+1
print('sum of:' ,i)
'''
#44.	Break a list into chunks of size N in Python'''


#45.	Python | Sort the values of first list using second list.
'''

list1 = ['o','p','l','h','f']
list2 = [1,2,4,3,5]
print(list(zip(list1,list2)))
print(set(zip(list1,list2)))
a= (list(sorted(list2)))
print(a)
'''
'''
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

# printing original lists
print("Original list 1 : " + str(test_list1))
print("Original list 2 : " + str(test_list2))

# using naive method to
# add two list
res_list = []
for i in range(0, len(test_list1)):
    res_list.append(test_list1[i] + test_list2[i])

# printing resultant list
print("Resultant list is : " + str(res_list))
'''






























