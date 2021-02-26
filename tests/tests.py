# list1 = [1,2,3,4]

# list2 = list1

# list2.append(5)

# print("list1")
# print(list1)
# print("list2")
# print(list2)

# del list1[0]
# print(list1)
# print(list1[0])

# dict1 = {13: {20: [[1, 4], [4, 2], [2, 3], [1, 3]]}, 14: {12: [[5, 3], [1, 3]]}, 21: {20: [[1, 3], [2, 3], [4, 2], [1, 4]]}, 22: {24: [[5, 3], [2, 3], [4, 2], [1, 4]]}}

# for traindata in dict1.values():
#     for key in traindata.keys():
#         print(sorted(traindata[key]))

# list3 = [1,2,3,4]
# list4 = [4,3,2,1]

# if sorted(list3) == sorted(list4):
#     print(1)
# else:
#     print(0)

# if len(match) == 0:
#     subtrain.update({0 : {0 : []}}) 
# elif len(match) == 1 and match[0][0] == match[0][1]:
#     print("in single double match")
#     subtrain.update({0 : {0 : []}})
# else:
#     for w in match:
#         newDomoinoes = [d for d in dominoes if d != w]
#         subresult = f((set(w) - {comparer}).pop(), handSize, newDomoinoes)
#         for x in subresult.values():
#             for y,z in x.items():
#                 subtrain.update({keyList[0]:{sum(w) + y : z + [w]}})
#                 del keyList[0]

# match = [w for w in range(10)]
# print(match)
# print(w)

def trainOutput(handSize, fullTrains, multiTrains):
    perfectTrains = []

    # only fullTrains could possibly have a perfect train
    # multiTrains by nature will remove one or more dominoes
    for fullTrain in fullTrains:
        if handSize == len(list(fullTrain.values())[0]):
            perfectTrains += [fullTrain]
    
    #used later, clearing for safety
    fullTrain = None

    print("")

    #perfect train specific output
    if len(perfectTrains) == 1:
        print("You have a perfect train! You win!!!\n")
        trainBreakdown(perfectTrains)
    
    elif len(perfectTrains) > 1:
        print("WHOA. You have multiple perfect trains! You must be cheating...\n")
        trainBreakdown(perfectTrains)
    
    if perfectTrains:
        print("--------------------------------------------------\n")
    
    # standard output
    # no matches at all (if fullTrains is empty so will be multiTrains)
    if not fullTrains:
        print("You've got nothing - you're drawing this round buddy.")
    
    # matches in both (if multiTrains is populated so will be fullTrains)
    elif multiTrains:
        print("Playing with strategy? Try these:\n")
        trainBreakdown(multiTrains)

        print("Going for broke? Try these:\n")
        trainBreakdown(fullTrains)

    # multi is empty but full is not
    else:
        print("Here are your options:\n")
        trainBreakdown(fullTrains)

def trainBreakdown(inputTrains):
    counter = 0
    trainScores = []

    # get unique train scores for sorted output
    for inputTrain in inputTrains:
        inputScore = list(inputTrain.keys())[0]
        if inputScore not in trainScores:
            trainScores.append(list(inputTrain.keys())[0])

    # loop through sorted scores, if they match, output all the trains matched 
        # if there is a score tie, output order is random
    for score in sorted(trainScores, reverse=True):
        for inputTrain in inputTrains:
            if score in inputTrain:
                counter += 1
                if counter == 1:
                    strCount = "  Best Train:"
                else:
                    strCount = "  Train " + str(counter) + ":"

                trainScore = list(inputTrain.keys())[0]
                train = str(inputTrain[trainScore])

                print(strCount)
                print(f"    Score: {trainScore}")
                print("    Train:")
                print(f"    {train}")
                print("")


_fullTrains = [{15: [[1, 3], [2, 3], [4, 2]]}, {19: [[1, 3], [2, 3], [2, 2], [4, 2]]}, {12: [[1, 3], [5, 3]]}, {7: [[1, 6]]}]
_multiTrains = [{15: [[1, 3], [2, 3], [4, 2]]}, {19: [[1, 3], [2, 3], [2, 2], [4, 2]]}, {12: [[1, 3], [5, 3]]}, {7: [[1, 6]]}]
_handSize = 5

# _fullTrains = [{28: [[4, 2],[4,8],[2,8]]},{28: [[2,8],[4,8],[4,2]]}]
# _multiTrains = [{28: [[4, 2],[4,8],[2,8]]},{28: [[2,8],[4,8],[4,2]]}]
# _handSize = 3

trainOutput(_handSize,_fullTrains,_multiTrains)