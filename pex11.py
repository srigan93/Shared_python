def putNumbers(n):
	i=0
	while i<n:
		i+=1
		return i
	print (i)

for i in putNumbers(50):
    print ('a')


D:\python>py pex11.py
Traceback (most recent call last):
  File "pex11.py", line 8, in <module>
    for i in putNumbers(50):
TypeError: 'int' object is not iterable