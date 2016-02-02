#!/usr/bin/python
# coding: utf8 

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
	("7", ["kk", "k", "cc", "ca", "co", "c", "g", "q", "ga", "go", "cô"]),
	("8", ["ff", "f", "v", "ph"]),
	("9", ["pp", "bb", "p", "b"]),
	("70", ["cce", "cti", "x", "ex", "ccè", "ccé"]),
  ("75", ["gl"]),
  ("72", ["cn"]),
  ("73", ["cm"]),
  ("71", ["ct"])
  ]
  
voyelles = ["a", "e", "i", "o", "u", "y", "â", "é", "è", "ï", "ü", "û"]

class Usage(Exception):
  def __init__(self, msg):
        self.msg = msg
        
def isVoyelle(c):
  for voyelle in voyelles:
    if c == voyelle[0]:
      return True
  return False
  
def isMute(word, idx, sound):
  indexSound = word.find(sound, idx)
  muteConsonnesEnd = ["t", "s", "n", "z", "m", "x", "ts", "er", "ent", "ant"]
  muteSoundsBeforeConsonne = ["en", "an", "on", "in"]
  for muteConsonneEnd in muteConsonnesEnd:
    if (indexSound + len(muteConsonneEnd)) >= len(word) and word.endswith(muteConsonneEnd) == True:
      return (True, len(muteConsonneEnd))
  for muteSound in muteSoundsBeforeConsonne:
      muteSoundIdx = word.find(muteSound, idx)
      # print("word -> " + word + " idx -> " + str(idx) + " sound -> " + sound + " muteSound -> " + muteSound + " muteSoundIdx -> " + str(muteSoundIdx))
      if (muteSoundIdx >= idx and muteSoundIdx <= (idx + len(muteSound)) and 
			muteSound.find(sound) >= 0 and (muteSoundIdx + len(muteSound) < len(word) and 
      indexSound > muteSoundIdx and #I do not know if it must be >= or >
      isVoyelle(word[muteSoundIdx + len(muteSound)]) == False)):
        # print("ici")
        # print
        return (True, len(muteSound))
  # print
  return (False, 0)
  
def getFigure(word, idx):
  results=[]
  toAdd = 0
  for numberAndSounds in numbersAndSounds:
    for sound in numberAndSounds[1]:
      indexSound = word.find(sound, idx)
      mute = isMute(word, idx, sound)
      # if (sound == "cce"):
      #   print("idx -> " + str(idx) + " sound -> " + sound + " mute -> " + str(mute[0]) + " indexSound -> " + str(indexSound))
      if indexSound >= 0 and mute[0] == False:
        results.append((indexSound, numberAndSounds[0], sound))
      # elif mute[0] == True:
      #   print("sound -> " + sound + " mute1 -> " + str(mute[1]))
      #   idx = idx + mute[1]
  if len(results) == 0:
    return (idx + 1, "-1", "")
  else:
    # print("loop")
    bestRes = (len(word), "-1", "")
    for result in results:
      # print(result)
      if result[0] < bestRes[0]:
        bestRes = result
      elif result[0] == bestRes[0]:
        if len(result[2]) > len(bestRes[2]):
          bestRes = result;
    return (bestRes[0] + len(bestRes[2]), bestRes[1], bestRes[2])
  
def getNumber(word):
  word = word.replace(" ", "").replace("\n", "").rstrip('\n')
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
		nbr = getNumber(line)
		os.system("echo " + line.rstrip('\n') + " >> WordByNumber/" + str(nbr) + ".txt")
	return 1
		
if __name__ == "__main__":
	if len(sys.argv) >= 2:
		parseFile(sys.argv[1])
