fname = input('Enter File Name with Location : ')
file = open(fname,'a+')
info = input('Enter Info  : ')
while info!= "":
    file.write(info)
    info = input()
    