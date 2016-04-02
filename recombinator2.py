import csv
import math

class Trial():
    def __init__(self, nifB, nifBmod, nifN, nifNmod, nifE, nifEmod, nifM, nifMmod, nifU, nifUmod, nifH, nifHmod):
        self.nifB = nifB
        self.nifN = nifN
        self.nifE = nifE
        self.nifM = nifM
        self.nifU = nifU
        self.nifH = nifH
        self.nifBmod = nifBmod
        self.nifNmod = nifNmod
        self.nifEmod = nifEmod
        self.nifMmod = nifMmod
        self.nifUmod = nifUmod
        self.nifHmod = nifHmod
        self.score = predict3(nifB, nifN, nifE, nifH, nifM, nifU)
    def __lt__(self, otherTrial):
        if self.score < otherTrial.score:
            return True
        return False
    def __gt__(self, otherTrial):
        if self.score > otherTrial.score:
            return True
        return False
    def __eq__(self, otherTrial):
        if self.score == otherTrial.score:
            return True
        return False
    def __str__(self):
        stringRep = "nifB: %s : %s  " % (self.nifB, self.nifBmod)
        stringRep += "nifN: %s : %s  " % (self.nifN, self.nifNmod)
        stringRep += "nifE: %s : %s  " % (self.nifE, self.nifEmod)
        stringRep += "nifM: %s : %s  " % (self.nifM, self.nifMmod)
        stringRep += "nifU: %s : %s  "  % (self.nifU, self.nifUmod)
        stringRep += "nifH: %s : %s  " % (self.nifH, self.nifHmod)
        stringRep += " score = " + str(self.score)
        return stringRep
        
    

def predict(factor):
##(Intercept) -6.200e+02  9.824e+01  -6.311 9.08e-08 ***
##nifB         3.538e-02  1.065e-02   3.323 0.001732 ** 
##nifN         3.255e-02  8.778e-03   3.708 0.000551 ***
##nifE         4.373e-02  9.567e-03   4.571 3.53e-05 ***
##nifM         3.161e-02  1.122e-02   2.818 0.007045 ** 
##nifU         9.442e-02  1.010e-02   9.349 2.69e-12 ***
##nifH         5.023e-02  1.415e-02   3.550 0.000888 ***
##    return total
    total = -6.200e+02
    total += float(factor[0]) * 3.538e-02
    total += float(factor[1]) * 3.255e-02
    total += float(factor[2]) * 4.373e-02
    total += float(factor[3]) * 3.161e-02
    total += float(factor[4]) * 9.442e-02
    total += float(factor[5]) * 5.023e-02
    return total


def predict2(factor):
##(Intercept) -1.419e+02  8.952e+01  -1.586 0.120160    
##nifB         3.604e-02  7.038e-03   5.120 6.82e-06 ***
##nifN         3.770e-03  8.619e-03   0.437 0.664017    
##nifE         7.484e-03  9.932e-03   0.754 0.455246    
##nifM        -7.151e-04  1.166e-02  -0.061 0.951396    
##nifU        -5.367e-02  2.040e-02  -2.631 0.011784 *  
##nifH         9.336e-03  1.472e-02   0.634 0.529265    
##nifN:nifU    7.530e-06  1.705e-06   4.417 6.66e-05 ***
##nifE:nifU    1.152e-05  2.430e-06   4.739 2.37e-05 ***
##nifM:nifU    1.069e-05  2.870e-06   3.726 0.000563 ***
##nifU:nifH    1.323e-05  3.618e-06   3.656 0.000693 ***
    total = -1.419e+02
    total += float(factor[8]) * 3.604e-02
    total += float(factor[7]) * 3.770e-03
    total += float(factor[6]) * 7.484e-03
    total += float(factor[5]) * -7.151e-04
    total += float(factor[3]) * -5.367e-02
    total += float(factor[0]) * 9.336e-03
    total += float(factor[7])*float(factor[3]) * 7.530e-06
    total += float(factor[6])*float(factor[3]) * 1.152e-05
    total += float(factor[5])*float(factor[3]) * 1.069e-05
    total += float(factor[3])*float(factor[0]) * 1.323e-05
    return total

def predict3(nifB, nifN, nifE, nifH, nifM, nifU):
    ## this is the flexible function that we'll use on our fractional factorial design
    ## that is, the one with all of the interactions
    total = -1.419e+02 ## intercept
    total += float(nifB) * 3.604e-02
    total += float(nifN) * 3.770e-03
    total += float(nifE) * 7.484e-03
    total += float(nifH) * 9.336e-03
    total += float(nifM) * -7.151e-04
    total += float(nifU) * -5.367e-02
    total += float(nifN) * float(nifU) * 7.530e-06
    total += float(nifE) * float(nifU) * 1.152e-05
    total += float(nifM) * float(nifU) * 1.069e-05
    total += float(nifU) * float(nifH) * 1.323e-05
    return total
    
def predict4(nifB, nifN, nifE, nifH, nifM, nifU):
    ## this is the flexible function that we'll use on our fractional factorial design
    ## that is, the one with all of the interactions
    total = -1.419e+02 ## intercept
    total += float(nifB) * 3.604e-02
    total += float(nifU) * -5.367e-02
    total += float(nifN) * float(nifU) * 7.530e-06
    total += float(nifE) * float(nifU) * 1.152e-05
    total += float(nifM) * float(nifU) * 1.069e-05
    total += float(nifU) * float(nifH) * 1.323e-05
    return total   

def runYields():
    ## second library predictions:
    yieldfile = open("library_yields3.csv", "r")
    yielddata = list(csv.reader(yieldfile))
    variables = yielddata[0][1:7]
    for i in range(0, len(variables)):
        print(i, " ", variables[i])

    print("Second Library Predictions")

    for j in range(1, len(yielddata)):
        factor = yielddata[j][1:7]
        print(yielddata[j][0])
        predicted = predict2(factor)
        print("Predicted: %s, actual: %s" % (predicted, float(yielddata[j][7])))


    ### sanity test
    print("First Library Predictions")

    yieldfile2 = open("library_yields.csv", "r")
    yielddata = list(csv.reader(yieldfile2))
    for j in range(1, len(yielddata)):
        factor = yielddata[j][1:10]
        print(yielddata[j][0])
        predicted = predict2(factor)
        print("Predicted: %s, actual: %s" % (predicted, float(yielddata[j][10])))

## get some of the top values and a few on the bottom, don't re-use promoters/terminators
        ## create a magic factorial design with some top values for our 4 positive
        ## correlates and our 2 negative correlates
        ## plus the negative interaction correlates are really low magnitude
def GetHighModuleLibrary():
    modules = {}
    gridFile = open("grid.csv", "r")
    gridData = list(csv.reader(gridFile))
    for d in range(1, 11):
        modules[gridData[d][0] + "," + gridData[0][d]] = gridData[d][d]
    return modules

def GetLowModuleLibrary():
    modules = {}
    gridFile = open("grid.csv", "r")
    gridData = list(csv.reader(gridFile))
    for d in range(8, 14):
        modules[gridData[d][0] + "," + gridData[0][d]] = gridData[d][d]
## old version - really low modules
##        modules[gridData[0][36-d] + gridData[33 - d][0]] = gridData[33 - d][36-d]
    return modules

def main():
    ## do a small factorial design for these sets - lets see what the predicted yields are
    highModules = GetHighModuleLibrary()
    lowModules = GetLowModuleLibrary()
    highModNames = list(highModules)
    lowModNames = list(lowModules)
    highNum = len(highModNames)
    lowNum = len(lowModNames)
    results = []

    ## semi-factorial design - don't re-use modules!
    for a in range(highNum):
        for b in range(highNum):
            if a != b:
                for c in range(highNum):
                    if c != a and c != b:
                        for d in range(highNum):
                            if d != a and d != b and d != c:
                                for x in range(lowNum):
                                    if x != a and x != b and x != c and x != d:
                                        for y in range(lowNum):
                                            if x != y:
                                                score = predict3(highModules[highModNames[a]], highModules[highModNames[b]],
                                                                 highModules[highModNames[c]], highModules[highModNames[d]], lowModules[lowModNames[x]], lowModules[lowModNames[y]]) 
                                                print("nifB %s: %s  nifN %s: %s  nifE %s: %s  nifH %s: %s\nnifM %s: %s  nifU %s: %s  = %s" % (highModNames[a], highModules[highModNames[a]], highModNames[b], highModules[highModNames[b]],
                                                                             highModNames[c], highModules[highModNames[c]], highModNames[d], highModules[highModNames[d]], lowModNames[x], lowModules[lowModNames[x]], lowModNames[y], lowModules[lowModNames[y]], score))
                                                if(len(results) < 10): ## populate with first 10 results
                                                    results.append(Trial(highModules[highModNames[a]], highModNames[a], highModules[highModNames[b]], highModNames[b],
                                                                 highModules[highModNames[c]], highModNames[c], highModules[highModNames[d]], highModNames[d], lowModules[lowModNames[x]], lowModNames[x], lowModules[lowModNames[y]], lowModNames[y]))
                                                    if (len(results) == 10):
                                                        results.sort(reverse=True) ## sort first time around
                                                else:
                                                    if(score > results[9].score):
                                                        results.pop()
                                                        results.append(Trial(highModules[highModNames[a]], highModNames[a], highModules[highModNames[b]], highModNames[b],
                                                                 highModules[highModNames[c]], highModNames[c], highModules[highModNames[d]], highModNames[d], lowModules[lowModNames[x]], lowModNames[x], lowModules[lowModNames[y]], lowModNames[y]))
                                                        results.sort(reverse=True)

    for result in results:
        print(result)

    ## get the modules
    modFile = open("library_design5mods.csv", "w")
    modValues = csv.writer(modFile)
    modValues.writerow(["nifB","nifN","nifE","nifM","nifU","nifH"])
    for result in results:
          modValues.writerow([result.nifBmod,result.nifNmod,result.nifEmod,result.nifMmod,result.nifUmod,result.nifHmod])
    modFile.close()

    levelFile = open("library_design5levels.csv", "w")
    levelValues = csv.writer(levelFile)
    levelValues.writerow(["nifB","nifN","nifE","nifM","nifU","nifH"])
    for result in results:
          levelValues.writerow([result.nifB,result.nifN,result.nifE,result.nifM,result.nifU,result.nifH])
    levelFile.close()
    

if __name__ == '__main__':
    main()
