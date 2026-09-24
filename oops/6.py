class Home:
    
    def showbal(self):
        self.amount = 10000 # self.amount is non static variable
        print(f'Amount is : {self.amount}')
    def spent(self,samount):
        self.amount = self.amount-samount
        print(f'Spent Amount is : {samount} Balance is : {self.amount}')
        
print("=======Bother-1 Object===========")        
br1 = Home()
br1.showbal() # Amount is : 10000
br1.spent(3000)# 3000, 7000



print("=======Bother-2 Object===========")        
br2 = Home()
br2.showbal()# Amount is : 10000
br2.spent(2000) #       Bal:8000

print("=======Bother-3 Object===========")        
br3 = Home()
br3.showbal() # Amount : 5000
br3.spent(1000)
