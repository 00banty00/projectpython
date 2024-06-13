"""
filter the data, cache the filtered data in pyspark

"""

df = spark.read.format("csv")\
                .load(path)

df = df.filter(col("col1")==)

df.cache()



# 
orders_df.select("order_id","order_status").filter("order_status == 'CLOSED'").cache() -----> data cached


1) orders_df.select("order_id","order_status").filter("order_status == 'CLOSED'").count() ----->from cached
2) orders_df.filter("order_status == 'CLOSED'").select("order_id","order_status").count() -----> from cached
3) orders_df.select("order_id").filter("order_status == 'CLOSED'").count()                ------> from noraml
4) orders_df.select("order_id","order_status").filter("order_status == 'OPEN'").count()   ------> from normal




class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

    def printAll(self,head):
        current = head
        while current != None:
            print("the value is {}".format(current.key))
            current = current.next

    def search(self,head,x):
        node = head
        pos = 1
        while node.key != None:
            if node.key == x:
                return pos
            
            else:
                pos += 1
                print("node value is {}".format(node.key))
                node = node.next

        return -1
    
    def insertAtBegining(self,key):
        head.next = Node(key)
        head




head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.printAll(head)

head.search(head,20)


memo = [None] * 100

def fib(n):
    if memo[n] != None:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]


fib(5)


subStr = [[-1]*5 for i in range(5)]