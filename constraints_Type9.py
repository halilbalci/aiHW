from abstractConstraints import Abstract_Constraints

class Constraints_Type9(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None,var3=None,val3=None,var4=None,val4=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.var3=var3
        self.val3=val3 
        self.var4=var4
        self.val4=val4
    
    def toString(self):
        try:
            str= "("+self.var1+"="+self.val1+") = ("+self.var3+"="+self.val3+") xor (" + self.var4+"="+self.val4 +") \n("+self.var2+"="+self.val2+") = ("+self.var3+"="+self.val3+") xor (" + self.var4+"="+self.val4 +")"
            return str
        except:
            print("all attributes are not assigned")
    
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 8 ):
            print("constraint type is not fit")
            return None
        try:
            temp=splitted_line[2]
            temp=temp[1:-1]
            temp=temp.split(",")
            self.var1,self.val1=temp[0].split("=")
            self.var2,self.val2=temp[1].split("=")
            self.var3,self.val3=splitted_line[5].split("=")
            self.var4,self.val4=splitted_line[7].split("=")
        except:
            print("line is not fit type 5 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            indexOfVal3=domain.index([self.val3])
            indexOfVal4=domain.index([self.val4])
            #print("indexOfVal1=",indexOfVal1)
            #print("indexOfVal2=",indexOfVal2)
            #print("indexOfVal3=",indexOfVal3)
            #print("indexOfVal4=",indexOfVal4)
        except:
            return False
        
        if((indexOfVal1%4 != indexOfVal3%4) and (indexOfVal1%4 != indexOfVal4%4)): # 1 and 3 same subject or 1 and 4 same subject
            return True
        if((indexOfVal2%4 != indexOfVal3%4) and (indexOfVal2%4 != indexOfVal4%4)): #(2and 3) or (2 and 4) same subject
            return True
        if(indexOfVal1%4 == indexOfVal2%4):
            return True
        return False

