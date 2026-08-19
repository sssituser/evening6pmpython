temp = int(input('Enter Room Temp : ')) # 17  20 24 22
if temp>19: # 20>19-T 24>19-T 22>19-T
    if temp<23: # 20<23-T 24<23-F 22<23
        print('Room is in Normal Temp')
    else:
        print('Room is in Hot Temp') 
else:
    print('Room is Cool')