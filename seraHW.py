def financialCrisis(roadRegister):
    newRegister = []
    n = len(roadRegister)
    newRegister = [ [ [roadRegister[j][k] for j in range(n) if j!=l] for k in range(n) if k!=l] for l in range(n)] 
    return newRegister
false = False
true = True
roadRegister = [[false, true,  true,  false],
                [true,  false, true,  false],
                [true,  true,  false, true ],
                [false, false, true,  false]]
print(financialCrisis(roadRegister))