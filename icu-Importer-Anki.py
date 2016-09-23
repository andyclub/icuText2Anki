#!/usr/bin/python
# encoding:utf-8
import re

Question = []
Answer = []
file =  open("/Users/ad/Downloads/Anki_ICU_Book.txt")
line =' '
while line :
    line = file.readline()
#    print line
    if 'Q:' in line:
        Question.append(line)
    if 'A:' in line:
        tmp = ''
        while (not line.startswith('\n') ) and line:
            line = file.readline()
            tmp = tmp + line
            tmp = tmp.replace('-',' ')
        Answer.append(tmp)
file.close()
i = 0
while i < len(Question):
    print Question[i]
    print Answer[i]
    print '...........'
    i =i+1

