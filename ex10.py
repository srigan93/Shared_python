a='hello, word'


print(a.strip('hello '))

value=[1,2,3,4,5,6]
doubled_value= [x*2 for x in value]

print ('double vale',doubled_value)


even=[x for x in value if x%2 == 0]
print ("even",even)


odd=[x for x in value if x%2 != 0]
print ("odd",odd)

############ tuble
value_t=(1,2,3,4,5,6)
doubled_value_t= [x*2 for x in value_t]

print ('double vale_t',doubled_value_t)


########### dic

value_d={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six'}
doubled_value_d= [x for x in value_d]

print ('double vale_d',value_d)

print ('double vale_d',value_d.pop(4))

print ('double vale_d',value_d)

print ('double vale_d',value_d)


l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

#print (l)

print (','.join(l))
print ("','".join(l))


