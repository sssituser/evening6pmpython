class BasicCalcy:
    def sum(self,a,b):
        print(f'Sum : {a+b}')
    def sub(self,a,b):
        print(f'Sub : {a-b}')
    def mul(self,a,b):
        print(f'Mul : {a*b}')
    def div(self,a,b):
        print(f'Quo : {a/b}')
import math
class SciCalcy(BasicCalcy):
    def sine(self,val):
        print(f'Sine {val} is :{math.sin(val)}')
    def cos(self,val):
        print(f'Cos {val} is : {math.cos(val)}')
p = SciCalcy()
p.sine(90)
p.cos(0)
p.sum(5,2)
p.sub(5,3)