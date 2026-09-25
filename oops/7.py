class Cricket:
    totalscore = 0
     # static variable or class variable
    def setplayerinfo(self,pname,runscored):    
        print(f'Total Runs : {Cricket.totalscore}')# 0
        self.pname=pname
        self.runscored = runscored 
        Cricket.totalscore = Cricket.totalscore+runscored # 30
    def getplayerinfo(self):
        print(f"Total Score : Runs : {Cricket.totalscore}") # 50
        print(f'Player Name {self.pname}: Runs : {self.runscored}') #50
print("======================Player-1(kholi) Object===================")        
p1 = Cricket() 
p1.setplayerinfo("kholi",50)
p1.getplayerinfo()
print("======================Player-2(Rohit) Object===================")        
p2 = Cricket() 
p2.setplayerinfo("Rohit",30)
p2.getplayerinfo()

