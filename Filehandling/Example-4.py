fname = input('Enter File Name : ')
file = open(fname,'r+')
print("=======Information inside the file is =============")
print(file.read())
