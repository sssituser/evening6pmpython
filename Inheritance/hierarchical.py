class A:
    def __init__(self):
        self.a = 5
        self.b = 2
    def shownums(self):
        print(f'a = {self.a} b = {self.b}')
        
class B(A):
    def sum(self):
        print(f'Sum : {self.a+self.b}')
        
class C(A):
    def sub(self):
        print(f'Sub :{self.a-self.b}')
class D(A):
    def mul(self):
       print(f'Mul : {self.a*self.b}')
b = B()
b.shownums()
b.sum()

c = C()
c.sub()

d = D()
d.mul()
                    