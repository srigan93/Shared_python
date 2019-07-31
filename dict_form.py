'''Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

Solution:


n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print (d)'''

values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)