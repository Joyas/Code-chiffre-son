#!/usr/bin/python

import sys
import getopt

numbersAndSounds = [
	("0", ["ss", "s", "z", "ce", "ci", "cy"]), 
	("1", ["tt", "d", "t"]), 
	("2", ["n", "nn"]), 
	("3", ["mm", "m"]), 
	("4", ["rr", "r"]), 
	("5", ["ll", "l"]), 
	("6", ["j", "gi", "ge", "gy", "ch", "sh"]),
	("7", ["kk", "ca", "co", "cu", "ct"]),
	("8", ["ff", "f", "v", "ph"]),
	("9", ["pp", "bb", "p", "b"]),
	("70", ["ct", "x"])
	]

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg
	
def isMute(word, idx, sound):
	indexSound = word.find(sound, idx)
	muteConsonne = "tsnzmx"
	if (indexSound + len(sound) + 1) >= len(word) and muteConsonne.find(sound) >= 0:
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
		return (idx + 1, "-1")
	else:
		bestRes = (len(word), "-1", "")
		for result in results:
			if result[0] < bestRes[0]:
				bestRes = result
			elif result[0] == bestRes[0]:
				if len(result[2]) > len(bestRes[2]):
					bestRes = result;
		return (bestRes[0] + len(bestRes[2]), bestRes[1])
	
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
	for line in inputfile:
		nbr = getNumber(line)
		if len(nbr) < 3:
			sys.stdout.write(line.rstrip('\n') + "=>")
			print(nbr)
	return 1
		
if __name__ == "__main__":
	if len(sys.argv) >= 2:
		parseFile(sys.argv[1])