# Addition

# input() always returns string
a = input("Enter first number: ")
b = input("Enter second number: ")

# Convert to float (or int)
a = float(a)
b = float(b)

# Perform addition
result = a + b
print("Sum is:", result)


# Average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

average = (a + b) / 2
print("Average is:", average)


# Multiple Operation
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)

# Avoid division by zero
if y != 0:
    print("Division:", x / y)
else:
    print("Division not possible (y is zero)")