#! /usr/bin/env python


#ShellTODO v.0.8.5
#author: Adrian7 (http://adrian.silimon.eu)

import sys, getopt, codecs
from os.path import expanduser

#-------- Settings -------#
AUTOSAVE = True  					#Auto-Save edits to file: True/False 
AUTOLOAD = True					#Auto-Load the todo list file: True/False
SHELLONLY=True					#After executing a command from shell, the script should get back to shell?: True/False
HOMEDIR = expanduser("~")			#The basedir to determine the todo list file location
OUTFILE  = HOMEDIR + "/todo.list"	#The path to the todo list file, you can set here an absolute path (e.g. '/var/todo.list') 
#-------- Settings -------# 

VER	 = "0.8.5"
TODOList = []


def doautosave():
	"Checks if AUTOSAVE option is enabled and saves the current todolist to the OUTFILE"

	if(AUTOSAVE):
		save()


def add(item, asinput='file'):
	"Adds a new item in the current todolist"
	
	global TODOList

	TODOList.append(unicode(item.strip(), 'utf-8'))

	if (asinput != 'file'): 
		doautosave()


def view(index):
	"Shows a single item from the TODO List"

	global TODOList

	if (len(TODOList) == 0): 
		return

	print "#"+str(index+1), TODOList[index]


def complete(index):
	"Marks an item as complete"
	
	global TODOList

	if (len(TODOList) == 0): 
		return

	if (index <= 0):
		print "Oups: no such index ", index
		return

	TODOList[index-1] += u' \u2713'

	doautosave()


def save():
	"Saves the TODO List to a file"

	out = codecs.open(OUTFILE, mode="w", encoding="utf-8")

	global TODOList;

	if(AUTOLOAD):
		out.seek(0)
		out.truncate()

	for single in TODOList:
		out.write(single + "\n")

	print "File", OUTFILE, "saved."

	out.seek(0)
	out.close()


def load(showerr=True):
	"Loads the default TODO list from file"

	if(showerr):
		print "Loading file", OUTFILE

	try:
		fin = codecs.open(OUTFILE, mode="r", encoding="utf-8")

		global TODOList;

		for line in fin.readlines():
			add(line.encode("utf-8"))

		print "File", OUTFILE, "loaded."

		fin.seek(0)
		fin.close()

	except IOError as ie:
		if(showerr):
			print "File",  OUTFILE, "is missing!"


def delete(index):
	"Removes an item from the TODO List"
	
	global TODOList

	del(TODOList[index])

	doautosave()


def clearlist():
	"Clears the entire todo list"

	global TODOList;

	TODOList = []

	doautosave()


def show():
	"Displays the entire TODO List"

	global TODOList

	if (len(TODOList) == 0): 
		return

	print "------- TODO List -------"

	for index in range(len(TODOList)): 
		print "#"+str(index+1), TODOList[index]

	print "-------------------------"


def print_header():
	print "======= ShellTODO version", VER, "======="


def print_help():
	print_header()	
	print "Help section:"
	print "Commands (works both uppercase or lowercase): "
	print "S : Shows the entire TODO list"
	print "A : Add a new item in the list"
	print "X : Clear the entire list"
	print "V : View a single item from the list"
	print "M : Mark an item as complete"
	print "F : Save the list to file"
	print "L : Load the list from file, items will be added to the current list"
	print "D : Delete an item from the list"
	print "H : Displays this help section"
	print "C : Credits section"
	print ""
	print "Example usage from command line: "
	print "$./todo.py -a 'Todo item' -q: add a new item, then quit"
	print "$./todo.py -rsq : load the list from the file, show it, then bye (back to shell)"
	print "$./todo.py -rm 1 -q: read from file, mark first item as completed, then quit"


def print_credits():
	print_header()	
	print "Credits:"
	print "author: Adrian7: http://adrian.silimon.eu/"
	print "github: comming soon"


action 	 = None
commands = []

if(AUTOLOAD): 
	load(False) 

if ( len(sys.argv) < 2 ):

	print_header()	
	print "Press H for help"
	print "Commands: \n S=show \n V=view \n A=add \n D=delete \n F=save to file \n R=load from file \n M=mark as complete \n H=help \n C=credits \n Q=exit"

else:

	try:
	
		commands, args = getopt.getopt(sys.argv[1:], "hcsfrxqm:a:v:d:")

		for cmd, arg in commands:

			if(cmd in ("-h", "-H")):
				print_help()
			elif(cmd in ("-c", "-C")):
				print_credits()
			elif(cmd in ("-r", "-R")):
				load()
			elif(cmd in ("-a", "-A")):
				add(str(arg), 'shell')
			elif(cmd in ("-m", "-M")):
				complete(int(arg))
			elif(cmd in ("-d", "-D")):
				delete(int(arg))
			elif(cmd in ("-x", "-X")):
				clearlist()
			elif(cmd in ("-s", "-S")):
				show()
			elif(cmd in ("-f", "-F")):
				save()
			elif(cmd in ("-q", "-Q")):
				sys.exit()
			else:
				print "Unrecognized command: "
				print "Type -h for help."
			

	except getopt.GetoptError as ge:
		print "Unrecognized command: ", ge
		print "Type -h for help."
		sys.exit(2)
	except ValueError as ve:
		print "Invalid number for argument: ", ve
		sys.exit(2)


if(SHELLONLY):
	sys.exit()


while 1:

	try:
		if (action == None):
			action = str(raw_input("CMD: "))

		if(action in ["S", 's']):
			show()
		elif(action in ["V", "v"] ):
			index = int(raw_input("Index: "))
			view(index)
		elif(action in ["A", "a"]):
			item = str(raw_input("Task: "))
			add(item, 'shell')
		elif(action in ["D", "d"]):
			index = int(raw_input("Index: "))
			delete(index)
		elif(action in ["X", "x"]):
			clearlist()
		elif(action in ["M", "m"]):
			index = int(raw_input("Index: "))
			complete(index)
		elif(action in ["F", "f"]):
			save()
		elif(action in ["R", "r"]):
			load()
		elif(action in ["Q", "q"]):
			break
		elif(action in ["H", "h"]):
			print_help()
		elif(action in ["C", "c"]):
			print_credits()
		else:
			show()
	
		action = None

	except  KeyboardInterrupt as ki:
		print "Bye!"
		sys.exit()


