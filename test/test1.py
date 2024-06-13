import yaml

with open('/Users/chandan/Desktop/Data Science/Git/projectpython/config.yaml', 'r') as file:
    config = file.read()

config[0]


def decorator(func1):
    def wrapper():
        print("before function call")
        func1()
        print("after func1 call")

    return wrapper

@decorator
def hello():
    print("Hello decorator")

hello()


# merge sort

def merge(arr,low,mid,high):
    left = arr[low:mid]
    right = arr[mid:high]
    i,j,k = 0,0,low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            K += 1
            j += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

    




def mergeSort(arr):
    low = 0
    high = len(arr)
    if low < high:
        mid = (low + high)//2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)

    return arr

arr = [10,5,30,15,7]
mergeSort(arr)

1234//10

# List

l1 = [1,2,3,4]
l1.append(5)
max(l1)

len(l1)
sum = 0
for i in range(len(l1)):
    sum = sum + l1[i]
mean = sum/len(l1)

from functools import reduce

sum = lambda x,y : x+y
l_sum = reduce(sum,l1)
avg = l_sum/len(l1)


pure_sum = lambda l:l[0] if len(l) == 1 else l[0]  + pure_sum(l[1:])

pure_sum(l1)

# even and ODd

l2 = [10,41,30,15,80]
even = [x for x in l2 if x % 2 == 0]
odd = [x for x in l2 if x % 2 != 0]
ev_fun = lambda x: x if x % 2 == 0 else None

lambda_even = list(filter(lambda x: x if x % 2 == 0 else None,l2))
lambda_even(l2)

sq_lambda = list(map(lambda x:x**2,l2))




s1 = "geeks for geeks"

s2 = s1.split()

"".join(s2)

s3 = "geek"
s3[::-1]

def isSubseq(s1,s2):
    i,j = 0,0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1

        else:
            i += 1

    if j == len(s2):
        return True
    else:
        return False
    

isSubseq("ABCDE","AED")


str1 = "Welcome to GFG"

str1.split(" ")

def revWord(str):
    left = 0
    right = len(str)-1
    while left < right:
        str[left],str[right] = str[right],str[left]
        left += 1
        right -= 1

    return str


revWord("Welcome")

len("Welcome")

str1[0] = 'c'

str2 = "an apple a day keeps the doctor away and apple is good for health"
word_list = str2.split(" ")
word_freq = [word_list.count(word) for word in word_list]

word_dict = dict(zip(word_list,word_freq))

dict1 = {}









        

