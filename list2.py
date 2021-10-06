# Creation
a=[12,34,56,67]
a=[]
a=list()
print(a)
a=list("abcedf")
print(a)

# Modifications:

a=[12,34,56,67]
a[0]=90
a[1:3]=[6,7,8,9]
print(a)

a.append(123)
print(a)

a.extend([1,2,3])
print(a)

a.insert(1,999)
print(a)

a.pop(0)
print(a)

a.remove(67)
print(a)

a.reverse()
print(a)

a.sort()
print(a)


