#!/usr/bin/env Rscript
library('data.table')
library('stringi')
library('Hmisc')

rawp <- readLines('./list.txt')
spec_chars <- c('@', '!', '$', '-', '.', ':', '_', '%', '?')
pplist <- c(rawp)

for (i in 1:length(rawp)){
  l <- rawp[i]
  l <- gsub(' ', '', l)
  if (grepl('\\d', l)) {
    l <- as.integer(l)
    for(inc in 1:5) {
      pplist <- c(pplist, toString(l+inc))
      pplist <- c(pplist, toString(l-inc))
    }
    l <- toString(l)
  }
  else {
    pplist <- c(pplist, toupper(l))
    pplist <- c(pplist, tolower(l))
    pplist <- c(pplist, capitalize(l))
  }
  pplist <- c(pplist, stri_reverse(l))
}
pplist <- unique(pplist)
for (i in 1:length(pplist)){
  l <- pplist[i]
  for(specc in spec_chars) {
    pplist <- c(pplist, paste(l, specc, sep=''))
  }
}
pplist2 <- c()
for (i in 1:length(pplist)){
  l <- pplist[i]
  for(i2 in 1:length(pplist[!(pplist==l)])) {
    subpp <- pplist[!(pplist==l)]
    pplist2 <- c(pplist2, paste(l, subpp[i2], sep=''))
  }
}
pplist <- unique(c(pplist, pplist2))
write.table(data.table(pplist), './PPMaster.txt', col.names = FALSE, row.names = FALSE, quote = FALSE)