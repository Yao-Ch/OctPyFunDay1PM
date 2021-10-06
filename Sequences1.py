
"""
Container or collections:
        list tuple str bytes set dict ....
Sequences:
        list tuple str bytes ...
            
Collections:           
    len(): size of a collection
    for loop: to iterate through a collection
    in: to test if an element is present in a collection or not
    ...

Sequences:
    Collections 
            +
    []: to access an element
    [:]: to access several elements
    +: concatenate
    ...

"""

data=[56,78,89,56,"atc", False, "ete"]    
text="Hello World"

# Access to a single element:

print(data[0])
print(data[4])
print(data[-1])
print(data[-2])
data[0]=900
print(data)
print("char t:",data[4][1])

print(text[0])
print(text[4])
print(text[-1])
print(text[-2])
# text[0]="T" # Wrong because a str is "immutable"

# Access to several elements (slice )
print(data[1:4])
print(data[2:])
print(data[:5])
print(data[:])
print(data[1:6:2])
print(data[::-1])
print(data[-6:-3])

data[0:4]=[1000,2000]
print(data)

# + operator
name="world"
ext=".gif"
filename=name + ext
print(filename)

l1=[5,6,7]
l2=[8,1,2,10]
l3=l1+l2
print(l3)

# * operator

line="*-" * 30
print(line)

data=[0] * 10
print(data)

data=[2,3,4,5,6]
data=[e*10 for e in data]
print(data)

    
    
    
    
    
    
    