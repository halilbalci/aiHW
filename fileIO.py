from constraints_Type1 import Constraints_Type1
from constraints_Type2 import Constraints_Type2
from constraints_Type3 import Constraints_Type3
from constraints_Type4 import Constraints_Type4
from constraints_Type5 import Constraints_Type5
from constraints_Type6 import Constraints_Type6
from constraints_Type7 import Constraints_Type7
from constraints_Type8 import Constraints_Type8
from constraints_Type9 import Constraints_Type9
from constraints_Type10 import Constraints_Type10

def txtToArray(fileName):
    try:
        f = open(fileName, "r")
        line = f.readline()
        line=line.rstrip("\n")
        linesArray  = []
        while line :
            linesArray.append(line)
            line = f.readline()
            line=line.rstrip("\n")
        f.close()
        return linesArray
    except:
        print("file error")
        
def initialize_constraints_from_linesArray(linesArray):
    constraintsBase=[]
    try:    
        for i in linesArray:
            constraintsBase.append(initializeConstraintAccoringToline(i))
        return constraintsBase    
    except:
        print("initializing error")

def initializeConstraintAccoringToline(line):
    splitted_line = line.split()
    if(splitted_line[0]=="if"):
        if("not" in splitted_line):                                 #if x=a then not y=b
            constraint=Constraints_Type2() 
        elif("either" in splitted_line):                            #if x=a then either y=b or z=c
            constraint=Constraints_Type3() 
        elif("then" in splitted_line):                              #if x=a then y=b
            constraint=Constraints_Type1()
        else:
            print("error! line is not fit any constraint type")
    else:
        if(len(splitted_line)==3):
            if("=" in splitted_line):                               #n(x=a) = n(y=b) 
                constraint=Constraints_Type4()
            elif("<" in splitted_line):                             #n(x=a) < n(y=b) 
                constraint=Constraints_Type8()
            elif(">" in splitted_line):                             #n(x=a) > n(y=b) 
                constraint=Constraints_Type7()
            else:
                print("error! line is not fit any constraint type")
        elif(len(splitted_line)==5):
            if("+" in splitted_line):                               #n(x=a) = n(y=b) + m
                constraint=Constraints_Type5()
            elif("-" in splitted_line):                              #n(x=a) = n(y=b) - m
                constraint=Constraints_Type6()
            else:
                print("error! line is not fit any constraint type")
        elif(len(splitted_line)==8):
            constraint=Constraints_Type9()                          #one of {x=a,y=b} corresponds to z=c other t=d
        elif(len(splitted_line)==4):
            constraint=Constraints_Type10()                         #{x=a,y=b,z=c} are all different
        else:
                print("error! line is not fit any constraint type")
    constraint.createConstaintsFromLine(line)
    return constraint

def initialize_dict_from_dataLinesArray(linesArray):
    try:
        data_dict={}
        for i in range(len(linesArray)):
            splitted_line=linesArray[i].split(",")
            data_dict.update({splitted_line[0]:splitted_line[1:]})
        return(data_dict)
    except:
        print("initializing dictionary error")
        