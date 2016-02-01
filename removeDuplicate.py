#!/usr/bin/python

import sys
import getopt
import CodeChiffreSonFromWord
  
lastTenWords = []
  
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
      print(word.rstrip('\n') + " -> " + CodeChiffreSonFromWord.getNumber(word))
  while len(lastTenWords) != 0:
    word = isDuplicate("")
    if word != "":
      print(word.rstrip('\n') + " -> " + CodeChiffreSonFromWord.getNumber(word))
  return 1
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    parseFile(sys.argv[1])
