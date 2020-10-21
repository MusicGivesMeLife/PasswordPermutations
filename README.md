# PasswordPermutations

## Requirements (R)
* R installation (RStudio is easiest to use)
* R packages: data.table, stringi, Hmisc

## Requirements (P)
* Python 3 installation, tested on 3.8
* Python packages: re, inflect

## Processes
* Adds separator characters ('@', '!', '$', '-', '.', ':', '_', '%', '?')
* Converts integer numbers into word equivalents
* Assembles all possible combinations of listed items

## Input
* list.txt - list of terms to process, one item per line

## Output
* PPMaster_R.txt - output when R version run
* PPMaster_P.txt - output when Python version run
