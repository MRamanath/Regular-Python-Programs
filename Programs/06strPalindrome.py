# Check string palindrome

def palindrome(str):
    rev = str[::-1]
    if str == rev:
        print('Palindrome')
    else:
        print('Not palindrome')

if __name__ == '__main__':
    userInput = input('Enter a string : ')
    palindrome(userInput)


# Enter a string : madam
# Palindrome