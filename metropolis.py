from random import choice, random
from math import exp
state=0
nstates=4
states=[0]*nstates
T=0.1
ntrials=1000000
for trial in range (ntrials):
    newstate=choice(range(nstates))
    x=exp(-(newstate-state)/T)
    if x>random():
        state=newstate
    states[state]+=1
#Insert code from lecture notes here

Boltz=[0]*nstates
partition=0.
for i in range(nstates):
	Boltz[i]=exp(-i/T)
	partition+=exp(-i/T)
for i in range(nstates-1,-1,-1):
	print("%d   %6.3f  %6.3f"%(i,states[i]/ntrials,Boltz[i]/partition))