'''
Write a program to generate list of odd number from the given
range
'''
# oddnums =[x for x in range(20,70) if x%2!=0]
# print(oddnums)

# squares =[x*x for x in range(1,21)]
# print(squares)

name = input('Enter a nume : ')
vowels=[x for x in name if x in 'aeiou']
print(vowels)
cons = [x for x in name if x not in 'aeiou']
print(cons)