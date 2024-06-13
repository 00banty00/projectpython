a =5

'''
geenrate the list of 1st 20 even no
'''

def eveList(num):
    eve_num = []
    count = 0
    i = 1
    while count <= num:
        if i % 2 == 0:
            eve_num.append(i)
            count += 1
            i += 1
        else:
            i += 1
    return eve_num

eveList(20)

num_list1 = [1,2,3,4,5,6,7,8,9]

eve = ['even' if num %2 == 0 else 'odd' for num in num_list1]


class calculation:
    def __init__(self,num1, num2):
        self.x = num1
        self.y = num2

    def eveList(self):
        eve_num = []
        count = 0
        i = 1
        while count <= self.x:
            if i % 2 == 0:
                eve_num.append(i)
                count += 1
                i += 1
            else:
                i += 1
        return eve_num
    
    def isPrime(self):
        for i in range(2,self.x):
            if self.x % i == 0:
                return False
        return True
    
    def lambdaEve():
        eve = lambda x: x % 2 == 0
        return eve

    
obj1 = calculation(11,20)
obj1.eveList()    
obj1.isPrime()
obj1.lambdaEve()

num_list1 = [1,2,3,4,5,6,7,8,9]


eve = list(map(lambda x: '1' if x % 2 == 0 else '0',num_list1))




'''
generate a dict with 2 keys- lt_20, gt_20
'''

def dictVal(list1):
    lt_20 = [num for num in list1 if num < 20]
    gt_20 = [num for num in list1 if num > 20]
    res_dict = {'lt_20':lt_20,'gt_20':gt_20}
    
    return res_dict


dictVal(output_eve)


'''
"Pythoninterview"

o/p = 1st reoccuring char
'''
str1[0]
def repChar(str1):
    for i in range(len(str1)):
        for j in range(1,len(str1)):
            if str1[i] == str1[j]:
                return str1[i]
            
    return -1

repChar("Pythoninterview")


# silver,gold and medival architecture

