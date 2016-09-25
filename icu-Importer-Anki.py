#!/usr/bin/python
# encoding:utf-8

<<<<<<< HEAD
Question = []
Answer = []
# Set the path to your own note address and note filename
noteFile ="/Users/ad/Downloads/Anki_ICU_Book.txt"
file =  open(noteFile)
line =' '
while line :
    line = file.readline()
    # get Question by token 'Q:'
    if 'Q:' in line and len(line) > 4:
        # just support single line question
        line = line.replace('\n','')
        Question.append(line)
    # get answer by token 'A:', with Markdown '-', support muti-lines
=======
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
>>>>>>> 8ca89bfb93440ec78695f1513993a2c4d70bcbf2
    if 'A:' in line:
        tmp = line
        while (not line.startswith('\n') ) and line:
            line = file.readline()
            # apply to the markdown
            while line.startswith('-'):
                line = line.replace('-','   ',1)
            tmp = tmp + line
<<<<<<< HEAD
        if len(tmp.strip()) > 3 :
            Answer.append(tmp)
file.close()

# temp file
file = open(noteFile + '_tmp.csv','w')
i = 0
print 'Q&A writing into csv file, casds like this:'
while i < len(Question):
    print Question[i]
    print Answer[i]
    print '...........'
    file.write('"' + Question[i]+'",')
    file.write('"' + Answer[i] + '"\n')
    i = i + 1
file.close()
print 'To import into Anki, the tmp file path & name is: ', noteFile + '_tmp.csv'
=======
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
>>>>>>> 8ca89bfb93440ec78695f1513993a2c4d70bcbf2
