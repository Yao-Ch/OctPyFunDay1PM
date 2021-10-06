
"""
Container or collections:
        list tuple str bytes set dict ....
        Sequences:
            list tuple str bytes ...
            
Collections:           
len(): size of a collection
for loop: to iterate through a collection
in: to test if an element is present in a collection or not

Sequences:
[]: to access an element
[:]: to access several elements
+: concatenate

"""

name="Peter"
print(len(name))
name=[56,78,89,56,"abc", False]
print(len(name))

nb=89
if nb in name:
    print("Is present")
    
nb="t"
name="Peter"
if nb in name:
    print("Is present")
    
name=[56,78,89,56,"atc", False, "ete"]    
if nb in name:
    print( "is present in name")
    
for element in name:
    #print(element)
    if isinstance(element, str):
        if "t" in element:
            print(f"The string {element} contains t")
    
    
    
    
    
    
    