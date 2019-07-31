#!/usr/bin/env python

'''
values = []
for i in range(1000, 3001):
	s = str(i)
	if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
	#if (int(i) %2 == 0 ):
		values.append(s)
#print (",".join(values))

print(values) '''

'''

value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))
'''


'''

s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))
'''



'''import math
c=50
h=20
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ('|'.join(value))
print(value)
'''
i
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]

print(dimensions)
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]


print('#############################')
print(multilist[0])
print(multilist[1])
print(multilist[2])

print('############################# 0,0')
print(multilist[0],[0])
print(multilist[0],[1])
print(multilist[0],[2])
print(multilist[0],[3])

print('############################# 1,0')
print(multilist[1],[0])
print(multilist[1],[1])
print(multilist[1],[2])
print(multilist[1],[3])
print('#############################')




for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist[0])
print(multilist[1])
print(multilist[2])
		
print (multilist)

print('############################# 0,0')
print(multilist[0],[0])
print(multilist[0],[1])
print(multilist[0],[2])
print(multilist[0],[3])

print('############################# 1,0')
print(multilist[1],[0])
print(multilist[1],[1])
print(multilist[1],[2])
print(multilist[1],[3])
print('#############################')

print(multilist[2],[2])
'''
a="without,hello,bag,world
Then, the output should be:
bag,hello,without,world


items=[x for x  input().split(',')]
items.sort()

print(items)

'''


'''


lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print (sentence)
	
	
print(lines)	

'''