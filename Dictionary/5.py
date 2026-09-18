d = {12:"jashwanth",23:"Alekhya",24:"Lahari",45:"ShivaRam",44:"yasahwini"}
print("=========Key value Pairs============")
for trisha in d.items():
    print(trisha)
    
d.setdefault(88,"vishnavy")
print("=========Key value Pairs============")
for trisha in d.items():
    print(trisha)
print(f"Key-Value pair Count : {d.__len__()} =>{len(d)}")
print(f'Delete Item is :{d.popitem()}')

k = int(input('Enter Key : '))
print(f'{k} and its value : {d.get(k)}')
print(f'{k} value is : {d[k]} ')
