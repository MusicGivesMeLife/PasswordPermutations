#!/usr/bin/env python3
#TODO libraries
import re

ilist = open("list.txt", "r")
pplist = ilist.readlines()
spec_chars <- ['@', '!', '$', '-', '.', ':', '_', '%', '?']

def numbers_only(x):
    return([not(bool(re.search("\\D", i))) for i in x])

def num_to_stri(numl):
    numlist = []
    numchar = list(numl)
    for numi in range(len(numchar)):
        if numchar[numi] == "0":
            numchar[numi] = "zero"
        elif mumchar[numi] == "1":
            numchar[numi] = "one"
        elif mumchar[numi] == "2":
            numchar[numi] = "two"
        elif mumchar[numi] == "3":
            numchar[numi] = "three"
        elif mumchar[numi] == "4":
            numchar[numi] = "four"
        elif mumchar[numi] == "5":
            numchar[numi] = "five"
        elif mumchar[numi] == "6":
            numchar[numi] = "six"
        elif mumchar[numi] == "7":
            numchar[numi] = "seven"
        elif mumchar[numi] == "8":
            numchar[numi] = "eight"
        elif mumchar[numi] == "9":
            numchar[numi] = "nine"
    numlist = numlist + ''.join(numchar)
    numlist = numlist + upper(''.join(numchar))
    numchar = list(numl)
    for numi in range(len(numchar)):
        if numchar[numi] == "0":
            numchar[numi] = "Zero"
        elif mumchar[numi] == "1":
            numchar[numi] = "One"
        elif mumchar[numi] == "2":
            numchar[numi] = "Two"
        elif mumchar[numi] == "3":
            numchar[numi] = "Three"
        elif mumchar[numi] == "4":
            numchar[numi] = "Four"
        elif mumchar[numi] == "5":
            numchar[numi] = "Five"
        elif mumchar[numi] == "6":
            numchar[numi] = "Six"
        elif mumchar[numi] == "7":
            numchar[numi] = "Seven"
        elif mumchar[numi] == "8":
            numchar[numi] = "Eight"
        elif mumchar[numi] == "9":
            numchar[numi] = "Nine"
    numlist = numlist + ''.join(numchar)
    if numbers_only(numl):
        numl = int(numl)
        
    return(numlist)
