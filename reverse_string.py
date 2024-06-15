def reverse_string(string):
    stack = []
    reversed_string = ""

    # Push each character of the string onto the stack
    for char in string:
        stack.append(char)

    # Pop each character from the stack to build the reversed string
    while stack:
        reversed_string += stack.pop()

    return reversed_string

original_string = "abcde"
reversed_string = reverse_string(original_string)
print(reversed_string)
