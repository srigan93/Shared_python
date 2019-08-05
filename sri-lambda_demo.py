#!/bin/python
''' A demo for lambda filter and map method in python'''
double = lambda x: x * 2 ''' the operation x *2 will be saved in x'''
print(double(5))

add = lambda x,y:x+y# two arguments
print(add(5,10))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
