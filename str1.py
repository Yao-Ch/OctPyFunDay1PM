
text="abcdef"
text='abcdef'
text="a large large\
string"
print(text)

text="""a large large
large
string"""
print(text)

text='''a large large
    large
string'''
print(text)

text=str(123)
print(text, len(text))

nb=12

text=f"nb is {nb} nb ** 2 is {nb**2}"
print(text)

nb=10/3
name="Pierre"
text=f"name is {name[:3]:>10s} nb is {nb:.2f} nb ** 2 is {nb**2:.2f}"
print(text)

text="line1\n\n\tline2"
print(text)

path="c:\temp\new.txt"
print(path)

path="c:\\temp\\new.txt"
print(path)

path= r"c:\temp\new.txt" # a raw string
print(path)

path="c:/temp/new.txt" 
print(path)










