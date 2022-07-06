        #Tuple Programs:
#1.	Python program to Find the size of a Tuple
'''
import sys
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")
'''

#2.	Python – Maximum and Minimum K elements in Tuple

# Python3 code to demonstrate working of
# Maximum and Minimum K elements in Tuple
# Using sorted() + loop

'''
test_tup = (5, 20, 3, 7, 6, 8)
print("The original tuple is : " + str(test_tup))
K = 2
res = []
test_tup = list(sorted(test_tup))
print(test_tup)
for idx, val in enumerate(test_tup):
	if idx < K or idx >= len(test_tup) - K:
		res.append(val)
res = tuple(res)
print("The extracted values : " + str(res))
'''


'''
tuple = (7, 25, 36, 9, 6, 8)
k=2
new_tuple=[]
tuple=sorted(tuple)
for x in tuple:
    new_tuple.append(x)
print('my new tuple:',new_tuple[-k:])
print('my new tuple:',new_tuple[0:2])
'''

#3.	Create a list of tuples from given list having number and its cube in each tuple

'''
def cubeoflist(li):
    # list of tuples
    result=[(num, num**3) for num in li]
    return result
li = [3, 4, 1, 2]

print(cubeoflist(li))
'''




#4.	Python – Adding Tuple to List and vice – versa
'''
test_list = [5, 6, 7]
test_tup = (9, 10)
test_list+= test_tup
test_list+=test_tup
for i in test_list:
    print(i)


print("The container after addition : ",test_list)
'''





#5.	Python – Closest Pair to Kth index element in Tuple
'''
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
test_list.sort()
print(test_list)
K = 2
for i in test_list:
 print(i)
print('Closest Pair to Kth index element in Tuple:',test_list[-K:])
'''



#6.	Python – Join Tuples if similar initial element
'''
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
print("The original list is : " + str(test_list))
res = []
for i in test_list:
    res.append(i)
    print(res)

print("The extracted elements : " + str(res))

'''
#7.	Python – Extract digits from Tuple list
'''
from itertools import chain
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res  = set()
for i in temp:
    res.add(i[0])

print(res)
'''


#8.	Python – All pair combinations of 2 tuples
'''
from itertools import chain, product

tuple1 = (1, 2)
tuple2 = (3, 4)

print("The tuple 1 : " + str(tuple1))
print("The tuple 2 : " + str(tuple2))
result = list(chain(product(tuple1, tuple2), product(tuple2, tuple1)))
print("The resultant tuple : " + str(result))

'''
#or
'''
tuple1 = (4, 5)
tuple2 = (6, 7)
        #  original tuples
print("The tuple 1 : " + str(tuple1))
print("The tuple 2 : " + str(tuple2))
        # All pair combinations of 2 tuples
result = [(x, y) for x in tuple1 for y in tuple2]
result = result + [(x, y) for x in tuple2 for y in tuple1]

print("The resultant tuple : " + str(result))

tuple1 = (4, 5)
tuple2 = (6, 7)
tuple3=[(tuple1) +(tuple2)]
print(tuple3)

'''




#9.	Python – Remove Tuples of Length K
'''
List =  [(12, 13, 14), (14, 15), (16, 17), (18, 19)]
#  original list
print("The original list : " + str(List))
# initializing K
K = 2
result = [a for a in List if len(a) != K]
# printing result
print("Resultant list : " + str(result))
'''




#10.	Sort a list of tuples by second Item
'''
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
tup.sort()
print(tup)
tuple = [(200, 6), (100, 3), (400, 12), (300, 9)]
print("Orignal Tuple List :" ,tuple)
'''


'''
def Sort(tuple):
    # Sorts in Ascending order
    tuple.sort(key = lambda a: a[1])
    return tuple

# printing the sorted list of tuples
print("Sorted Tuple List:" ,Sort(tuple))
'''
#11.	Python program to Order Tuples using external List
'''
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

print("The original list is : " + str(test_list))

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

temp = dict(test_list)
res = [(key, temp[key]) for key in ord_list]

print("The ordered tuple list : " + str(res))
'''




#12.	Python – Flatten tuple of List to tuple
'''
test_tuple = ([5, 6], [6, 7, 8, 9], [3])
print("The original tuple : " + str(test_tuple))
res = tuple(sum(test_tuple, []))
print("The flattened tuple : " + str(res))
'''


#13.	Python – Convert Nested Tuple to Custom Key Dictionary
'''
test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
print("The original tuple : " + str(test_tuple))

        # Convert Nested Tuple to Custom Key Dictionary
        # Using list comprehension + dictionary comprehension
res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}
for sub in test_tuple]

        # printing result
print("The converted dictionary : " + str(res))
'''

#Searching and Sorting Programs:
#1.	Python Program for Binary Search (Recursive and Iterative)
'''
def binary_search(n, item):
   left, right = 0, len(n)
   while right > left:
    middle = (left + right) // 2
        if nums[middle] > item:
             right = middle
        elif nums[middle] < item:
          left = middle + 1
    else:
     return middle
      return None

'''
#2.	Python Program for Linear Search

        def linearsearch(arr, x):
         for i in range(len(arr)):
          if arr[i] == x:
           return i
          return -1


        arr = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
        x = 'a'
        print("element found at index " + str(linearsearch(arr, x)))

 #3.	Python Program for Insertion Sort
 '''
        for i in range(1, len(arr)):

         key = arr[i]

         # Move elements of arr[0..i-1], that are
         # greater than key, to one position ahead
         # of their current position
         j = i - 1
         while j >= 0 and key < arr[j]:
          arr[j + 1] = arr[j]
          j -= 1
         arr[j + 1] = key

        # Driver code to test above
        arr = [12, 11, 13, 5, 6]
        insertionSort(arr)
        print("Sorted array is:")
        for i in range(len(arr)):
         print("%d" % arr[i])



#4.	Python Program for Recursive Insertion Sort
# recursive way
def insertionSortRecursive(arr,n):
   # base case
   if n<=1:
      return
   # Sort
   insertionSortRecursive(arr,n-1)
   last = arr[n-1]
   j = n-2
   # move ahead
   while (j>=0 and arr[j]>last):
      arr[j+1] = arr[j]
      j = j-1
   arr[j+1]=last
# main
arr = [1,5,3,4,8,6,3,4,5]
n = len(arr)
insertionSortRecursive(arr, n)
print("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")



#.	Python Program for QuickSort
   def partition(arr, low, high):
    # rightmost element as pivot
    pivot = arr[high]

    # pointer
    i = low - 1

    for j in range(low, high):
     if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # return the position
    return i + 1


   # QickSort
   def QuickSort(arr, low, high):
    if low < high:
     # find pivot element
     pivot = partition(arr, low, high)
     quickSort(arr, low, pivot - 1)
     quickSort(arr, pivot + 1, high)


#6.	Python Program for Iterative Quick Sort

   def partition(array, low, high):
    i = (low - 1)
    x = array[high]

    for j in range(low, high):
     if array[j] <= x:
      i = i + 1
      array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)




#8.	Python Program for Bubble Sort
 for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9, 8, 3]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)







#9.	Python Program for Merge Sort





#10.	Python Program for Iterative Merge Sort
'''