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
t1 =threading.Thread(target=p1.play,name='Thread-1')
t2 = threading.Thread(target=p2.play,name="Thread-2")
# Unstarted state
# Thread creation
# Ready state of Thread
# Thread Scheduler
t1.start() 
t2.start()
