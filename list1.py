
a=[12,34,56,67]

b=a # .copy() is a method

print(a, b)

b[0]=100

print(a, b)

nb1=100
print(nb1, id(nb1))
nb2=nb1
print(nb2, id(nb2))


nb1=nb1+1
print(nb1, id(nb1))

print(nb2, id(nb2))


