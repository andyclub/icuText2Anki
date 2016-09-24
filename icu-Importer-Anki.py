#!/usr/bin/python
# encoding:utf-8
import csv

Question = []
Answer = []
file =  open("/Users/ad/Downloads/Anki_ICU_Book.txt")
line =' '
while line :
    line = file.readline()
#    print line
    if 'Q:' in line:
        line = line.replace('\n','')
        if len(line) > 3 :
            Question.append(line)
    if 'A:' in line:
        tmp = line
        while (not line.startswith('\n') ) and line:
            line = file.readline()
            tmp = tmp + line
            tmp = tmp.replace('-',' ')
        if len(tmp) > 3 :
            Answer.append(tmp)
file.close()
i = 0
file = open('//Users/ad/Downloads/Anki_ICU_Book_tmp.csv','w')
while i < len(Question):
    print Question[i]
    print Answer[i]
    print '...........'
    csvfile.write('"' + Question[i]+'",')
    csvfile.write('"' + Answer[i] + '"\n')
    i = i + 1
file.close()
