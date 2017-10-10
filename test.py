# -*- coding: utf-8 -*-
import random

arr = [random.randint(0,5) for x in range(50)]

print (arr)

start = 0
end = 0

for i in range(1, len(arr)):
    if arr[i]!=arr[start]:
        if end-start>=1:
            number = arr[start]
            size = end-start+1
            print('{} повторяется {} раза'.format(number, size))
        start = i
        end = i
    else:
        end = i
        if i == len(arr)-1:
            if end-start>=1:
                number = arr[start]
                size = end-start+1
                print('{} повторяется {} раза'.format(number, size))