# Kenji Crenshaw
# 

#This file is made to show the best match line with the highest 
# aligntment score for a given file

# Gain access to the file
fileIn = open("seq.txt")
bestLineLoc = 0
highestScore = 0
bestMatchSequence = " "
bestMatchID = " "
source = input("SOURCE : ")

for line in fileIn:
   #first get the line id and the sequence
   matchScore = 0
   matchId = line[0:8]
   matchSequence = line[10:]
   #Iterate through each line
   for lineLoc in range(len(matchSequence)-len(source)):
      sourceChar = 0
      #Calculates the match score at each for each placement of the sorce
      for matchChar in matchSequence[lineLoc:lineLoc + len(source)]:
         if(matchChar == source[sourceChar]):
            matchScore = matchScore + 5;
         else:
            matchScore = matchScore - 3;
         sourceChar = sourceChar + 1;
      if(matchScore >= highestScore):
         highestScore = matchScore;
         bestMatchID = matchId;
         bestMatchSequence = matchSequence;
         bestLineLoc = lineLoc;
      matchScore = 0;

#Print Results
print("Highest score : " + str(highestScore))
print("Best match line : " + bestMatchID)
print(" " * bestLineLoc + source)
print(" " * bestLineLoc, end = '')
count = 0
for i in range(bestLineLoc, bestLineLoc + len(source)):
   if(bestMatchSequence[i] == source[count]):
      print("|", end = '')
   else:
      print(" ", end = '')
   count = count + 1; 
print()
print(bestMatchSequence)
