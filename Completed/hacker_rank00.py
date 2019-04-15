#!/bin/python3

import math
import os
import random
import re
import sys



class Muliplication:
    def __init__(self,n):
        self.number = int(n)
    
    def calc(self):
        for multi in range(11):
            print(self.number, "x", multi, "=", (self.number * multi))
        
     


if __name__ == '__main__':
    n = int(input())
    table = Muliplication(n)
    table.calc()
