def f(comparer, handSize, dominoes):
    #logic removes comparer from set so pop() has to remove the non-comparer number
    #it then returns the random value it removed (not random b/c only non-comparer is left)
    
    trains = []
    
    match = [x for x in dominoes if comparer in x]

    print('RECURSION')
    print('comparer')
    print(comparer)
    print('dominoes')
    print(dominoes)
    print('match:')
    print(match)
    print('')

    subtrain = {}

    if len(match) == 0:
        if len(dominoes) == handSize:
            subtrain.update({0:match})
        else:
            subtrain.update({comparer:match})
    else:
        for x in match:
            subresult = f((set(x) - {comparer}).pop(), handSize, [d for d in dominoes if d != x])
            for y,z in subresult.items():
                if len(dominoes) == handSize:
                    subtrain.update({comparer + y : z + [x]})
                else:
                    subtrain.update({(comparer*2) + y : z + [x]})

    return subtrain



# double = int(input("Enter the number on your starting double: \n"))

# handSize = int(input("How many dominoes are in your hand? \n"))

# dominoes = []

# for i in range(handSize):
#     dominoe = [int(i) for i in input("Enter dominoe " + str(i+1) + " as x,y: \n").split(",")]
#     #print(dominoe)
#     dominoes.append(dominoe)

double = 1
handSize = 4
dominoes = [[1, 3], [2, 3], [5, 3], [4, 2]]

# double = 3
# handSize = 15
# dominoes = [[6,2], [6,4], [6,5], [6,12], [9,2], [9,0], [3,4], [4,11], [2,0], [10,5], [7,3], [0,8], [1,8], [11,8], [11,12]]

#bad logic: b/c comparer is being multiplied by 2 in function only need one number of the double
#train = f(double, dominoes) + (double*2)
#good logic:
train = f(double, handSize, dominoes)
counter = 0

for trainTotal in sorted(train.keys(), reverse=True):
    counter += 1
    print('Train ' + str(counter) + ':')
    print('\tTotal points: ' + str(trainTotal))
    subTrain = train[trainTotal]
    trainLen = len(subTrain)
    trainDiff = handSize - trainLen
    print('\tTrain length: ' + str(trainLen))
    print('\tdominoes left in hand: ' + str(trainDiff))
    print('\tTrain:')
    print('\t' + str([subTrain[trainLen - (subTrain.index(x)+1)] for x in subTrain]))

