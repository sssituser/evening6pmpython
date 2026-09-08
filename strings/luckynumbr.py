'''
Write a program to find the luckynumber for the
given date of birth  "11-Oct-2020"
Ex: 11+10+2020=>2041=>2+0+4+1=> 7 is the lucky number
'''
dob = input('Enter Dob : ')
li = dob.split('-')
date =int(li[0])
year = int(li[2])
month = li[1].lower()
monnum = 0
months =['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
for i in range(len(months)):
    if month.__contains__(months[i]):
        monnum = i+1
sum = date+monnum+year
while(sum>9): # 2041
    num = sum
    lopsum = 0
    while(num>0): #2044>0
        digit = num%10
        lopsum += digit
        num=num//10
    sum = lopsum 
print(f'Your Lucky Number is : {sum}')
    
        