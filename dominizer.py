def trainRecursion(comparer, dominoes):
    #logic removes comparer from set so pop() has to remove the non-comparer number
    #it then returns the random value it removed (not random b/c only non-comparer is left)
    
    matches = [d for d in dominoes if comparer in d]

    print('RECURSION')
    print('comparer')
    print(comparer)
    print('dominoes')
    print(dominoes)
    print('matches:')
    print(matches)
    print('match len')
    print(len(matches))
    print('')

    subtrains = []

    if (len(matches) == 0) or (len(matches) == 1 and matches[0][0] == matches[0][1]):
        subtrains += [{0 : []}]
    
    else:
        for match in matches:
            newDominoes = [d for d in dominoes if d != match]
            
            if match[0] == match[1]:
                newComparer = match[0]
            else:
                newComparer = (set(match) - {comparer}).pop()
           
            subresults = trainRecursion(newComparer, newDominoes)
           
            for subresult in subresults:
                for total,train in subresult.items():
                    subtrains += [{sum(match) + total : [match] + train}]

    return subtrains    

# def trainOutput(handSize, fullTrains, multiTrains):
#     counter = 0
#     perfectTrains = {}
#     comboTrains = list({**fullTrains, **multiTrains}.values())
#     print("comboTrains")
#     print(comboTrains)
#     for comboTrain in comboTrains:
#         print(len(list(comboTrain.values())[0]))
    


# for trainTotal in sorted(train.values().keys(), reverse=True):
#     counter += 1
#     print('Train ' + str(counter) + ':')
#     print('\tTotal points: ' + str(trainTotal + (double * 2)))
#     subTrain = train[trainTotal]
#     trainLen = len(subTrain)
#     trainDiff = handSize - trainLen
#     print('\tTrain length: ' + str(trainLen))
#     print('\tdominoes left in hand: ' + str(trainDiff))
#     print('\tTrain:')
#     print('\t' + str([subTrain[trainLen - (subTrain.index(x)+1)] for x in subTrain]))


# double = int(input("Enter the number on your starting double: \n"))

# handSize = int(input("How many dominoes are in your hand? \n"))

# dominoes = []

# for i in range(handSize):
#     dominoe = [int(i) for i in input("Enter dominoe " + str(i+1) + " as x,y: \n").split(",")]
#     #print(dominoe)
#     dominoes.append(dominoe)

double = 1
handSize = 5
dominoes = [[1, 3], [2, 3], [5, 3], [4, 2], [2,2]]

# double = 3
# handSize = 15
# dominoes = [[6,2], [6,4], [6,5], [6,12], [9,2], [9,0], [3,4], [4,11], [2,0], [10,5], [7,3], [0,8], [1,8], [11,8], [11,12]]

#keyList = list(range(10000))

fullTrains = trainRecursion(double, dominoes)

multiTrains = []
multiStarts = [d for d in dominoes if double in d]
print("multiStarts")
print(multiStarts)

if len(multiStarts) > 1:
    for starter in multiStarts:
        remainingDominoes = [d for d in dominoes if d not in multiStarts]
        remainingDominoes.append(starter)
        subMultiTrain = trainRecursion(double, remainingDominoes)
        multiTrains += subMultiTrain

print("fullTrains")
print(fullTrains)
print("multiTrains")
print(multiTrains)



#dedupe
#retired in favor of dual type output
# for randKey,trainData in fullTrains.items():
#     for trainTotal in trainData.keys():
#         sortTrain = sorted(trainData[trainTotal])
        
#         for multiData in list(train.values()):
#             for multiTotal in multiData.keys():
#                 sortMulti = sorted(multiData[multiTotal])
                
#                 if sortTrain != sortMulti:
#                     train.update({randKey:trainData})



