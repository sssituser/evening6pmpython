num = 14569
div = 10000
while num!=0:
    d = num//div # d = 1 d = 53//10 d = 5 d = 3//1
    print(d,end=" ")
    num = num%div # num = 53%10 num = 3%1
    div = div//10
    
    
