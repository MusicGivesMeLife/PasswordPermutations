#!/usr/bin/env python3
#TODO libraries
import re

#TODO read in file

def numbers_only(x):
    return([not(bool(re.search("\\D", i))) for i in x])

def num_to_stri(numl):
    numlist = []
    numchar = numl #TODO type conversion may be needed
    for numi in range(len(numchar)):
        if numchar[numi] == "0":
            numchar[numi] = "zero"
        elif mumchar[numi] == "1":
            numchar[numi] = "one"
    return(numlist)
