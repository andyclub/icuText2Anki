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


def txtConvertor():
	Question = []
	Answer = []
	csvCardCount = 0
	# Set the path to your own note address and note filename
	noteFile = "/Users/ad/Downloads/ToAnki.txt"
	note =  open(noteFile)
	line = " "
	tmp = ""
	while line:
		while line and not('Q：' in line):
			line = note.readline()
		#Got Q:
		while line and not ('A：' in line):
			tmp = tmp + line
			line = note.readline()
		Question.append(tmp)
		tmp = ""
		#Got A:
		while line and not ('______________' in line):
			tmp = tmp + line
			line = note.readline()
		Answer.append(tmp)
		tmp = ""
		csvCardCount = csvCardCount + 1
		line = note.readline()
	note.close()
	# temp csv file
	file = open(noteFile + '_tmp.csv','w')
	i = 0
	while i < len(Question):
		file.write('"' + Question[i]+'",')
		file.write('"' + Answer[i] + '"\n')
		i = i + 1
	file.close()
	return noteFile + '_tmp.csv'

def txtImporter():
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
	ti = TextImporter(mw.col, txtConvertor())
	ti.initMapping()                                
	ti.run()       
	mw.reset()
	CardCount = mw.col.cardCount()
	# show a message box
	showInfo("Cards before import:" + str(oriCardCount) + "\nCards after import:" + str(CardCount))
	
	                                 


action = QAction("txtImporter", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(txtImporter)
# and add it to the tools menu
mw.form.menuTools.addAction(action)



