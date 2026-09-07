'''
Write a program to find the namescore of a given name.
input : "abcd"  Result : 1+2+3+4=> 10 NameScore = 10


Solution :
name = "raj"
res = "abcdefghijklmnopqrstuvwxyz"

'''

name = input('Enter Name : ') # name = "abc"
sum = 0
alphas = "abcdefghijklmnopqrstuvwxyz"
name = name.lower()
for ch in name: # "abc"
   sum = sum+alphas.index(ch)+1 # sum = 3
print(f'Score of given name : {sum}')
