# put these tests somewhere else with a separate entry point
        elif test_mode == 1:
            # basic test
            double = 1
            hand_size = 5
            dominoes = [[1, 3], [2, 3], [5, 3], [4, 2], [2,2]]

        elif test_mode == 2:
            # full hand/ multi start test
            double = 3
            hand_size = 15
            # these are not the inputs from the picture, correct
            dominoes = [[6,2], [6,4], [6,5], [6,12], [9,2], [9,0], [3,4], [4,11], [2,0], [10,5], [7,3], [0,8], [1,8], [11,8], [11,12]]

        elif test_mode == 3:
            # perfect train test
            print("test doesnt exist yet")

        elif test_mode == 4:
            # forced failure
            0/0