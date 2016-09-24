#!/usr/bin/python
# encoding:utf-8

Question,Answer = []
# Set the path to your own note address and note filename
file =  open("/Users/ad/Downloads/Anki_ICU_Book.txt")
line =' '
while line :
    line = file.readline()
    # get Question
    if 'Q:' in line and len(line) > 3:
        # just support single line question
        line = line.replace('\n','')
        Question.append(line)
    # get answer
    if 'A:' in line:
        tmp = line
        while (not line.startswith('\n') ) and line:
            line = file.readline()
            # apply to the markdown
            while line.startswith('-'):
                line = line.replace('-','   ',1)
            tmp = tmp + line
        if len(tmp) > 3 :
            Answer.append(tmp)
file.close()
# set the path to your own not address and a temp file name
file = open('//Users/ad/Downloads/Anki_ICU_Book_tmp.csv','w')
i = 0
while i < len(Question):
#    print Question[i]
#    print Answer[i]
#    print '...........'
    csvfile.write('"' + Question[i]+'",')
    csvfile.write('"' + Answer[i] + '"\n')
    i = i + 1
file.close()