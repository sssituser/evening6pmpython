
class A:
    def readdata(self):
        self.a =int(input("Enter a value : "))
        self.b =int(input("Enter b value : "))
    def getdata(self):
        print(f'a = {self.a}\tb = {self.b}')
class B(A):
    def sum(self):
        print(f'Sum is :{self.a+self.b}')
    def sub(self):
        print(f'Sub is {self.a - self.b}')
class C:
    def show(self):
        print("hi this show method from class C")
    def display(self):
        print("hi this display method from Class C")
class D(B,C):
    def power(self):
        print(f'{self.a} to the power {self.b} : {self.a**self.b}')
    def mul(self):
        print(f'Mul is :{self.a*self.b}')
res = D()
res.readdata()
res.getdata()
res.sum()
res.sub()
res.power()
res.mul()
    