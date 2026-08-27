'''
Write a program to generate numbers for the given from 
2 to given number.  

input : 10   numbers : 2 4 6 8 10
input : 15  numbers : 2 4 6 8 10 12 14
'''
start = 2
end = int(input("Enter a number : ")) # end = 20

while start <=  end:
    print(start,end=" ")
    start += 2
