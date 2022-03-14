from abstractConstraints import Abstract_Constraints

class Constraints_Type10(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None,var3=None,val3=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.var3=var3
        self.val3=val3 
    
    def toString(self):
        try:
            str= "("+self.var1+"="+self.val1+") != ("+self.var2+"="+self.val2+") != (" + self.var3+"="+self.val3 +")"
            return str
        except:
            print("all attributes are not assigned")
    
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 4 ):
            print("constraint type is not fit")
            return None
        try:
            temp=splitted_line[0]
            temp=temp[1:-1] #cut { and }
            temp = temp.split(",")
            self.var1,self.val1=temp[0].split("=")
            self.var2,self.val2=temp[1].split("=")
            self.var3,self.val3=temp[2].split("=")
        except:
            print("line is not fit type 5 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        firstAssigned,secondAssigned,thirdAssigned = False,False,False
        variables=list(dataDict.keys())
        try:
            indexOfVal1=domain.index([self.val1])
            firstAssigned = True
            subjectNum1=indexOfVal1%4
        except:
            indexOfVal1=False
        try:
            indexOfVal2=domain.index([self.val2])
            secondAssigned =True
            subjectNum2=indexOfVal2%4
        except:
            indexOfVal2=False
        try:
            indexOfVal3=domain.index([self.val3])
            thirdAssigned=True
            subjectNum3=indexOfVal3%4
        except:
            indexOfVal3=False
            
        if(firstAssigned and secondAssigned):
            if(subjectNum1 == subjectNum2):
                return True
            n=variables.index(self.var3)
            if(self.val3 in domain[4*n+subjectNum1]):
                domain[4*n+subjectNum1].remove(self.val3)
            if(self.val3 in domain[4*n+subjectNum2]):
                domain[4*n+subjectNum2].remove(self.val3)
        if(firstAssigned and thirdAssigned):
            if(subjectNum1 == subjectNum3):
                return True
            n=variables.index(self.var2)
            if(self.val2 in domain[4*n+subjectNum1]):
                domain[4*n+subjectNum1].remove(self.val2)
            if(self.val2 in domain[4*n+subjectNum3]):
                domain[4*n+subjectNum3].remove(self.val2)    
        if(secondAssigned and thirdAssigned):
            if(subjectNum2 == subjectNum3):
                return True
            n=variables.index(self.var1)
            if(self.val1 in domain[4*n+subjectNum2]):
                domain[4*n+subjectNum2].remove(self.val1)
            if(self.val1 in domain[4*n+subjectNum3]):
                domain[4*n+subjectNum3].remove(self.val1)
            
        if([] in domain):
            return True
        return False
"""c=Constraints_Type10()
c.createConstaintsFromLine("{year=2007,owners=Anita,breeds=bulldog} are all different")
print(c.toString())
x={'years': ['2006', '2007', '2008', '2009'], 'owners': ['Anita', 'Barbara', 'Douglas', 'Fernando'], 'breeds': ['bulldog', 'dalmatian', 'greatDane', 'pekingese'], 'dogs': ['Harley', 'Molly', 'Riley', 'Shadow']}


d=[["2006"],['2007'], ['2008'], ['2009'], ['Anita'], ['Douglas'], ['Barbara'],[ 'Fernando'], [ 'dalmatian'], [ 'pekingese'],['bulldog'],[ 'greatDane'], [ 'Harley'], ['Riley'],[ 'Molly'], [ 'Shadow']]
print(c.isConstraintViolated(d,x))"""