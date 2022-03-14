from abstractConstraints import Abstract_Constraints

class Constraints_Type2(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
    
    
    def toString(self):
        try:
            str= self.var1+"="+self.val1+" => "+self.var2+"!="+self.val2
            return str
        except:
            print("all attributes are not assigned")
    
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 5 ):
            print("constraint type is not fit")
            return None
        try:
            self.var1= splitted_line[1].split("=")[0]
            self.val1=splitted_line[1].split("=")[1]
            
            self.var2= splitted_line[4].split("=")[0]
            self.val2=splitted_line[4].split("=")[1]
        except:
            print("line is not fit type2 constraints")
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            return (indexOfVal1%4 == indexOfVal2%4)
        except:
            try:#forward checking
                indexOfVal1=domain.index([self.val1])
                subjectNum = indexOfVal1%4
                variables = list(dataDict.keys())
                n=variables.index(self.var2)
                if([self.var2] in domain[4*n+subjectNum]):
                    domain[4*n+subjectNum].remove(self.var2)
            except:
                try:
                    indexOfVal2=domain.index([self.val2])
                    subjectNum = indexOfVal2%4
                    variables = list(dataDict.keys())
                    n=variables.index(self.var1)
                    if([self.var1] in domain[4*n+subjectNum]):
                        domain[4*n+subjectNum].remove(self.var1)
        
                except:
                    return False
        if([] in domain):
            return True
        return False
"""
x={'years': ['2006', '2007', '2008', '2009'], 'owners': ['Anita', 'Barbara', 'Douglas', 'Fernando'], 'breeds': ['bulldog', 'dalmatian', 'greatDane', 'pekingese'], 'dogs': ['Harley', 'Molly', 'Riley', 'Shadow']}
c=Constraints_Type2()
c.createConstaintsFromLine("if breeds=greatDane then not years=2006")

d=[["2007"],['2006'], ['2008'], ['2009'], ['Anita'], ['Barbara'], ['Douglas'],[ 'Fernando'], ['bulldog'],[ 'greatDane'], [ 'dalmatian'], [ 'pekingese'], [ 'Harley'], [ 'Molly',], ['Riley'], [ 'Shadow']]
print(c.isConstraintViolated(d,x))"""