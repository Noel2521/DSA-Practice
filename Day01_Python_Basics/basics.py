# name = "Noel"
# age = 25
# score = 9.5
# is_ready = True

# print(type(age))

# print(type(name))
# print(type(score))
# print(type(is_ready))


# numbers = [10,20,30,40,50]

# print(numbers[0])      # First item — indexing starts at 0
# print(numbers[-1])     # Last item — negative index goes from the end
# print(len(numbers))    # How many items are in the list


# numbers = [10,20,30,40,50]
# for num in numbers:
#     print(num)

# for i in range(5):
#     print (i)

# for i in range(1,6):
#     print(i)

# def greet(name):
#     return "Hello " + name

# print(greet("Noel"))

# def add_numbers(a,b):
#     return a + b
# print(add_numbers(5,10))

# numbers = [1, 2, 3, 4, 5]
# squared = []
# for n in numbers:
#     squared.append(n * n)
# print(squared)

numbers = [1, 2, 3, 4, 5]
squared = [n * n for n in numbers]
print(squared)