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


def icu-Importer():
#	file = u"/Users/ad/Downloads/Anki_ICU_Book.txt" 
	##select deck                                   
	did = mw.col.decks.id("Test")                   
	mw.col.decks.select(did)                        
	# set note type for deck                        
	m = mw.col.models.byName("Basic")               
	deck = mw.col.decks.get(did)                    
	deck['mid'] = m['mid']                           
	mw.col.decks.save(deck) 
	                        
	# get icu note question & answer
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
	                        
	# import into the collection                    
	ti = TextImporter(mw.col, '//Users/ad/Downloads/Anki_ICU_Book_tmp.csv')                 
	
	ti.initMapping()                                
	ti.run()                                        


action = QAction("icu-Importer", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(icu-Importer)
# and add it to the tools menu
mw.form.menuTools.addAction(action)



