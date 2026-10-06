class Sample:
    def readvalues(self):
        self.a = int(input("Enter a value : "))
        self.b = int(input("Enter b value : "))
    def showvalues(self):
        print(f'a = {self.a} b = {self.b}')
    def __sub__(x, y):
        res = Sample()
        res.a = x.a-y.a
        res.b = x.b-y.b
        return res
print("==========Object p1=========")
p1 = Sample()
p1.readvalues()
p1.showvalues()      
print("==========Object p2=========")
p2 = Sample()
p2.readvalues()
p2.showvalues()  
print("==========Object p3=========")
p3 = Sample()
p3 = p1-p2
p3.showvalues()      
