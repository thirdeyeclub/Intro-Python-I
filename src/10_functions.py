# Write a function is_even that will return true if the passed-in number is even.

def suit(x):
    return x % 2 ==0

# Read a number from the keyboard
num = input("Enter A #")

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if suit(num):
    print("Even!")
else:
    print("This is Odd")

