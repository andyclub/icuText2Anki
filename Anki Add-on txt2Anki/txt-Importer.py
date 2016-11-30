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
	FCard = []
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
		FCard.append([])
		FCard[csvCardCount]=[tmp,'','']
		tmp = ""
		#Got A:
		while line and not ('______________' in line):
			if '[' in line and ']' in line:
				line = line.replace('[','',1)
				line = line.replace(']', '', 1)
				FCard[csvCardCount][2]=line
			else:
				tmp = tmp + line
			line = note.readline()
		FCard[csvCardCount][1]=tmp
		tmp = ""
		csvCardCount = csvCardCount + 1
		line = note.readline()
	note.close()
	# temp csv file
	file = open(noteFile + '_tmp.csv','w')
	for i in (0,len(FCard)-1):
		file.write('"' + FCard[i][0] + '",')
		file.write('"' + FCard[i][1] + '",')
		file.write('"' + FCard[i][2] + '"\n')
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
	showInfo("Cards imported:" + str(CardCount-oriCardCount) + "\n\nCards Count:" + str(CardCount))
	
	                                 


action = QAction("txtImporter", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(txtImporter)
# and add it to the tools menu
mw.form.menuTools.addAction(action)



