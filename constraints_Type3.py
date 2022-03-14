from abstractConstraints import Abstract_Constraints

class Constraints_Type3(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None,var3=None,val3=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.var3=var3
        self.val3=val3
    
    
    def toString(self):
        try:
            str= self.var1+"="+self.val1+" => ("+self.var2+"="+self.val2+" or "+self.var3+"="+self.val3+")"
            return str
        except:
            print("all attributes are not assigned")
    
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 7 ):
            print("constraint type is not fit")
            return None
        try:
            self.var1= splitted_line[1].split("=")[0]
            self.val1=splitted_line[1].split("=")[1]
            
            self.var2= splitted_line[4].split("=")[0]
            self.val2=splitted_line[4].split("=")[1]
            
            self.var3= splitted_line[6].split("=")[0]
            self.val3=splitted_line[6].split("=")[1]
        except:
            print("line is not fit type 3 constraints")
    def isConstraintViolated(self,domain,dataDict):
        isViolated=True
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            indexOfVal3=domain.index([self.val3])
            #print("indexOfVal1=",indexOfVal1)
            #print("indexOfVal2=",indexOfVal2)
            #print("indexOfVal3=",indexOfVal3)
        except:
            return False
        
        if((indexOfVal1%4 == indexOfVal2%4) or (indexOfVal1%4 == indexOfVal3%4)):
            isViolated = False
        if(indexOfVal1%4 == indexOfVal2%4):
            if(indexOfVal2%4 == indexOfVal3%4):
                return True
        return isViolated
"""
c=Constraints_Type3()
c.createConstaintsFromLine("if dogs=Riley then either owners=Douglas or breeds=bulldog")
print(c.toString())

x={'years': ['2006', '2007', '2008', '2009'], 'owners': ['Anita', 'Barbara', 'Douglas', 'Fernando'], 'breeds': ['bulldog', 'dalmatian', 'greatDane', 'pekingese'], 'dogs': ['Harley', 'Molly', 'Riley', 'Shadow']}


d=[["2007"],['2006'], ['2008'], ['2009'], ['Anita'], ['Douxglas'], ['Barbara'],[ 'Fernando'], [ 'dalmatian'],['bulldog'], [ 'pekingese'],[ 'greatDane'], [ 'Harley'], [ 'Molly',], ['Riley'], [ 'Shadow']]
print(c.isConstraintViolated(d,x))"""