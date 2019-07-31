
Output = [] 
Output_dict = {}

for y in range(5):
	Output.append(y)
	print(Output)
	Output_dict={'key1':y}
	print('Output_dict',Output_dict)

print("output-:", Output) 

dict1={1:'one',2:'two',3:'three'}
print(dict1)
print('dict-1-',dict1.get(1))
print('dict-2-',dict1.get(2))