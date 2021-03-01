import dominizer as dom

def main():

    # user input
    # double = int(input("Enter the number on your starting double: \n"))
    # handSize = int(input("How many dominoes are in your hand? \n"))
    # dominoes = []
    # for i in range(handSize):
    #     dominoe = [int(i) for i in input("Enter dominoe " + str(i+1) + " as x,y: \n").split(",")]
    #     #print(dominoe)
    #     dominoes.append(dominoe)

    # hardcoded input
    double = 1
    handSize = 5
    dominoes = [[1, 3], [2, 3], [5, 3], [4, 2], [2,2]]
    # double = 3
    # handSize = 15
    # dominoes = [[6,2], [6,4], [6,5], [6,12], [9,2], [9,0], [3,4], [4,11], [2,0], [10,5], [7,3], [0,8], [1,8], [11,8], [11,12]]

    fullTrains = dom.trainRecursion(double, dominoes)

    multiTrains = []
    multiStarts = [d for d in dominoes if double in d]
    print("multiStarts")
    print(multiStarts)

    if len(multiStarts) > 1:
        for starter in multiStarts:
            remainingDominoes = [d for d in dominoes if d not in multiStarts]
            remainingDominoes.append(starter)
            subMultiTrain = dom.trainRecursion(double, remainingDominoes)
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


if __name__ = "__main__":
    
    main()