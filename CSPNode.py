class CSPNode:
    def __init__(self, solution=[],domains=[]):
        
        self.children = [] 
        self.solution = solution
        self.domains  = domains 
        
    def addChildren(self, childNode):
        self.children.append(childNode)
        
    def printNode(self):
        print("----solution",self.solution)
        print("----domain=",self.domains)

