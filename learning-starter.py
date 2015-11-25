import mountaincar
from Tilecoder import numTilings, tilecode, numTiles, tiles
from pylab import *
import random

numRuns = 50
numEpisodes = 200
alpha = 0.05/numTilings
gamma = 1
lmbda = 0.9
epsilon = 0
n = numTiles * 3
F = [-1]*numTilings

def actionTileCode(F,S,A):
    tilecode(S[0],S[1],F)
    F = [x + A*(numTilings*tiles*tiles) for x in F]
    return F

def getExpected(q):
    expectedVal = 0
    a = argmax(q)
    for i in range(3):
        if(a==i):
            expectedVal = expectedVal + (1 - 2*(epsilon/3))*q[i]
        else:
            expectedVal = expectedVal + (epsilon/3)*q[i]
    return expectedVal
        
def eligibilityTrace(zerovec,F):
    zerovec = alpha*lmbda*zerovec
    zerovec[F] = 1
    return zerovec
 
def Qs(F,S):
    q = zeros(3)
    actionTileCode(F,S,0)
    q[0] = sum(w[F])
    actionTileCode(F,S,1)
    q[1] = sum(w[F])
    actionTileCode(F,S,2)
    q[2] = sum(w[F])
    return q
   
    
returnAvg = zeros(200)
numSteps = zeros(200)    
    
runSum = []
for run in range(numRuns):
    w = -0.01*rand(n)
    returnSum = 0.0
    
    for episodeNum in range(numEpisodes):
        zerovec = zeros(n)
        G = 0
        A = 0
        S = mountaincar.init()
        F = actionTileCode(F,S,A)
        zerovec[F] = 1
        episodeLen = 0
        while(S is not None):
            episodeLen = episodeLen + 1
            RSA = mountaincar.sample(S,A)
            R = RSA[0]
            S = RSA[1]
            G = G + R
            delta = R - sum(w[F])
            q = zeros(3)
            
            if(S is not None):
                for a in range(3):
                    F = actionTileCode(F,S,a)
                    q[a] = sum(w[F])
            else:
                w = w + alpha*delta*zerovec
                break
                    
            expected_q = getExpected(q)
            delta = delta + expected_q
            
            A = argmax(q) if rand() >= epsilon else random.choice([0,1,2])
            
            w = w + alpha*delta*zerovec
            
            F = actionTileCode(F,S,A)
            zerovec = eligibilityTrace(zerovec,F)
        
        returnAvg[episodeNum] = returnAvg[episodeNum] + G
        numSteps[episodeNum] = numSteps[episodeNum] + episodeLen
#        print "Episode Length: ", episodeLen, "Return: ", G
#        returnSum = returnSum + G
#    print "Average return:", returnSum/numEpisodes
#    runSum.append(returnSum/numEpisodes)
#print "Overall average return:", runSum/numRuns/numEpisodes

returnAvg = returnAvg/50;
numSteps = numSteps/50;

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F,(-1.2+i*1.7/steps, -0.07+j*0.14/steps)))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()


