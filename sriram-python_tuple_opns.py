#! /bin/python
''' This program demonstrates the basic operations that can be performed by using python. Here the variables used are global and the scope 
is limited to through out the program'''
#Tuple_Operations
Tuple1=()       #creates an empty tuple
Tuple1="beasant","Python","Programming"
print (Tuple1)  #print the values contained in tuple
Tuple2=("we","are","into","code")
print (Tuple1+Tuple2)   # valid in python just like list
print (Tuple1,Tuple2)   # this will create a nested list
print (Tuple1 * 4)      #mutes multiplication, valid in python
Tuple1[0] = 4           # This line is invalid, Tuples cannot be muted.( we cant change the value of tuples like this
print (Tuple1)
del(Tuple1[1])          #This is also invalid Tuple elements cannot be deleted.

''' Compare, min and max function usage in Tuples'''
if cmp(Tuple1, Tuple2) != 0: 
  print('Not the same') 
else: 
  print('Same') 
print ('Maximum element in tuples 1,2: ' + 
        str(max(Tuple1)) +  ',' + 
        str(max(Tuple2))) 
print ('Minimum element in tuples 1,2: ' + 
     str(min(Tuple1)) + ','  + str(min(Tuple2)))
