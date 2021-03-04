from dominizer import dominizer

def test_selector(mode):

    try:
        # class instantiation
        dom = dominizer()

        #set variables
        if mode == 1 or mode == 4:
            # basic test
            if mode == 1:
                print('beginning basic test')
            elif mode == 4:
                print('beginning component test: dominizer.train_recursion()')

            double = 1
            hand_size = 5
            dominoes = [[1, 3], [2, 3], [5, 3], [4, 2], [2,2]]

        elif mode == 2:
            # full hand/ multi start test
            print('beginning full hand/multi start test')
            double = 3
            hand_size = 15
            # these are not the inputs from the picture, correct
            dominoes = [[6,2], [6,4], [6,5], [6,12], [9,2], [9,0], [3,4], [4,11], [2,0], [10,5], [7,3], [0,8], [1,8], [11,8], [11,12]]

        elif mode == 3:
            # perfect train test
            print('beginning perfect train test')
            print('test doesnt exist yet')
            return
        
        elif mode == 5:
            # output test
            print('beginning output test')
            full_trains = []
            multi_trains = []

        else:
            # forced failure
            print('no existing test specified')
            return


        # run test
        if mode in range(1,4):

            full_trains = dom.train_recursion(double, dominoes, hand_size)

            multi_trains = []
            multi_starts = [d for d in dominoes if double in d]
            print("multi_starts")
            print(multi_starts)

            if len(multi_starts) > 1:
                for starter in multi_starts:
                    remaining_dominoes = [d for d in dominoes if d not in multi_starts]
                    remaining_dominoes.append(starter)
                    sub_multi_train = dom.train_recursion(double, remaining_dominoes, hand_size)
                    multi_trains += sub_multi_train

            # print("full_trains")
            # print(full_trains)
            # print("multi_trains")
            # print(multi_trains)

            dom.train_output(full_trains, multi_trains)
        
        elif mode == 4:

            full_trains = dom.train_recursion(double, dominoes, hand_size)
            
            print('full_trains')
            print(full_trains)

        elif mode == 5:
            dom.train_output(full_trains, multi_trains)


    except Exception as e:
        raise