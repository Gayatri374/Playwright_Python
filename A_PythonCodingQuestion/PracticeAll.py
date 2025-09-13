var1=(1,2,3,4,5,6,6,'a','a','b','c','d')

def dup(s):
    return set(s)

print('without duplication:',dup(var1))

def di(a):
    dup=set([char for char in a if a.count(char)>1])
    return dup
print('duplicated values:',di(var1))



# frequence

var2=("MADAMAAAJA")
from collections import Counter

def fre(b):
    return dict(Counter(b))
print('frequency:',fre(var2))

# Odd numbers

var3=[1,2,3,4,5,6,7,8,9,10,11]

for i in var3:
    if i%2!=0:
        print(i,end=" ")


# palindrom

var4='mam'

def pel(d):
    return d==d[::-1]

print(pel(var4))


# reverse string

var5='gayatri'

def rev(f):
    return f[::-1]
print(rev(var5))


# second largest

var6=[1,2,3,4,4,5,6,7,7,8,9]

def sec(b):
    uni=list(set(b))
    uni.sort()
    return uni[-2]

print(sec(var6))


# prime number


# for num in range(1,12):
#     if num>1:
#         for i in range(2,num):
#             if i%num==0:
#                 break
#         else:
#             print(num,end=' ')


for num in range(1,12):
    if num > 1:  # only check for n > 1
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num, end=' ')