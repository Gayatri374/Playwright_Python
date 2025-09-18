for num in range(1, 12):
    if num > 1:  # only check for n > 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
print()

for number in range(1,50):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number,end=' ')





# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# # Create object
# a = Animal()
# a.speak()  # Output: Animal speaks
#
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name   # assigning name to object
#         self.age = age     # assigning age to object
#
#     def show(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")
#
# # Create object
# p1 = Person("Gayatri", 28)
# p1.show()