class Product:
    def __init__(self,pid:int,pname:str,price:float):
        self.pid = pid
        self.pname = pname
        self.price = price
        print("Hi Iam Construcor with Parameter")
    def getprodut(self):
        print('Product Information')
        print(f'Product ID   : {self.pid}')
        print(f'Product Name : {self.pname}')
        print(f'Product Price: {self.price}')
print("=================Product-1 Object================")
p1 = Product(11,"Soap",100)        
p1.getprodut()
print("=================Product-2 Object================")
p2 = Product(12,"ABC",200)        
p2.getprodut()
print("=================Product-3 Object================")
p3 = Product(13,"DEF",300)        
p3.getprodut()
        