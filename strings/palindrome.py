s = input('Enter a string : ') # s = eye
rev = ''
for i in range(len(s)-1,-1,-1): # range(2,-1,-1) 
    rev += s[i]  # rev = eye
if rev == s:
    print(f'{s} is a Palindrome')
else:
    print(f'{s} is not a Palindrome')
