## Write a Python program to shuffle and print a specified list.

import random
import math

def randomize_list(list):
    random.shuffle(list)
    print(list)

def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    randomize_list(list)

main()