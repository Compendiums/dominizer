def trainOutput(handSize, full_trains, multi_trains):
     counter = 0
     perfect_trains = {}
     comboTrains = list({**full_trains, **multi_trains}.values())
     print("comboTrains")
     print(comboTrains)
     for comboTrain in comboTrains:
         print(len(list(comboTrain.values())[0]))
 
 for trainTotal in sorted(train.values().keys(), reverse=True):
     counter += 1
     print('Train ' + str(counter) + ':')
     print('\tTotal points: ' + str(trainTotal + (double * 2)))
     subTrain = train[trainTotal]
     trainLen = len(subTrain)
     trainDiff = handSize - trainLen
     print('\tTrain length: ' + str(trainLen))
     print('\tdominoes left in hand: ' + str(trainDiff))
     print('\tTrain:')
     print('\t' + str([subTrain[trainLen - (subTrain.index(x)+1)] for x in subTrain]))