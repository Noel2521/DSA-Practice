# name = "Noel"

# print(name[0])   # First character
# print(name[-1])  # Last character
# print(len(name)) # How many characters

name = "Noel Anthony"

print(name[0:4])   # Extract first 4 characters
print(name[5:12])  # Extract from index 5 to 11
print(name[:4])    # From beginning to index 3
print(name[5:])    # From index 5 to the end

name = "noel anthony"

print(name.upper())        # Convert to uppercase
print(name.lower())        # Convert to lowercase
print(name.replace("noel", "john"))  # Replace a word
print(name.split(" "))     # Split into a list by space


#Arrays
numbers = [3,1,4,1,5,9,2,6]

print(numbers[0])
print(len(numbers))
numbers.append(7)
print(numbers)
numbers.sort()
print(numbers)
print(numbers[0])
print(numbers[-1])


def find_max(numbers):
    numbers.sort()
    return numbers[-1]
print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))


def find_min(numbers):
    numbers.sort()
    return numbers[0]
print(find_min([3, 1, 4, 1, 5, 9, 2, 6]))