import msvcrt
import random
from os import system
def cls():
  system("cls")
cls()
randwordstr = ""
randwords = []
prewords = ["alpha","beta","gama","delta","epsilon","zeta","eta","theta","iota","kappa","lambda","mu","nu","xi","omicron","pi","rho","sigma","tau","upsilon","phi","chi","psi","omega"] 
for i in range(0,60):
  random.append(random.choice(prewords))
  randwordstr = randwordstr + randwords[i] + " "
print(randwordstr)
