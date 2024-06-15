def reverse_string(string):
    stack = []
    reversed_string = ""

    # Push each character onto the stack
    for char in string:
        stack.append(char)

    # Pop characters from the stack to reverse the string
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Get user input
original_string = input("Enter a string: ")

# Reverse the string using the function
reversed_string = reverse_string(original_string)

# Print the reversed string
print("Reversed string:", reversed_string)
