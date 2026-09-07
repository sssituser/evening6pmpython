'''
Write a program to check given string is palindrome or not
'''
s = input('Enter a string : ')
if s == s[::-1]:
    print(f'{s} is a Palindrome String')
else:
    print(f'{s} is not a Palindrome string')