from abstractConstraints import Abstract_Constraints

class Constraints_Type1(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
    
    
    def toString(self):
        try:
            str= self.var1+"="+self.val1+" => "+self.var2+"="+self.val2
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
            self.var1= splitted_line[1].split("=")[0]
            self.val1=splitted_line[1].split("=")[1]
            
            self.var2= splitted_line[3].split("=")[0]
            self.val2=splitted_line[3].split("=")[1]
        except:
            print("line is not fit type1 constraints")

    def isConstraintViolated(self,domain,dataDict):
        if([] in domain):
            return True
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            return (indexOfVal1%4 != indexOfVal2%4)
        except:
            #forward checking
            try:
                indexOfVal1=domain.index([self.val1])
                subjectNum = indexOfVal1%4
                variables = list(dataDict.keys())
                n=variables.index(self.var2)
                domain[4*n+subjectNum]=[self.val2]
                for i in range(4*n,4*n+4):
                    if(i%4 != subjectNum ):
                        if(self.val2 in domain[i]):
                            domain[i].remove(self.val2)
            except:
                try:
                    indexOfVal2=domain.index([self.val2])
                    subjectNum = indexOfVal2%4
                    variables = list(dataDict.keys())
                    n=variables.index(self.var1)
                    domain[4*n+subjectNum]=[self.val1]
                    for i in range(4*n,4*n+4):
                        if(i%4 != subjectNum ):
                            if(self.val1 in domain[i]):
                                domain[i].remove(self.val1)
                except:
                    return False
        
"""
x={'years': ['2006', '2007', '2008', '2009'], 'owners': ['Anita', 'Barbara', 'Douglas', 'Fernando'], 'breeds': ['bulldog', 'dalmatian', 'greatDane', 'pekingese'], 'dogs': ['Harley', 'Molly', 'Riley', 'Shadow']}
c=Constraints_Type1()
c.createConstaintsFromLine("if breeds=greatDane then years=2006")

d=[["2007"],['2006'], ['2008'], ['2009'], ['Anita'], ['Barbara'], ['Douglas'],[ 'Fernando'], ['bulldog'],[ 'greatDane'], [ 'dalmatian'], [ 'pekingese'], [ 'Harley'], [ 'Molly',], ['Riley'], [ 'Shadow']]
print(c.isConstraintViolated(d,x))
"""