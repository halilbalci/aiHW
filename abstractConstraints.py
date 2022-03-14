from abc import ABC
  
class Abstract_Constraints(ABC): 
    
    # abstract method 
    def toString(self): 
        pass
    
    def createConstaintsFromLine(self,line):
        pass
    
    def isConstraintViolated(self,domain,dataDict):
        pass