def my_function(a):
	m=1
	for i in range(a):
		n=i+1
		m=m*n
		
		print('fact',m)
num=int(input('enter the value'))
my_function(num)