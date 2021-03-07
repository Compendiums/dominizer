import argparse
import json
import logging
import os

from datetime import datetime

from dominizer import dominizer
from tests import tests


# globals
DIR = os.path.dirname(os.path.abspath(__file__))

def main():

    try:
        # user input
        if test_mode == 0:
            while True:
                try:
                    double = int(input('Enter the number on your starting double: \n'))

                    if double < 0 or double > 18:
                        print("dominoes only go from 0 to 18. Try again...")
                        continue

                except ValueError:
                    print("That doesn't look like a number to me. Try again...")
                    continue
                else:
                    # parse was successful, exit loop
                    break
                
            while True:
                try:
                    hand_size = int(input("How many dominoes are in your hand? \n"))

                    if hand_size < 0 or hand_size > 190:
                        print("dominoes sets only have up to 190 pieces and I KNOW you didn't buy the expansion pack.")
                        continue

                except ValueError:
                    print("That doesn't look like a number to me. Try again...")
                    continue
                else:
                    # parse was successful, exit loop
                    break

            dominoes = []
            for i in range(hand_size):
                dominoe = [int(i) for i in input("Enter dominoe " + str(i+1) + " as x,y: \n").split(",")]
                #print(dominoe)
                dominoes.append(dominoe)

        # hardcoded input
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


        dom = dominizer()

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

    except Exception as e:
        raise



if __name__ == '__main__':
    
    start_time = datetime.now()
    timestamp = start_time.strftime("%y-%m-%d_%H:%M:%S")
    
    with open(os.path.join(DIR,'config\config.json')) as f:
        config = json.load(f)

    log_dir = os.path.join(DIR, config['log_dir'])
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    #set log filename
    config['log_config']['handlers']['file']['filename'] = f'log_{timestamp}.log'
    logging.config.dictConfig(config['log_config'])

    logger = logging.getLogger("first_log")
    logger.info("testing")

    parser = argparse.ArgumentParser()
    parser.add_argument('--test_mode', type=int, required=False, default=0, help="run app with fixed inputs in test mode")
    _args = parser.parse_args()
    
    
    # eventually
    if _args.test_mode != 0:
        print('in test mode')
        tests.test_selector(_args.test_mode)
    else:
        main()