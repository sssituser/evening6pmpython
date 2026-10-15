fname = input("Enter File Name : ")
file = open(fname,'a')
info  = input("Enter Your Info to append : ")
while info != "":
    file.write(info)
    info=input()
file.close()