def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 2)

x=int(input())

a= (fact(x))

print(a)