#Dictionary Programs:
#1.	Python – Extract Unique values dictionary values
'''
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print("The original dictionary is : " ,test_dict)

# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values list is : " + str(res))
'''


'''
from itertools import chain

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print("The original dictionary is : ",test_dict)

res = list(sorted(set(chain(*test_dict.values()))))

print("The unique values list is : ",res)
'''
'''
dict1 = {'A': [1, 3, 5, 4],
         'B': [4, 6, 8, 10],
         'C': [6, 12, 4, 8],
         'D': [5, 7, 2]}

print("The original dictionary is : ", dict1)

# Using list comprehension, values() and sorted()
res = list(sorted({ele for val in dict1.values() for ele in val}))

print("The unique values list is : ", res)
'''
#2.	Python program to find the sum of all items in a dictionary
'''
dic={ 'x':455, 'y':223, 'z':300, 'p':908 }

print("Dictionary: ", dic)
print("sum: ",sum(dic.values()))
'''
#or
'''
def Sum(dic):
    sum=0
    for i in dic.values():
        sum=sum+i
    return sum
dic={ 'x':30, 'y':145, 'z':55 }
print("Dictionary: ", dic)
print("sum: ",Sum(dic))
'''

'''
dict={'ram':12,'shyam':13,'krishna':14}
sum=0
for i in dict.value():
    sum=sum+i
    print('sum:',sum(dict))
'''

#3.	Python | Ways to remove a key from Demonstrating key-value pair deletion using del
'''
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

print("The dictionary before performing remove is : " + str(test_dict))

del test_dict['Mani']
test_dict.remove('mani')
print("The dictionary after remove is : ",test_dict)

del test_dict['Manjeet']
print(test_dict)
'''


#or
'''
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

print("The dictionary before performing remove is : ", test_dict)

# Using pop() to remove a dict. pair
# removes Mani
removed_value = test_dict.pop('Mani')

print("The dictionary after remove is : ",test_dict)
print("The removed key's value is : ",removed_value)

test_dict={"Arusi":12,"Manjeet":14,"Mani":21,"Hariran":22}

removed_value = test_dict.pop('Manjeet', 'No Key found')

print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))
'''



#4.	Ways to sort list of dictionaries by values in Python – Using itemgette

#for implementing itemgetter
'''
from operator import itemgetter

# Initializing list of dictionaries
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age: ",sorted(lis, key=itemgetter('age')))

# using sorted and itemgetter to print list sorted by age in descending order
print("The list printed sorting by age in descending order: ",sorted(lis, key=itemgetter('age'), reverse=True)))
'''


#5.	Ways to sort list of dictionaries by values in Python – Using lambda function
'''
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print("The list printed sorting by age: ",sorted(lis, key=lambda i: i['age']))

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ",print(sorted(lis, key=lambda i: (i['age'], i['name']))))



# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(lis, key=lambda i: i['age'], reverse=True))

'''






#6.	Python | Merging two Dictionaries
# Python code to merge dict using update() method
'''
def Merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)
'''



#7.	Python – Convert key-values list to flat dictionary
'''
dic= { "day": [1, 2, 3], "name": ['Mon', 'Tues', 'Wed' ] }
print("Original dictionary: ",dic)

# convert to flat dictionary

f_dic= dict(zip(dic["day"], dic["name"]))
print("FLATTENED DICTIONARY: ", f_dic)
'''


#8.	Python – Insertion at the beginning in OrderedDict
'''
from collections import OrderedDict

dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
insrt = OrderedDict([("D", '400')])
final = OrderedDict(list(insrt.items()) + list(dic1.items()))
print("Resultant Dictionary :")
print(final)
'''

'''
from collections import OrderedDict

dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])

dic1.update({"D": '400'})
print(dic1)

dic1.move_to_end("D", last=False)

print("Resultant Dictionary :")
print(dic1)
'''

#9.	Python | Check order of character in string using OrderedDict( )
'''
if __name__ == '__main__':
    string = "YourString123"
    pattern = re.compile("[A-Za-z0-9]+")

    # if found match (entire string matches pattern)
    if pattern.fullmatch(string) is not None:
        print("Found match: " + string)
    else:
        # if not found match
        print("No match")
'''




#10.	Dictionary and counter in Python to find winner of election
'''
totalVotes=[]
dct = {}
i = 1
while(True):
    name = input('Please enter a name: ')
    if name == '':

        break
    votes = input('Please enter vote total for canidate: ')
    totalVotes.append(votes)
    totalVotesInt= map(int, totalVotes)
    total = sum(totalVotesInt)
    dct[i] = {name,votes,int(votes)/total*100}
    i += 1
header='{:>0}{:>10}{:>10}{:>20}'.format('ID','Name','Votes','% of Total Vote')
print(header)    
print("n".join("{}t{}".format(key, value) for key, value in dct.items()))
print('Total '+str(total))
print('The Winner of the Election is '+max(totalVotes))
'''

#11.	Python – Append Dictionary Keys and Values ( In order ) in dictionary
'''
test_dict = {"Gfg": 1, "is": 3, "Best": 2}
print("The original dictionary is : ",test_dict)
res = list(test_dict.keys() + list(test_dict.values())
print("The ordered keys and values : ",res)



from itertools import chain
test_dict = {"Gfg": 1, "is": 3, "Best": 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# chain() is used for concatenation
res = list(chain(test_dict.keys(), test_dict.values()))

# printing result
print("The ordered keys and values : " + str(res))





#12.	Python | Sort Python Dictionaries by Key or
def dictionairy():
    # Declaring hash function
    key_value = {}

    # Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=
    lambda kv: (kv[1], kv[0])))


def main():
    # function calling
    dictionairy()


# main function calling
if __name__ == "__main__":




#13.	Python – Sort Dictionary key and values List

# Function calling
def dictionairy():
    # Declare hash function
    key_value = {}

    # Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")
    print("Keys are")

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")


def main():
    # function calling
    dictionairy()

    # Main function calling


if __name__ == "__main__":
    main()





#14.	Handling missing keys in Python dictionaries
# initializing Dictionary
d = {'a': 1, 'b': 2}

# trying to output value of absent key
print("The value associated with 'c' is : ")
print(d['c'])

country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')

# search dictionary for country code of India
print(country_code['India'])

# search dictionary for country code of Japan
print(country_code['Japan'])




#15.	Python dictionary with keys having multiple inputs
import random as rn

# creating an empty dictionary
dict = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;

# print the dictionary
print(dict)

places = {("19.07'53.2", "72.54'51.0"): "Mumbai", \
          ("28.33'34.1", "77.06'16.6"): "Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)






#16.	Print anagrams together in Python using List and Dictionary

dict = {}

# traversal
for val in d1:

    # sorts list
    key = ''.join(sorted(val))

    if key in dict.keys():
        dict[key].append(val)
    else:
        dict[key] = []
        dict[key].append(val)

        # traverse dictionary and join keys together
result = ""
for key, value in dict.items():
    result = result + ' '.join(value) + ' '

return result

d1 = ['act', 'cat', 'silent', 'listen']
print("Words: ", d1)
print("Anagram: ", Anagram(d1))

#17.	K’th Non-repeating Character in Python using  List Comprehension and OrderedDict
from collections import OrderedDict
import itertools
def kthRepeating(inp,k):
   # returns a dictionary data
   dict=OrderedDict.fromkeys(inp,0)
      # frequency of each character
   for ch in inp:
      dict[ch]+=1
   # now extract list of all keys whose value is 1
   nonRepeatDict = [key for (key,value) in dict.items() if value==1]
   # returns (k-1)th character
   if len(nonRepeatDict) < k:
      return 'no ouput.'
   else:
      return nonRepeatDict[k-1]
# Driver function
if __name__ == "__main__":
   inp = "tutorialspoint"
   k = 3
   print (kthRepeating(inp, k))








#18.	Check if binary representations of two numbers are anagram
from collections import Counter


def checkAnagram(n1, n2):
    # convert numbers into binary
    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]

    # append zeros in shorter string
    zeros = abs(len(bin1) - len(bin2))
    if (len(bin1) > len(bin2)):
        bin2 = zeros * '0' + bin2
    else:
        bin1 = zeros * '0' + bin1

    # convert binary to  dictionary
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)

    # compare both dictionaries
    if dict1 == dict2:
        print('Yes')
    else:
        print('No')








#19.	Python Counter to find the size of largest subset of anagram words
from collections import Counter


def maxAnagramSize(input):
    # split input string separated by space
    input = input.split(" ")

    # sort each string in given list of strings
    for i in range(0, len(input)):
        input[i] = ''.join(sorted(input[i]))

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    freqDict = Counter(input)

    # get maximum value of frequency
    print(max(freqDict.values()))


# Driver program
if __name__ == "__main__":
    input = 'ant magenta magnate tan gnamate'
    maxAnagramSize(input)

from collections import Counter


def remov_duplicates(input):
    # split input string separated by space
    input = input.split(" ")

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    UniqW = Counter(input)

    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print(s)


# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)








#21.	Python Dictionary to find mirror characters in a string


def mirrorChars(input, k):
    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))

    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k - 1]
    suffix = input[k - 1:]
    mirror = ''

    # change into mirror
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]

    # concat prefix and mirrored part
    print(prefix + mirror)


# Driver program
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input, k)




#22.	Counting the frequencies in a list using dictionary in Python
def CountFreq(li):
    freq = {}
    for item in li:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
     print(freq)
li =[1, 1, 3, 2, 6, 5, 3, 1, 3, 3, 1, 4, 6, 4, 4, 2, 2, 2, 2]
CountFreq(li)






#23.	Python | Convert a list of Tuples into Dictionary

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))



#24.	Python counter and dictionary intersection example(Make a string using deletion and rearrangement)

from collections import Counter


def makeString(str1, str2):
    # convert both strings into dictionaries
    # output will be like str1="aabbcc",
    # dict1={'a':2,'b':2,'c':2}
    # str2 = 'abbbcc', dict2={'a':1,'b':3,'c':2}
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    # take intersection of two dictionries
    # output will be result = {'a':1,'b':2,'c':2}
    result = dict1 & dict2

    # compare resultant dictionary with first
    # dictionary comparison first compares keys
    # and then compares their corresponding values
    return result == dict1


# Driver program
if __name__ == "__main__":
    str1 = 'ABHISHEKsinGH'
    str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (makeString(str1, str2) == True):
        print("Possible")
    else:
        print("Not Possible")



#25.	Python dictionary, set and counter to check if frequencies can become same

def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))


# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    CountFrequency(my_list)





#26.	Scraping And Finding Ordered Words In A Dictionary using Python
def isOrdered():
    collection = scrapeWords()
    collection = collection[:100]
    word = ''
    for word in collection:
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1
    if (len(word) < 3):
        continue
    while i < l:
        if (ord(word[i]) > ord(word[i + 1])):
            result = 'Word is not ordered'
        break
    else:
        i += 1

    if (result == 'Word is ordered'):
        print(word, ': ', result)




#27.	Possible Words using given characters in Python
def Countchar(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
def find_words(word_list, charSet):
    for word in word_list:
        flag = 1
        chars = Countchar(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)
word_list = ['mat', 'boy', 'bat', 'goal', 'get', 'got', 'orange']
charSet = ['e', 'o', 'b', 'a', 'g', 'l', 't']
find_words(word_list, charSet)

input="Extreme"
letter=(x.lower() for x in input)
print(letter)
'''



#28.	Python – Keys associated with Values in Dictionary
'''
my_dict ={"Hi":100, "there":121, "Mark":189}
print("The dictionary is :",my_dict)

dict_key = list(my_dict.keys())
print("The keys in the dictionary are :",dict_key)
dict_val = list(my_dict.values())
print("The values in the dictionary are :",dict_val)

my_position = dict_val.index(100)
print("The value at position 100 is : ",dict_key[my_position])

my_position = dict_val.index(189)
print("The value at position 189 is",dict_key[my_position])


from collections import defaultdict
test_dict = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}
print("The original dictionary is : ",test_dict)

res = defaultdict(list)
for key, val in test_dict.items():
    for ele in val:
        res[ele].append(key) 
print("The values associated dictionary :",dict(res)) 
'''









