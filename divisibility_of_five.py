# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Pseudo Code

# ask user for number of elements they want in the list
number_of_elements = int(input("How many elements do you want in the list? "))
print(number_of_elements)

list = []
# make user input said elements
for i in range(number_of_elements):
    elements = input("Enter your desired element: ")
    list.append(elements)

print(list)
# write the program that only prints numbers in a list that are divisbile by 5
for i in list:
    if int(i) % 5 == 0:
        print(i)

