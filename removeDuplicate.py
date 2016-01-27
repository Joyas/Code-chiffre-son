#!/usr/bin/python

# pb -> abaissates

import sys
import getopt
import CodeChiffreSonFromWord
  
lastTenWords = []

# numbersAndSounds = [
#   ("0", ["ss", "s", "z", "ce", "ci", "cy"]), 
#   ("1", ["tt", "d", "t"]), 
#   ("2", ["nn", "n"]), 
#   ("3", ["mm", "m"]), 
#   ("4", ["rr", "r"]), 
#   ("5", ["ll", "l"]), 
#   ("6", ["j", "gi", "ge", "gy", "ch", "sh"]),
#   ("7", ["kk", "ca", "co", "cu", "ct", "qu"]),
#   ("8", ["ff", "f", "v", "ph"]),
#   ("9", ["pp", "bb", "p", "b"]),
#   ("70", ["ct", "x"])
#   ]
  
# def isMute(word, idx, sound):
#   indexSound = word.find(sound, idx)
#   muteConsonne = "tsnzmx"
#   muteSounds = ["en", "an", "on", "ent"]  
#   if (indexSound + len(sound) + 1) >= len(word) - 1 and (muteConsonne.find(sound) >= 0 or sound.endswith("er")):
#     return True
#   for muteSound in muteSounds:
#     if word.find(muteSound, indexSound - 1) >= 0 and muteSound.find(sound) >= 0 and (idx - 1 + len(muteSound)) == len(word):
#       return True
#   return False
  
# def getFigure(word, idx):
#   results=[]
#   for numberAndSounds in numbersAndSounds:
#     for sound in numberAndSounds[1]:
#       indexSound = word.find(sound, idx)
#       if indexSound >= 0 and isMute(word, idx, sound) == False:
#         results.append((indexSound, numberAndSounds[0], sound))
#   if len(results) == 0:
#     return (idx + 1, "-1")
#   else:
#     bestRes = (len(word), "-1", "")
#     for result in results:
#       if result[0] < bestRes[0]:
#         bestRes = result
#       elif result[0] == bestRes[0]:
#         if len(result[2]) > len(bestRes[2]):
#           bestRes = result;
#     return (bestRes[0] + len(bestRes[2]), bestRes[1])
  
# def getNumber(word):
#   result = ""
#   idx = 0
#   while idx < len(word) and idx >= 0:
#     resultGetFigure = getFigure(word, idx)
#     idx = resultGetFigure[0]
#     if resultGetFigure[1] != "-1":
#       figure = resultGetFigure[1]
#       result += figure
#   return result
  
def hasManySameCharacter(word1, word2):
  if len(word1) > len(word2):
    word = word1
    word1 = word2
    word2 = word
  i = 0
  same = 0.0
  for c in word1:
    if c == word2[i]:
      same = same + 1.0
    i = i + 1
  if same != 0 and same / float(len(word2)) > 0.5:
    return True
  return False 
  
def isDuplicate(newWord):
  word = ""
  if len(lastTenWords) == 100 or newWord == "":
    word = lastTenWords.pop(0)[0]
    numberOfWord = CodeChiffreSonFromWord.getNumber(word)
    for idx, oldWord in enumerate(lastTenWords):
      numberOfOldWord = CodeChiffreSonFromWord.getNumber(oldWord[0])
      if numberOfWord == numberOfOldWord and hasManySameCharacter(word, oldWord[0]) == True:
        if oldWord[0].endswith("er") == True:
          word = oldWord[0]
        lastTenWords[idx] = (lastTenWords[idx][0], True)
    i=0
    while i < len(lastTenWords):
      if lastTenWords[i][1] == True:
        lastTenWords.pop(i)
      else:
        i+=1
  if newWord != "":
    lastTenWords.append((newWord, False))
  return word
  
def parseFile(fileName):
  inputfile = open(fileName)
  for line in inputfile:
    word = isDuplicate(line.rstrip('\n'))
    if word != "":
      print(word.rstrip('\n'))
  while len(lastTenWords) != 0:
    word = isDuplicate("")
    if word != "":
      print(word.rstrip('\n'))
  return 1
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    parseFile(sys.argv[1])
