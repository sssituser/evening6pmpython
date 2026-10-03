from typing import final

class A:
    def readnums(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def getnums(self):
        print(f'num1 : {self.num1}\tnum2 : {self.num2}')

class B(A):
    def sum(self):
        print(f'Sum : {self.num1+self.num2}')
    def sub(self):
        print(f'Sub : {self.num1-self.num2}')
class C(B):
    def mul(self):
        print(f'Mul : {self.num1*self.num2}')
    def div(self):
        print(f'Quo : {self.num1/self.num2}')
ob = C()
ob.readnums(5,2)
ob.getnums();
ob.sum()
ob.sub()
ob.mul()
ob.div()