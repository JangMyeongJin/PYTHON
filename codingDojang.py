#!/usr/bin/env python
# coding: utf-8

# 1000미만 자연수 중 3,5의 배수 합

# In[ ]:


a =[]
for i in range(1000):
    if i % 3 == 0 or i % 5 ==0:
        a.append(i)
print(sum(a))


# 1. 김씨와 이씨의 수
# 2. 이재영의 수
# 3. 중복되 이름 제거
# 4. 오름차순으로 정렬

# In[55]:


names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")

count_lee = 0
count_kim = 0

#1
for name in names:
    if name[0] == "이":
        count_lee += 1
    if name[0] == "김":
        count_kim += 1

#2
print(count_lee,count_kim)
print(names.count("이재영"))

#3
list_names = list(set(names))
print(list_names)

#4
list_names.sort()
print(list_names)


# 음수는 앞쪽으로, 양수는 뒷쪽으로 정렬. 단 순서는 안바뀌게

# In[61]:


a= [5,3,-1,-7,2,-7]

list = [i for i in a if i < 0]
list1 = [i for i in a if i > 0]
list_a = list + list1

print(list_a)


# 숫자를 입력 받았을 때 0~9까지 숫자가 한번만 사용되었는지

# In[92]:


num = input("숫자입력")
set_num = set(num)
print(len(set_num)==len(num))


# In[10]:


a = int(input("숫자입력"))

for i in range(a):
    b = a*"O"
    c = b[:a-i]
    d = a*"X"
    print(c,d)


# 피보나치수열의 구하기

# In[12]:


a=[1,2]
b=[]
for i in range(100):
    a.append(a[i]+a[i+1])
    if a[i] % 2 == 0:
        b.append(a[i])
print(a)
print(b)
   
    


# 게시판 페이지 만들기

# In[2]:


import math

m = int(input("총건수 : "))
n = int(input("한 페이지에 보여질 게시물 수 : "))

print(math.ceil(m/n))


# 1~1000에서 각 숫자 갯수 구하기

# In[9]:


count = {x:0 for x in range(0,10)}

for x in range(1,10001):
    for i in str(x):
        count[int(i)] += 1
        
print(count) #원하는 숫자의 갯수 = count[x]


# 숫자를 각 자리수별 분리

# In[22]:


#1. 문자열로 변환 후 분리
num1 = 123
a=[]
for i in str(num1):
    a.append(i)
print(a)

#2. map 함수를 이용하여 분리
num2 = [123,456]
b = sum(map(int,num2))
print(b)


# 리스트 회전

# In[122]:


def list_turn(list_):
    num = int(list_.pop(0))
    
    if num > 0:
    
        list_num = list_[ len(list_) - num :]
    
        del list_[ len(list_) - num :]
        
    elif num < 0:
        
        list_num = list_[ -num : ]
        
        del list_[ -num : ]
    
    return list_num + list_

print(list_turn(input("").split(" ")))


# In[138]:


from datetime import time

p1 = [time(9,12,23), time(8,11,11)]

if b[0] > time(11,11,11):
    print("no")

