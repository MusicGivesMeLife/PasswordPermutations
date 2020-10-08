#!/usr/bin/env python3
#TODO libraries
import re

ilist = open("list.txt", "r")
pplist = ilist.readlines()
spec_chars = ['@', '!', '$', '-', '.', ':', '_', '%', '?']

def num_to_stri(numl):
    numlist = []
    numchar = list(numl)
    for numi in range(len(numchar)):
        if numchar[numi] == "0":
            numchar[numi] = "zero"
        elif numchar[numi] == "1":
            numchar[numi] = "one"
        elif numchar[numi] == "2":
            numchar[numi] = "two"
        elif numchar[numi] == "3":
            numchar[numi] = "three"
        elif numchar[numi] == "4":
            numchar[numi] = "four"
        elif numchar[numi] == "5":
            numchar[numi] = "five"
        elif numchar[numi] == "6":
            numchar[numi] = "six"
        elif numchar[numi] == "7":
            numchar[numi] = "seven"
        elif numchar[numi] == "8":
            numchar[numi] = "eight"
        elif numchar[numi] == "9":
            numchar[numi] = "nine"
    numlist.append(''.join(numchar))
    numlist.append(''.join(numchar).upper())
    numchar = list(numl)
    for numi in range(len(numchar)):
        if numchar[numi] == "0":
            numchar[numi] = "Zero"
        elif numchar[numi] == "1":
            numchar[numi] = "One"
        elif numchar[numi] == "2":
            numchar[numi] = "Two"
        elif numchar[numi] == "3":
            numchar[numi] = "Three"
        elif numchar[numi] == "4":
            numchar[numi] = "Four"
        elif numchar[numi] == "5":
            numchar[numi] = "Five"
        elif numchar[numi] == "6":
            numchar[numi] = "Six"
        elif numchar[numi] == "7":
            numchar[numi] = "Seven"
        elif numchar[numi] == "8":
            numchar[numi] = "Eight"
        elif numchar[numi] == "9":
            numchar[numi] = "Nine"
    numlist.append(''.join(numchar))
    if ''.join(numl).isdecimal():
        numl = int(''.join(numl))
        
    return(numlist)
