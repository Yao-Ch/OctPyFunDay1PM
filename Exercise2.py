'''
Exercise 2 (ExercisePy1.pdf)
    
Step 1: Write a Python script that prompts the user for several numbers 
(when the user enter the string "stop", the script stop asking for numbers).
The numbers entered are stored into a list one after the other.

Step 2: After having retrieved all the numbers, print the list.

Step 3: The script will then compute and print the minimum, the maximum and the 
mean of the different numbers present in the list.
Take into account the situation where the list is empty.

Step 4: Compute the "truncated mean" of the elements: 
the mean of all elements except the smallest and largest ones.
    [3,4,3,6,77,3,77,55]
    =>
    [3,3,3,4,6,55,77,77]
    =>
    [4,6,55] then compute the mean
'''


# # A way to remove all elements with a given value

# d=[23,45,23,56,23,78]

# elt=23
# while elt in d:
#     d.remove(elt)

# print(d)

# # 2 ways to access all list elements via their positions:
# d=[23,45,23,56,23,78]
# # Using a while loop:
# ix=0
# while ix < len(d):
#     print(f"{ix} -> {d[ix]}")
#     ix += 1
    
# # Using a for loop and the range() function:   
# for ix in range(len(d)):
#     print(f"{ix} -> {d[ix]}")
    

numbers=[]   # Creation of an empty list <=> numbers=list()

# Step 1:
while True:
    answer=input("Enter an int or 'stop': ")
    if answer=='stop':
        break
    else:
        answer=int(answer)
        numbers.append(answer)
        # or numbers.append(int(answer))
        
# Step 2:
print(f"Here is the constructed list: {numbers} it's size is {len(numbers)}")

# Step 3:

if len(numbers) > 0: # If the list numbers is not empty
    
    mini=numbers[0] 
    maxi=numbers[0]
    total=numbers[0]
    # mini=maxi=total=numbers[0]
    for e in numbers[1:]:
        if e < mini:
            mini=e
        if e > maxi:
            maxi=e
        total+=e
        
    print(f"Minimum: {mini} Maximum: {maxi}")    
    print(f"Mean: {total/len(numbers)}")
else:
    print("The list is empty")    
    
if len(numbers) > 0:
    print(f"Minimum: {min(numbers)} Maximum: {max(numbers)}")    
    print(f"Mean: {sum(numbers)/len(numbers)}")
    # or
    import statistics
    print(f"Mean: {statistics.mean(numbers)}")
    
else:
    print("The list is empty")

# Step 4:
if len(numbers) > 0:
    # [3,4,3,6,77,3,77,55]
    org=numbers.copy() # <=> org=numbers[:]
    numbers.sort() # inplace
    # [3,3,3,4,6,55,77,77]
    miniCount=numbers.count(numbers[0])
    maxiCount=numbers.count(numbers[-1])
    print(numbers)
    subList=numbers[miniCount:-maxiCount]
    print(subList)
    if len(subList) != 0:
        print(f"Truncated mean is {sum(subList)/len(subList)}")   
else:
    print("The list is empty")  