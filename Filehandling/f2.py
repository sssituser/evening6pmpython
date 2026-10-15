# fname=input("Enter File Name : ")
# file = open(fname,'x')

fname = input("Enter File Name : ")
file = open(fname,"w")
info = input('Enter Your information : ')
file.write(info)
file.close()