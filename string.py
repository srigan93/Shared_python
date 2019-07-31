#The strip() method removes any whitespace from the beginning or the end:
'''
a = " Hello, World!          "

print(len(a))
print(a.strip()) # returns "Hello, World!" -->  its not woriking, need to check with him

print(len(a))

print(a.lower())
print(a.upper())




a = "Hello, World!"
print(a.replace("H", "J"))



#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"

a="Hello |Gopal |sangeetha |pooran |tamizhni"
print(a.split("|")) # returns ['Hello', ' World!']

c=a.split("|")

for i in c:

	print(i)


	
age = 36
txt = "My name is John, I am " + str(age)
print(txt)



age = 37
txt = "My name is John, and I am {}"
print(txt.format(age))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = "Gopal"
price = 49.95
myorder = 'I want {}

 pieces of item %s for %f dollars'
print(myorder.format(quantity, itemno, price))



'''

a = "Hello, World!"
print(a[0:5])


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity, itemno, price))

