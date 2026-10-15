
fname = input("Enter File Name : ")
f = open(fname,'w')
info = input("Enter Your Informtion : ")

while info !="":
    f.writelines(info)
    info = input()
f.close()
