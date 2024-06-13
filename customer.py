customer = input("What is your Name ? ")
print(f"Hi {customer}  Nice to meet you")

if len(customer) < 3:
    print("Name is short")
elif len(customer) > 10:
    print("name is too long")
else:
    print("Name looks good")
budget = input("What is your Budget ? ")
if int(budget) < 1000:
    print("Too low")
else:
    print("Enjoy shopping")


for i in range(1,10,2):
    print(i, i*i, i*i*i)

for char in 'Leopard':
    print(char)

for animal in ['cat', 'Dog', 'Tiger', 'Lion', 'Leopard']:
    print (animal)

for key in {'A101': 'Rajesh', 'A111': 'Sunil', 'A112': 'Rakesh'}:
    print(key)

i = 1
while 111:
    print(i, end='\n')
    i += 1
    if i > 10:
        break
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(n-i):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(i,n):
        print('_', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(n-i):
        print('*', end=' ')
    print()


for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(n-i):
        print('*', end=' ')
    print()


def sum_n(n):
    sum = 0
    a = 1
    while a<=n:
        sum = sum + a
        a = a+1

    return sum


import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.Builder.appName('test').get