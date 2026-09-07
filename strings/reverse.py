'''
Write a program to find the reverse of a given string
input : abc  result : cba
'''
# s = input('Enter a string : ') # s = "abc"
# res =""
# for i in range(len(s)-1,-1,-1): # for i in range(2,-1,-1)
#     res = res+ s[i]   # res = cba
# print(f'reverse is : {res}')
   
#================================
# s = input('Enter a string : ') # s = "abc"
# res = ''
# for i in range(-1,-len(s)-1,-1):
#     res = res+s[i] # res = cba
# print(f'Revese of the string is : {res}')

#=============================================
s = input('Enter  a string : ')
print(s[::-1])
