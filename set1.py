# Creation

s1={23,45,67,45,10}
print(s1, len(s1), type(s1))

for e in s1:
    print(e)


data=[56,67,78,67,54,78]
s2=set(data)
print(s2)


s1={45,67,78,89}
s2={67,89,100,200}

s3=s1.union(s2)
print(s3)
s3=s1.intersection(s2)
print(s3)