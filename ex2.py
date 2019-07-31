def convert_binary(n):
	if n > 1:
		convert_binary(n//2)
	print(n %2 ,end=' ')
dec=4

convert_binary(dec)

