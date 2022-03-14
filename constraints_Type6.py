from abstractConstraints import Abstract_Constraints

class Constraints_Type6(Abstract_Constraints):
    
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None,n=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
        self.n=n #string
    
    def toString(self):
        try:
            str= self.func+"("+self.var1+"="+self.val1+") = "+self.func + "("+self.var2+"="+self.val2+")-"+self.n
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
            first_func,last_func,self.n = splitted_line[0],splitted_line[2],splitted_line[4]#n is assigned string
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
            print("line is not fit type 5 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            variables= list(dataDict.keys())
            x=variables.index(self.func)
            if((len(domain[4*x+(indexOfVal1%4)])==1) and (len(domain[4*x+(indexOfVal2%4)])==1)):
                a=int(domain[4*x+(indexOfVal1%4)][0])
                b=int(domain[4*x+(indexOfVal2%4)][0])
                return not (a  == (b - int(self.n)))
            #Forward cheking
            elif((len(domain[4*x+(indexOfVal1%4)])==1) and (len(domain[4*x+(indexOfVal2%4)])!=1)):
                flag = True
                for possibleValue in domain[4*x+(indexOfVal2%4)]:
                    if(int(possibleValue) - int(self.n) == int(domain[4*x+(indexOfVal1%4)][0])):
                        for i in range(len(domain)):
                            if(possibleValue in domain[i]):
                                domain[i].remove(possibleValue)
                        domain[4*x+(indexOfVal2%4)]= [possibleValue]
                        flag = False
                return flag #if value not in domain then return true
            elif((len(domain[4*x+(indexOfVal1%4)])!=1) and (len(domain[4*x+(indexOfVal2%4)])==1)): 
                flag = True 
                for possibleValue in domain[4*x+(indexOfVal1%4)]:
                     if(int(possibleValue) == int(domain[4*x+(indexOfVal2%4)][0])  - int(self.n) ):
                        for i in range(len(domain)):
                            if(possibleValue in domain[i]):
                                domain[i].remove(possibleValue)
                        domain[4*x+(indexOfVal1%4)]= [possibleValue]
                        flag = False
                return flag
            return False # no possible value in domain return true
        except:
            
            return False
        
"""c=Constraints_Type6()
c.createConstaintsFromLine("years(owners=Anita) = years(dogs=Shadow) - 2")
print(c.toString())

x={'years': ['2006', '2007', '2008', '2009'], 'owners': ['Anita', 'Barbara', 'Douglas', 'Fernando'], 'breeds': ['bulldog', 'dalmatian', 'greatDane', 'pekingese'], 'dogs': ['Harley', 'Molly', 'Riley', 'Shadow']}


d=[["2007"],['2006'], ['2008'], ['2009'], ['Anita'], ['Douglas'], ['Barbara'],[ 'Fernando'], [ 'dalmatian'], [ 'pekingese'],['bulldog'],[ 'greatDane'], [ 'Harley'], ['Riley'],[ 'Molly'], [ 'Shadow']]
print(c.isConstraintViolated(d,x))"""