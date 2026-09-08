
'''
        012
1. s = "abc"   s[0]--->a  s[1]--->b  s[2]
input : abc result : zyx

'''
s = input('Enter string : ') # ABC
s = s.lower()# "abc"
al = 'abcdefghijklmnopqrstuvwxyz'
res = ''
for ch in s:
   res = res+al[25-al.index(ch)] # res = z
print(f'for the given string : {s} encryption is : {res}')