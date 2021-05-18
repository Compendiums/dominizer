from log_setup import logger

class dominizer:

    def train_recursion(self, comparer, dominoes, hand_size):

        # logger.info("comparer: " + comparer)
        # logger.info("hand_size: " + hand_size)
        # logger.info("dominoes:")
        # logger.info(dominoes)
        
        matches = [d for d in dominoes if comparer in d]

        # logger.info("matches:")
        # logger.info(matches)

        subtrains = []

        # logic for no matches or only matched to doubles (cannot play doubles without follow up dominoe)
        if (len(matches) == 0) or (len(matches) == 1 and matches[0][0] == matches[0][1]):
            subtrains += [{
                "total" : 0, 
                "train" : [],
                "perfect" : False
            }]

        else:
            for match in matches:
                new_dominoes = [d for d in dominoes if d != match]

                if match[0] == match[1]:
                    new_comparer = match[0]
                else:
                    #logic removes comparer from set so pop() has to remove the non-comparer number
                    #it then returns the random value it removed (not random b/c only non-comparer is left)
                    new_comparer = (set(match) - {comparer}).pop()

                subresults = self.train_recursion(new_comparer, new_dominoes, hand_size)

                for subresult in subresults:
                    new_train = [match] + subresult["train"]

                    if len(new_train) == hand_size:
                        perfect = True
                    else:
                        perfect = False
                    
                    subtrains += [{
                        "total" : sum(match) + subresult["total"], 
                        "train" : new_train,
                        "perfect" : perfect
                    }]

        return subtrains    

    
    def train_output(self, full_trains, multi_trains):
        
        perfect_trains = []
        new_full_trains = []

        # only full_trains could possibly have a perfect train
        # multi_trains by nature will remove one or more dominoes
        for full_train in full_trains:
            if full_train["perfect"]:
                perfect_trains += [full_train]
            else:
                new_full_trains += [full_train]

        #used later, clearing for safety
        full_train = None

        print("")

        #perfect train specific output
        if perfect_trains:
            if len(perfect_trains) == 1:
                print("You have a perfect train! You win!!!\n")

            elif len(perfect_trains) > 1:
                print("WHOA. You have multiple perfect trains! You must be cheating...\n")

            self.train_breakdown(perfect_trains)

            print("--------------------------------------------------\n")

        # standard output
        # no matches at all (if full_trains is empty so will be multi_trains)
        if not full_trains:
            print("You've got nothing - you're drawing this round buddy.")

        # matches in both (if multi_trains is populated so will be full_trains)
        elif multi_trains:
            print("Playing with strategy? Try these:\n")
            self.train_breakdown(multi_trains)

            print("Going for broke? Try these:\n")
            self.train_breakdown(full_trains)

        # multi is empty but full is not
        else:
            print("Here are your options:\n")
            self.train_breakdown(full_trains)

    
    def train_breakdown(self, input_trains):
        counter = 0
        train_scores = []

        # get unique train scores for sorted output
        for input_train in input_trains:
            input_score = input_train["total"]
            if input_score not in train_scores:
                train_scores.append(input_score)

        # loop through sorted scores, if they match, output all the trains matched 
            # if there is a score tie, output order is random
        for score in sorted(train_scores, reverse=True):
            for input_train in input_trains:
                
                train_score = input_train["total"]

                if score == train_score:
                    counter += 1
                    if counter == 1:
                        str_count = "  Best Train:"
                    else:
                        str_count = "  Train " + str(counter) + ":"

                    train = str(input_train["train"])

                    print(str_count)
                    print(f"    Score: {train_score}")
                    print("    Train:")
                    print(f"    {train}")
                    print("")





