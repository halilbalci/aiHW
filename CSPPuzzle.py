from CSPNode import CSPNode
import copy
import sys
from fileIO import txtToArray
from fileIO import initialize_dict_from_dataLinesArray
from fileIO import initialize_constraints_from_linesArray

class CSPPuzzle:
    indexOfDomains=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Root = CSPNode([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],indexOfDomains)
    constraintBase=[]
    dataDict={}
    
    def __init__(self,fileNumber):
        dataFileName="data-"+fileNumber+".txt"
        clueFileName="clues-"+fileNumber+".txt"
        self.dataDict=self.initializeDataDict(dataFileName) #pull data from file
        #print(self.dataDict)
        self.constraintBase = self.initializeConstraintBase(clueFileName) #pull constraints from file 
        #for i in self.constraintBase:            #newNode.printNode()
        #    print("---",i.toString())
        variables =[] 
        for k in self.dataDict:
            variables.append(k)
        #print("variables =",variables)
        #index of domains fill with all values
        n=0
        for var in variables:
            #print("var=",var)
            self.indexOfDomains[n] = self.dataDict.get(var).copy()
            self.indexOfDomains[n+1] = self.dataDict.get(var).copy()
            self.indexOfDomains[n+2] = self.dataDict.get(var).copy()
            self.indexOfDomains[n+3] = self.dataDict.get(var).copy()
            n+=4
    
    def initializeDataDict(self,filename):
        return initialize_dict_from_dataLinesArray(txtToArray(filename))
    def initializeConstraintBase(self,fileName):
        return initialize_constraints_from_linesArray(txtToArray(fileName))
    
    def solve(self):
        print("Puzzle is solving...")
        self.makeAssignment(self.Root,0)
       
    def makeAssignment(self,node,index):
        current_domain = copy.deepcopy(node.domains[index]) #inside domains may change [2006,2007,2008,2009] [2006,2007,2008,2009] 
        copyDomain = copy.deepcopy(node.domains)  #[[1,2,3,4],[1,2,3,4]...]
        for possibleValue in current_domain:
            possibleSolution = copy.deepcopy(node.solution)
            possibleSolution[index] = possibleValue
            new_domain = self._shrinkDomain(copyDomain, index, possibleValue)
            newNode = CSPNode(possibleSolution,new_domain)
            isValidAssignment=True
            for cons in self.constraintBase:
                if(cons.isConstraintViolated(new_domain,self.dataDict)):
                    isValidAssignment=False
                    break
            #if(isValidAssignment):
            #    node.addChildren(newNode)
            if(0 in possibleSolution):
                if(isValidAssignment):    
                    self.makeAssignment(newNode,index+1)
            else:
                for cons in self.constraintBase:
                    if(cons.isConstraintViolated(new_domain,self.dataDict)):
                        isValidAssignment=False
                        break
                    if(isValidAssignment):
                     
                        print(possibleSolution[0],possibleSolution[4],possibleSolution[8],possibleSolution[12])
                        print(possibleSolution[1],possibleSolution[5],possibleSolution[9],possibleSolution[13])
                        print(possibleSolution[2],possibleSolution[6],possibleSolution[10],possibleSolution[14])
                        print(possibleSolution[3],possibleSolution[7],possibleSolution[11],possibleSolution[15])
                        sys.exit("Solution is Found")

    def _shrinkDomain(self,domain,x,possibleValue):
        copyDomain = copy.deepcopy(domain)
        n=0
        if(x<4):
            n=0
        elif(x<8):
            n=4
        elif(x<12):
            n=8
        else:
            n=12
        for i in range(n,n+4):
            if(i==x):
                if(possibleValue in copyDomain[x]): #atanacak değer eğerki domainde ise
                    copyDomain[i]=[possibleValue]
            else:
                if(possibleValue in copyDomain[i] and len(copyDomain[i]) != 1): #posVAlue eğerki domainde ise ve sadece o yok ise
                    copyDomain[i].remove(possibleValue)
        return copyDomain
#puzzle = CSPPuzzle("3")
#puzzle.solve()