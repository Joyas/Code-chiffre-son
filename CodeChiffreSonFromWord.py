#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import os

numbersAndSounds = [
	("0", ["ss", "s", "z", "ce", "ci", "cy", "cè", "cé", "ç"]), 
	("1", ["tt", "d", "t"]), 
	("2", ["nn", "n", "gn", "nh"]), 
	("3", ["mm", "m"]), 
	("4", ["rr", "r"]), 
	("5", ["ll", "l"]), 
	("6", ["j", "gi", "ge", "gy", "ch", "sh", "gé", "gî"]),
	("7", ["kk", "cc", "ca", "co", "cu", "ct", "gu", "qu", "ga", "go"]),
	("8", ["ff", "f", "v", "ph"]),
	("9", ["pp", "bb", "p", "b"]),
	("70", ["ct", "x", "ex"]),
  ("75", ["gl"]),
  ("72", ["cn"]),
  ("73", ["cm"])
	]
  
voyelles = ["a", "e", "i", "o", "u", "y", "â", "é", "è", "ï", "ü", "û"]

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg
        
def isVoyelle(word, idx):
  
  for voyelle in voyelles:
    if word.find(voyelle) == idx:
      print("word ->" + word + " | idx -> " + str(idx) + " | voyelle -> " + voyelle)
      return True
  return False
  
def isMute(word, idx, sound):
  indexSound = word.find(sound, idx)
  muteConsonnesEnd = ["t", "s", "n", "z", "m", "x", "ts", "er", "ent"]
  muteSoundsBeforeConsonne = ["en", "an", "on"]  
  for muteConsonneEnd in muteConsonnesEnd:
    if indexSound + len(muteConsonneEnd) >= len(word) and word.endswith(muteConsonneEnd):
        return True
  for muteSound in muteSoundsBeforeConsonne:
      muteSoundIdx = word.find(muteSound, idx)
      if muteSoundIdx >= idx and muteSoundIdx <= (idx + len(muteSound)) and muteSound.find(sound) >= 0 and (muteSoundIdx + len(muteSound) < len(word) and isVoyelle(word, muteSoundIdx + len(muteSound)) == False):
        return True
  return False
  
def getFigure(word, idx):
  results=[]
  for numberAndSounds in numbersAndSounds:
    for sound in numberAndSounds[1]:
      indexSound = word.find(sound, idx)
      if indexSound >= 0 and isMute(word, idx, sound) == False:
        results.append((indexSound, numberAndSounds[0], sound))
  if len(results) == 0:
    return (idx + 1, "-1", "")
  else:
    bestRes = (len(word), "-1", "")
    for result in results:
      if result[0] < bestRes[0]:
        bestRes = result
      elif result[0] == bestRes[0]:
        if len(result[2]) > len(bestRes[2]):
          bestRes = result;
    return (bestRes[0] + len(bestRes[2]), bestRes[1], bestRes[2])
  
def getNumber(word):
  result = ""
  idx = 0
  while idx < len(word) and idx >= 0:
    resultGetFigure = getFigure(word, idx)
    idx = resultGetFigure[0]
    if resultGetFigure[1] != "-1":
      figure = resultGetFigure[1]
      result += figure
  return result
	
def parseFile(fileName):
	inputfile = open(fileName)
        os.system("mkdir WordByNumber")
	for line in inputfile:
		nbr = getNumber(line.rstrip('\n'))
#		sys.stdout.write(line.rstrip('\n') + "=>" + nbr + "\n")
                os.system("echo " + line.rstrip('\n') + " >> WordByNumber/" + str(nbr) + ".txt")
	return 1
		
if __name__ == "__main__":
	if len(sys.argv) >= 2:
		parseFile(sys.argv[1])
