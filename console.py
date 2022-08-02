import disco
import dictionary

import time
import copy

print(" ______  _________ _______  _______  _______    _______  _______  _______ ")
print("(  __  \ \__   __/(  ____ \(  ____ \(  ___  )  / ___   )(  ___  )(  ___  )")
print("| (  \  )   ) (   | (    \/| (    \/| (   ) |  \/   )  || (   ) || (   ) |")
print("| |   ) |   | |   | (_____ | |      | |   | |      /   )| |   | || |   | |")
print("| |   | |   | |   (_____  )| |      | |   | |     /   / | |   | || |   | |")
print("| |   ) |   | |         ) || |      | |   | |    /   /  | |   | || |   | |")
print("| (__/  )___) (___/\____) || (____/\| (___) |   /   (_/\| (___) || (___) |")
print("(______/ \_______/\_______)(_______/(_______)  (_______/(_______)(_______)")
print("                                                                          ")
print("Beginning Pattern Solving")
allPatterns = []
pattern = [['O','O','O','O','O'],
           ['O','O','O','O','O'],
           ['O','O','O','O','O'],
           ['O','O','O','O','O'],
           ['O','O','O','O','O']]
startTime = time.time()
patternTime = time.time()
for p in range(10):
    disco.recursivePattern(copy.deepcopy(pattern),0,0,p+1)
    allPatterns.append(disco.getPatterns())
    print(str(p+1) + " Space Patterns | " + str(len(allPatterns[p])) + " Patterns | Completed")
    print("Completed in " + str(round(time.time() - patternTime,5)) + " seconds")
    patternTime = time.time()
print("Finished Generating Patterns in " + str(round(time.time()-startTime,5)) + " seconds")
print("Begin Testing Patterns")

animalSolutions = []
solutionCount = []
for a in range(len(dictionary.animalNames)):
    testTime = time.time()
    print(dictionary.animalNames[a] + " | ", end='')
    animalBoards = disco.positionVariants(dictionary.animalPatterns[a])
    foundPatterns = False
    for p in range(10):
        print(str(p+1) + " ", end='')
        passedPatterns = disco.testPatterns(allPatterns[p],animalBoards)
        if len(passedPatterns) > 0:
            foundPatterns = True
            animalSolutions.append(passedPatterns)
            solutionCount.append(p+1)
            print()
            print(str(p+1) + " Space - " + str(len(passedPatterns)) + " Patterns Found")
            print(dictionary.animalNames[a] + " Completed in " + str(round(time.time() - testTime,5)) + " seconds")
            testTime = time.time()
            break
    if not (foundPatterns):
        passedPatterns.append([])
        print(-1)
        print("ERROR - No Patterns found for " + dictionary.animalNames[a])
        testTime = time.time()
print()
print("Process complete in " + str(round(time.time() - startTime,1)) + " seconds")

for i in range(5):
    print()
print("Welcome to the Disco Zoo Console, you can now browse the most efficient animal patterns in Disco Zoo")
while True:
    print("Type the Animal Name you want to search for or 'Exit'")
    command = input("")
    if command == "Exit":
        break
    index = -1
    for animal in dictionary.animalNames:
        if animal == command:
            index = dictionary.animalNames.index(animal)
    if index == -1:
        print("Invalid Input, Please Try Again")
        print()
    else:
        print(command + " --> " + str(len(animalSolutions[index])) + " Patterns Found --- " + str(solutionCount[index]) + " Spaces")
        print("Type 'Print' to print all patterns, or type 'Exit'")
        command = input("")
        if command == "Print":
            for pattern in animalSolutions[index]:
                disco.printPattern(pattern)