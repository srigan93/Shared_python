Input1 = ['cut', 'god', 'pass']  
Input2 = ['god', 'cut', 'cut', 'cut','god', 'pass', 'cut', 'pass'] 
Output = [] 
Output_2 = [] 
for y in Input1:
	Output.append(Input1.index(y))
	print ('(Input1.index(y))',Input1.index(y))
	Output.append(Input1.index(y))
print("output-:", Output) 