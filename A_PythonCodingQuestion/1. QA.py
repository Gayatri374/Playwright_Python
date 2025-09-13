from collections import Counter
name = "Gayatri"
age = 28

# Take a string input and print its first and last character.
print(name[0])
print(name[-1])

# Check if a string is a palindrome (same forward & backward).
def pali(s):
    return s==s[::-1]
print(pali(name))
# Count how many times "a" appears in "automation".

def fre(a):
    return dict(Counter(a))
print(fre(name))

# Reverse a string without using [::-1]
print(name[::-1])
def reve(c):
    return c[::-1]
print(reve(name))

# Format and print: "The price of {item} is {price}" using f-strings.
item='Book'
price=20


print(f"The price of {item} is {price}")



# Create a list of numbers from 1 to 10 and print only even numbers.
for i in range(1,10):
    if i%2==0:
        print(i,end=' ')
print()
# Write a program to find the maximum and minimum in a list without using max() or min().
num=[1,6,75,45,9,4]

max_num=num[0]
min_num=num[0]

for n in num:
    if n>max_num:
        max_num=n
    if n<min_num:
        min_num=n
print('Maximum Number:',max_num)
print('Minimum Number:',min_num)

# Convert a tuple (1,2,3,4,5) into a list and append 6.
tup=(1,2,3,4,5)
lis=list(tup)
lis.append(6)
tupl=tuple(lis)
print(tupl)

# Sort a list of words ["banana", "apple", "cherry"] in alphabetical order.

fruit=["banana", "apple", "cherry"]
fruit.sort()
print(fruit)


# Create a list comprehension to generate a list of squares of even numbers from 1 to 20.
square_of_even=[n**2 for n in range(1,20) if n%2==0]
print(square_of_even)

# Create a dictionary of 3 students with name as key and marks as value. Print all names.
dict={'abc':10,'def':20,'ghi':30}
print(dict.keys())

# Write a program to merge two dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged={**dict1,**dict2}
print(merged)

# Count frequency of each word in a string using dictionary.
text = "QA Automation with Python Automation QA"


def freq(z):
    words = z.split()          # split string into list of words
    return (Counter(words))

print(freq(text))

# Create a set of numbers 1–10. Remove even numbers from the set.
#
# Perform union, intersection, and difference on sets {1,2,3,4} and {3,4,5,6}.