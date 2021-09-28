import random 

class GVDie:  
   def __init__(self):      
      self.myValue = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.myValue = self.rand.randint(1, 6)  
      
   def setSeed(self, seed):
       self.rand.seed(seed)
   
   def compareTo(self, other):
       return self.myValue - d.myValue
       