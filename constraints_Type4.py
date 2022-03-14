from abstractConstraints import Abstract_Constraints

class Constraints_Type4(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
    
    
    def toString(self):
        try:
            str= self.func+"("+self.var1+"="+self.val1+") = "+self.func + "("+self.var2+"="+self.val2+")"
            return str
        except:
            print("all attributes are not assigned")
    
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 3 ):
            print("constraint type is not fit")
            return None
        try:
            first_func,last_func = splitted_line[0],splitted_line[2]
            temp=first_func.split("(")
            self.func=temp[0]
            temp =temp[1].split("=")
            self.var1=temp[0]
            self.val1=temp[1].split(")")[0]
            
            temp=last_func.split("(")
            if(temp[0]!= self.func):
                print("first and last functions are different")
                return None
            temp =temp[1].split("=")
            self.var2=temp[0]
            self.val2=temp[1].split(")")[0]


        except:
            print("line is not fit type 4 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            return not(indexOfVal1%4==indexOfVal2%4)
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
c=Constraints_Type4()
c.createConstaintsFromLine("years(dogs=Molly) = years(breeds=pekingese)")
print(c.toString())

x={'years': ['2006', '2007', '2008', '2009'], 'owners': ['Anita', 'Barbara', 'Douglas', 'Fernando'], 'breeds': ['bulldog', 'dalmatian', 'greatDane', 'pekingese'], 'dogs': ['Harley', 'Molly', 'Riley', 'Shadow']}


d=[["2007"],['2006'], ['2008'], ['2009'], ['Anita'], ['Douglas'], ['Barbara'],[ 'Fernando'], [ 'dalmatian'], [ 'pekingese'],['bulldog'],[ 'greatDane'], [ 'Harley'], ['Riley'],[ 'Molly'], [ 'Shadow']]
print(c.isConstraintViolated(d,x))
"""