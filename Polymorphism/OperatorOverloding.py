'''
Assigning  a new property for the operator is called
operator overloading.

+  can be used add integer, float values, complex nums, strings

In order overload the operator we need respective magical methods

+   __add__
-   __sub_


'''

class Test:
    def readvalues(self,a,b):
        self.a = a
        self.b = b
    def getvalues(self):
        print(f'a = {self.a}\tb = {self.b}')
    def __add__(x, y):
        res = Test()
        res.a = x.a+y.a
        res.b = x.b+y.b
        return res
print("=========Object t1========")
t1 = Test()
t1.readvalues(4,5)
t1.getvalues()

print("=========Object t2========")
t2 = Test()
t2.readvalues(2,3)
t2.getvalues()
print("=========Object t3========")
t3 = Test()
t3 = t1+t2
t3.getvalues()
