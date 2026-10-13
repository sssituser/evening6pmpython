import threading
import time
class Game:
    def __init__(self,name):
        self.name = name
    def play(self):
        for i in range(1,11):
            print(f'{self.name} Played {i} time')
            time.sleep(4)
p1 = Game("virat")
p2 = Game("Rohit")
p3 = Game("Raj")
# Unstarted state
t1 = threading.Thread(target=p1.play,name="Thread-1")
t2 = threading.Thread(target=p2.play,name="Thread-2")
t3 = threading.Thread(target=p3.play,name="Thread-3")
#Ready State

t1.start()
t2.start()
t2.join(10)
t3.start()

            