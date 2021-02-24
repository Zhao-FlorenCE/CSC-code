#basic list
'''
s1 = [i for i in range(1,57,2)]
s2 = [i for i in range(26 + 1,160) if i % 4 == 0 and i % 10 == 6]
print(s1)
print(s2)
'''
#list.sort()
'''
str1 = input()
str2 = input()
lt1 = list(str1)
lt2 = list(str2)
lt1.sort()
lt2.sort()
if lt1 == lt2:
    print("Yes")
else:
    print("No")
'''
#Exercises

#1
from math import sqrt
N = int(input("Input a integer:"))
Min = min(80,N)
Lis = [x for x in range(2,Min) if 0 not in [ x % d for d in range(2, int(sqrt(x))+1)]]
print(Lis)

#Exe1 extension
'''
from math import sqrt
N = int(input())
Lis = [x for x in range(2,N) if 0 not in [ x % d for d in range(2, int(sqrt(x))+1)]]
print(Lis)
lIs = [x for x in Lis if x < 50]
print(lIs)
'''

#2
N = int(input("Input ur Num: "))
List = [1] * N
dir = 1
for i in range(1,N):
    if i % 7 == 0 or str(i).find('7') != -1:
        dir *= -1
    List[i] = List[i - 1] + dir
print(List[N - 1])