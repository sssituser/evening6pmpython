import threading
import time

class Test:
    def __init__(self,name):
        self.name = name
    def play(self):
        for i in range(1,11):
            print(f'{self.name} Played {i} Time')
            time.sleep(3)
            
p1  = Test("Kohili")
p2 = Test("Rohit")

# unstarted state  
t1 =threading.Thread(target=p1.play,name='Thread-1')# Thread creation
t2 = threading.Thread(target=p2.play,name="Thread-2")
# Ready state of thread
t1.start() # Thread scheduler
t2.start()
