#!/usr/bin/python
# encoding:utf-8

# this can be use as add-on in Anki

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

from anki.importing import TextImporter

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.


def icuConvertor():
	Question = []
	Answer = []
	csvCardCount = 0
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
	        csvCardCount = csvCardCount + 1
	    # get answer by token 'A:', with Markdown '-', support muti-lines
	    if 'A:' in line:
	        tmp = line
	        while (not line.startswith('\n') ) and line:
	            line = file.readline()
	            # apply to the markdown
	            while line.startswith('-'):
	                line = line.replace('-','   ',1)
	            tmp = tmp + line
	        if len(tmp.strip()) > 3 :
	            Answer.append(tmp)
	file.close()
	# temp file
	file = open(noteFile + '_tmp.csv','w')
	i = 0
	print 'Q&A writing into csv file, casds like this:'
	while i < len(Question):
	    file.write('"' + Question[i]+'",')
	    file.write('"' + Answer[i] + '"\n')
	    i = i + 1
	file.close()
	showInfo("Converted cards:" + str(csvCardCount))
	return noteFile + '_tmp.csv'

def icuImporter():
	##select deck     
	# Modify to your own destination deck                               
	did = mw.col.decks.id("Test")                   
	mw.col.decks.select(did)                        
	# set note type for deck                        
	m = mw.col.models.byName("Basic")               
	deck = mw.col.decks.get(did)                    
	#deck['mid'] = m['id']                           
	mw.col.decks.save(deck)  
	# import into the collection
	oriCardCount = mw.col.cardCount()
	ti = TextImporter(mw.col, icuConvertor())                 	
	ti.initMapping()                                
	ti.run()       
	mw.reset()
	CardCount = mw.col.cardCount()
	# show a message box
	showInfo("Cards before import:" + str(oriCardCount) + "\nCards after import:" + str(CardCount))
	
	                                 


action = QAction("icuImporter", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(icuImporter)
# and add it to the tools menu
mw.form.menuTools.addAction(action)



