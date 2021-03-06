
# generate a runMC.csh script that creates the .csh and .jdl files
# to process MC data 

import os

def getArgs() :
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--inFile",default='MCsamples.csv',help="Input file name.") 
    return parser.parse_args()

args = getArgs() 
outLines = []
cwd = os.getcwd()
for line in open(args.inFile,'r').readlines() :
    nickname = line.split(',')[0]
    #print("\n\n\n line.split(',')={0:s}".format(str(line.split(','))))
    dataset = line.split(',')[6].replace(' ','_').strip()
    if len(dataset) < 2 : continue
    #print("\n***line.split()={0:s}".format(str(line.split(','))))
    print("nickname={0:s} \n dataset={1:s}".format(nickname,dataset))

    mode = 'anaXRD'
    
    outLines.append("mkdir {0:s}\ncd {0:s}\n".format(nickname))
    outLines.append("python ../makeCondor.py --dataSet {0:s} --nickName {1:s} --mode {2:s}\n".format(dataset,nickname, mode))
    outLines.append("cd {0:s}\n".format(cwd))

open('runMC.csh','w').writelines(outLines)



    
    
