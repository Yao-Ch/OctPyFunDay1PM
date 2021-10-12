
text="abcdef"

text=text.capitalize()
print(text)

text=text.upper()
print(text)

text="----Hello-----"
text=text.strip("-")
print(text)

line="123;456;567;788;788"
result=line.split(";")
print(result)

line="123  456     567    788      788"
result=line.split()
print(result, type(result))

line2=",".join(result)
print(line2, type(line2))

# newresult=[int(e) for e in result] # a list comprehension
# print(newresult)

line3=line2.replace(',', '/')
print(line3)







