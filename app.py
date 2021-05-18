import argparse
import json
import logging
import os

from datetime import datetime

from dominizer import dominizer
from log_setup import logger,log_dir,timestamp
from tests import tests


# globals
DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    try:
        while True:
            try:
                double = int(input('Enter the number on your starting double: \n'))

                if double < 0 or double > 18:
                    print("dominoes only go from 0 to 18. Try again...")
                    continue

                logger.info("starting double: " + str(double))

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

                logger.info("hand size: " + str(hand_size))

            except ValueError:
                print("That doesn't look like a number to me. Try again...")
                continue
            else:
                # parse was successful, exit loop
                break

        dominoes = []
        for i in range(hand_size):
            while True:
                try:
                    #  VERIFY THAT THE DOMINOE VALUES ARE POSSIBLE
                    # dominoe = [int(num) for num in input("Enter dominoe " + str(i+1) + " as x,y: \n").split(",") if int(num) >= 0 or int(num) <= 190]
                    dominoe = [int(num) for num in input("Enter dominoe " + str(i+1) + " as x,y: \n").split(",")]
                    if len(dominoe) != 2:
                        print("You only entered one dominoe value. Try again...")
                        continue
                    
                    if dominoe_value_check(dominoe):
                        if dominoe_dupe_check(dominoe=dominoe,dominoes=dominoes):
                            dominoes.append(dominoe)
                        else:
                            print("you already entered that dominoe. Try again...")
                            continue
                    else:
                        print("That number doesn't look right. Try counting those dots again...")
                        continue

                    #print(dominoe)
                    
                except ValueError:
                    print("that doesn't look like a number to me. Try again...")
                else:
                    # parse was successful, exit loop
                    break

        logger.info("starting hand:")
        logger.info(dominoes)

        dom = dominizer()

        logger.info("entering full_trains")
        full_trains = dom.train_recursion(double, dominoes, hand_size)

        multi_trains = []
        multi_starts = [d for d in dominoes if double in d]
        logger.info("multi_starts:")
        logger.info(multi_starts)

        if len(multi_starts) > 1:
            for starter in multi_starts:
                logger.info("entering multi_train for " + str(starter))
                remaining_dominoes = [d for d in dominoes if d not in multi_starts]
                remaining_dominoes.append(starter)
                sub_multi_train = dom.train_recursion(double, remaining_dominoes, hand_size)
                multi_trains += sub_multi_train

        # print("full_trains")
        # print(full_trains)
        # print("multi_trains")
        # print(multi_trains)

        logger.info("generating output")
        dom.train_output(full_trains, multi_trains)

    except Exception as e:
        logger.exception("failure in main")
        raise

def dominoe_value_check(dominoe):
    for num in dominoe:
        if int(num) < 0 or int(num) > 190:
            return False
    else:
        return True

def dominoe_dupe_check(dominoe, dominoes):
    for previous in dominoes:
        if sorted(previous) == sorted(dominoe):
            return False
    else:
        return True

if __name__ == '__main__':

    with open(os.path.join(DIR,'config\config.json')) as f:
        config = json.load(f)

    main()