word = input()

password = ''

for i in word:
    if i == 'i':
        password += '1'
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == '-':
        password += '8'
    elif i == 's':
        password += '$'
    else:
        password += i  # Keep the character as is if no replacement rule applies

password += '!'
print(password)
