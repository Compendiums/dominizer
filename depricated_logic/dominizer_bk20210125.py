def f(comparer,dominos):
    #logic removes comparer from set so pop() has to remove the non-comparer number
    #it then returns the random value it removed (not random b/c only non-comparer is left)
    
    trains = []
    
    match = [x for x in dominos if comparer in x]

    print('RECURSION')
    print('comparer')
    print(comparer)
    print('dominos')
    print(dominos)
    print('match:')
    print(match)
    print('')

    subtrain = {}

    if len(match) == 0:
        subtrain.update({comparer:match})
    elif len(match) == 1:
        subresult = f((set(match[0]) - {comparer}).pop(), [d for d in dominos if  d!= match[0]])
        for y,z in subresult.items():
            subtrain.update({(comparer*2) + y : z + [match[0]]})
    else:
        for x in match:
            subresult = f((set(x) - {comparer}).pop(), [d for d in dominos if d != x])
            for y,z in subresult.items():
                subtrain.update({(comparer*2) + y : z + [x]})

    return subtrain



# double = int(input("Enter the number on your starting double: \n"))

# handSize = int(input("How many dominos are in your hand? \n"))

# dominos = []

# for i in range(handSize):
#     domino = [int(i) for i in input("Enter domino " + str(i+1) + " as x,y: \n").split(",")]
#     #print(domino)
#     dominos.append(domino)

# double = 1
# handSize = 4
# dominos = [[1, 3], [2, 3], [5, 3], [4, 2]]

double = 3
handSize = 15
dominos = [[6,2], [6,4], [6,5], [6,12], [9,2], [9,0], [3,4], [4,11], [2,0], [10,5], [7,3], [0,8], [1,8], [11,8], [11,12]]

#bad logic: b/c comparer is being multiplied by 2 in function only need one number of the double
#train = f(double, dominos) + (double*2)
#good logic:
train = f(double, dominos)
counter = 0

# for traintotal,subtrain in train.items():
#     counter += 1
#     print('Train ' + str(counter) + ':')
#     print('\tTotal: ' + str(traintotal+double))
#     print('\tDominos used: ' + str(len(subtrain)))
#     print('\tTrain: ' + str(subtrain + [[double,double]]))

for trainTotal in sorted(train.keys(), reverse=True):
    counter += 1
    print('Train ' + str(counter) + ':')
    print('\tTotal points: ' + str(trainTotal+double))
    subTrain = train[trainTotal]
    trainLen = len(subTrain)
    trainDiff = handSize - trainLen
    print('\tTrain length: ' + str(trainLen))
    print('\tDominos left in hand: ' + str(trainDiff))
    print('\tTrain:')
    print('\t' + str([subTrain[trainLen - (subTrain.index(x)+1)] for x in subTrain]))

