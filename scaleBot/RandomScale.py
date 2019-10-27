#!/usr/bin/python3

"""
ScaleBot, a little bot who ust wants to help you practice

This program supports all sorts of scales: classical, jazz or custom scales.

Created by request of Zane Sereda
Created by Ethan Sengs
Contact me on Twitter! @potatoPetiole
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
import random

#filepath = str(raw_input("Enter file path: "))

keysAvailable = ["A","B","C","D","E","F","G"]
keysSelected = []

keysSelected += keysAvailable

sharpFlatAvailable = ["","b","#"]
sharpFlatSelected = []

sharpFlatSelected += sharpFlatAvailable

scalesEnabled = True
scalesAvailable = ["major",
	"minor harmonic",
	"minor melodic",
	"major in octaves",
	"major in 3rds",
	"major in 6ths",
	"minor in octaves",
	"minor in 3rds",
	"minor in 6ths"]
scalesSelected = []

chordsEnabled = True
chordsAvailable = ["major four note",
	"minor four note",
	"dominant 7th",
	"diminished 7th"]
chordsSelected = []

chordStylesAvaliable = ["solid", "broken", "arpeggiated"]
chordStylesSelected = []
chordStylesSelected += chordStylesAvaliable

filepath = None

title = "ScaleBot ^_^"

class FileReaderButton:
	
	"""
	The button which says "Load Technique"

	This allows a user to upload files into ScaleBot
	"""

	def __init__(self,master,reader):
		
		self.spot = tk.Frame(master)
		self.button = tk.Button(self.spot,
			text = "Load Technique",
			command = (lambda: reader.findFile(filepath, True)))

	def pack(self, **options):
		sideOption = options.get('side',tk.TOP)

		self.spot.pack(side = sideOption)
		self.button.pack()

class FileReader:
	"""
	The object which actually reads the file that has been uploaded

	This class will categorize the contents of the file as "scales" or "chords"
	"""
	def findFile(self,filepath, triggered = False):

		self.openedFile = None

		if (filepath == "") or (triggered == True):

			root.update()
			filepath = str(askopenfilename())
		
		if not (filepath == None):
			self.openedFile = open(filepath,"r")
			self.parseFile()
	
	def pack(self, **options):
		sideOption = options.get('side',tk.TOP)

		self.spot.pack(side = sideOption)
		self.button.pack()

	def parseFile(self):

		global chordsAvailable
		global scalesAvailable

		chordsAvailable = []
		scalesAvailable = []

		self.content = []
		self.chords = []
		self.scales = []
		
		if not (self.openedFile == None):
			for i in self.openedFile:
				self.content += [i]

		chordsAvailable = self.giveChords()
		scalesAvailable = self.giveScales()

	def giveChords(self):

		endOfParse = 0

		if (self.content.index("}\n") <= self.content.index("chords:{\n")):
			if ("}" in self.content):
				endOfParse = self.content.index("}")
			else:
				endOfParse = len(self.content) - (1 + self.content[::-1].index("}\n"))
		else:
			endOfParse = self.content.index("}\n")

		for i in self.content[self.content.index("chords:{\n") + 1:endOfParse]:
			self.chords.append(''.join(i.split("\n")))
		#print("chords",self.chords)

		#self.chords.pop(self.chords.index("chords:{"))
		#self.chords.pop(self.chords.index("}"))

		return self.chords

	def giveScales(self):

		endOfParse = 0

		if (self.content.index("}\n") <= self.content.index("scales:{\n")):
			if ("}" in self.content):
				endOfParse = self.content.index("}") - 1
			else:
				endOfParse = len(self.content) - (1 + self.content[::-1].index("}\n"))
		else:
			endOfParse = self.content.index("}\n") - 1

		for i in self.content[self.content.index("scales:{\n") + 1:endOfParse]: 
			self.scales.append(''.join(i.split("\n")))
		#print("scales",self.scales)

		#self.scales.pop(self.scales.index("scales:{"))
		#self.scales.pop(self.scales.index("}"))

		return self.scales

	def pack(self, **options):
		sideOption = options.get('side',tk.TOP)

		self.spot.pack(side = sideOption)
		self.button.pack()

class Print:

	"""
	Not to be confused with the actual print function within Python

	This class is the actual text that is present on the app.
	Within it, it randomizes the scale or chord to play, along with the key to 
	play it in.
	"""

	def __init__(self, master):
		
		self.master = master

		self.spot = tk.Frame(master)

		self.printScaleLabel = tk.Label(self.spot,text = title,
			font = ("Courier", 32))
		
		self.subWindow = None

	def newScale(self):
		
		printMe = "Ranomizing..."
		
		key = str(keysSelected[random.randint(0,len(keysSelected) - 1)]+
			sharpFlatSelected[random.randint(0,len(sharpFlatSelected) - 1)])
		scale = str(scalesSelected[random.randint(0,len(scalesSelected) - 1)])
		
		###TODO Fix this boi
		if (len(sharpFlatSelected) == 3):
			if (key == "Fb"):
				key = "E"
#				print("Would've been Fb!")
			if (key == "E#"):
				key = "F"
#				print("Would've been E#!")
			if (key == "Cb"):
				key = "B"
#				print("Would've been Cb!")
			if (key == "B#"):
				key = "C"
#				print("Would've been B#!")

		printMe = str(key + " " + scale + " scale")
		self.printScaleLabel.config(text = printMe)

 #	   print(printMe) #TESTING

	def newChord(self):
		
		printMe = "Ranomizing..."
		
		key = str(keysSelected[random.randint(0,len(keysSelected) - 1)]+
			sharpFlatSelected[random.randint(0,len(sharpFlatSelected) - 1)])
		chord = str(chordsSelected[random.randint(0,len(chordsSelected) - 1)])
		style = str(chordStylesSelected[random.randint(0,len(chordStylesSelected) - 1)])
		
		if (len(sharpFlatSelected) == 3):
			if (key == "Fb"):
				key = "E"
#				print("Would've been Fb!")
			if (key == "E#"):
				key = "F"
#				print("Would've been E#!")
			if (key == "Cb"):
				key = "B"
#				print("Would've been Cb!")
			if (key == "B#"):
				key = "C"
#				print("Would've been B#!")

		printMe = str(key + " " + chord + " chord, " + style)
		self.printScaleLabel.config(text = printMe)

#		print(printMe) #TESTING
	
	def error(self):

		errorMessage = "\nAn error has occurred:\n"

		if (len(sharpFlatSelected) < 1):
			errorMessage += "Enable at least one: Sharps, Flats or Naturals\n"

		if (len(keysSelected) < 1):
			errorMessage += "Enable at least one key\n"

		if (len(scalesSelected) < 1) and (len(chordsSelected) < 1):
			errorMessage += "Enable at least one chord or scale\n"

		if (len(chordStylesSelected) < 1) and (len(chordsSelected) >= 1):
			errorMessage += "Chord Sequence (Broken, Solid, Arpeggiated)\n"

		if (len(scalesAvailable) == 0) and (len(chordsAvailable) == 0):
			errorMessage += "Upload a file containing the technique\n"

		self.printScaleLabel.config(text = "Whoops!")

		self.CreateWindow(errorMessage)

	def CreateWindow(self,message):

		if (self.subWindow == None) or (tk.Toplevel.winfo_exists(self.subWindow) == 0):
			self.subWindow = tk.Toplevel(self.master)
			self.subWindow.title("Error!")
#		   self.window = OptionsMenu(root,ScalesPrintObject)
#		   self.window.pack()
			self.PopulateWindow(message)
		else:
			self.subWindow.lift(self.master)

	def PopulateWindow(self,message):

		self.content = tk.Label(self.subWindow,text = message)
		self.content.pack()

	def pack(self,**options):
		
		sideOption = options.get('side',tk.TOP)

		self.spot.pack(side = sideOption)
		self.printScaleLabel.pack()

class CleanUp:

	"""
	This class does two things: adds whitespace and ensures the dimensions of 
	the window are maintained.
	"""

	def __init__(self, master):
		self.blank = tk.Frame(master, width = 900, height = 200)

	def pack(self):
		self.blank.pack()

class GenerateButton:

	ScalesPrintObject = None

	def __init__(self, master, ScalesPrinter):

		def GeneratePress():
			
			if (len(keysSelected) > 0) and (len(sharpFlatSelected) > 0):
				if (len(scalesSelected) > 0) and (len(chordsSelected) > 0) and (len(chordStylesSelected) > 0):
					if (random.randint(0,1)):
						ScalesPrintObject.newScale()
					else:
						ScalesPrintObject.newChord()
				elif (len(scalesSelected) > 0):
					ScalesPrintObject.newScale()
				elif (len(chordsSelected) > 0) and (len(chordStylesSelected) > 0): 
					ScalesPrintObject.newChord()
				else:
					ScalesPrintObject.error()
			else:
				ScalesPrintObject.error()
			#print(scalesEnabled)

		def KeyGeneratePress(event):

	#	   print(str(event))
			
			GeneratePress()
				
		ScalesPrintObject = ScalesPrinter
		
		self.spot = tk.Frame(master)

		self.generate = tk.Button(self.spot, text = "Generate New Scale",
			command = GeneratePress)

		master.bind("<space>", KeyGeneratePress)

	def pack(self,**options):
		
		sideOptions = options.get("side", tk.TOP)

		self.spot.pack(side = sideOptions)
		self.generate.pack()

class AboutButton:
	
	"""
	Wow wow!

	Opens another window to say the credits!
	"""
	def __init__(self,master):

		self.subWindow = None
		self.master = master

		def LaunchWindow():
			
			self.CreateWindow()

		self.spot = tk.Frame(self.master)
		self.credits = tk.Button(self.spot, text = "About",
			command = LaunchWindow)

	def CreateWindow(self):

		creditsStuff = str("\n" +
			"To use this program, please\n" +
			"start feeding me some different\n" +
			"scales and chords with the\n" +
			"\"load technique\" button! :)\n" +
			"_______________________________\n" + 
			"Example:\n" +
			"chords:{\n" +
			"major four note\n" +
			"minor four note\n" +
			"dominant 7th\n" +
			"diminished 7th\n" +
			"}\n" +
			"\n" +
			"scales:{\n" +
			"major\n" +
			"minor harmonic\n" +
			"minor melodic\n" +
			"major in octaves\n" +
			"major in 3rds\n" +
			"major in 6ths\n" +
			"}\n" +
			"_______________________________\n" + 
			"\n" +  
			"Commissioned by Zane Sereda\n" +
			"Made by Ethan Sengavang\n" +
			"Interested in making something?\n" +
			"Or found a pesky bug?\n"
			"Contact me at:\n" +
			"eth.sengsavang@gmail.com :)\n")

		if (self.subWindow == None) or (tk.Toplevel.winfo_exists(self.subWindow) == 0):
			self.subWindow = tk.Toplevel(self.master)
			self.subWindow.title("About")
			self.content = tk.Label(self.subWindow, text = creditsStuff)
			self.content.pack()
		else:
			self.subWindow.lift(self.master)

	def pack(self,**options):

		sideOptions = options.get("side",None)

		self.spot.pack(side = sideOptions)
		self.credits.pack()

class OptionsButton:

	"""
	This button is the button to open up the options menu,where a user would be 
	able to specify which things to practice.
	"""

	def __init__(self,master):

		self.subWindow = None
		self.master = master
		
		self.spot = tk.Frame(self.master)
		self.options = tk.Button(self.spot, text = "Options",
			command = (lambda: self.CreateWindow()))

	def CreateWindow(self):

		if (self.subWindow == None) or (tk.Toplevel.winfo_exists(self.subWindow) == 0):
			self.subWindow = tk.Toplevel(self.master)
			self.subWindow.title("Options")
#		   self.window = OptionsMenu(root,ScalesPrintObject)
#		   self.window.pack()
			self.PopulateWindow()
		else:
			self.subWindow.lift(self.master)

	def PopulateWindow(self):

		self.content = OptionsMenu(self.subWindow)
		self.content.pack()

	def pack(self,**options): 

		sideOptions = options.get('side',tk.TOP)

		self.spot.pack(side = sideOptions)
		self.options.pack()

class OptionsMenu:

	"""
	This class open up the window for a user to the options menu

	Here, they can enable or disable specific technique they would or would not want to practice.
	"""

	def __init__(self,master):
		
		self.keyOptions = KeyOptions(master)
		self.scaleOptions = ScaleOptions(master, scalesAvailable,
			scalesSelected, "Scales:")
		self.chordOptions = ChordOptions(master)#, chordsAvailable, chordsSelected, "Chords:")
		
		#print(scalesSelected, scalesAvailable)

	def pack(self):

		self.keyOptions.pack(side = tk.LEFT, anchor = tk.N)
		self.scaleOptions.pack(side = tk.LEFT, anchor = tk.N)
		self.chordOptions.pack(side = tk.LEFT, anchor = tk.N)

class EntityChecker(object):
	"""
	Creates a checkbox for every option avaliable in any "Avaliable" list given, placing every option into a local listbox (done in __init__)
	It will then add or remove entities from the "Selected" list according to a choice (done in update)
	"""
	def __init__(self, master, availableList, selectedList, title, **options):

		boxHeight = options.get("height", 10)

		self.spot = tk.Frame(master)
		self.title = tk.Label(self.spot, text = title)

		self.returnedList = []
		self.availableList = availableList
		
		self.location = tk.Frame(self.spot, bd = 2,relief = tk.RIDGE)
		self.scroll = tk.Scrollbar(self.location)
		self.box = tk.Listbox(self.location,selectmode = "multiple",bd = 0,
			exportselection = False, height = boxHeight)

		self.box.bind("<<ListboxSelect>>",lambda event: self.update())

		for entity in availableList:
			self.box.insert(tk.END, str(entity))

		for i in availableList:
			if not (i in selectedList):
				#print(str(i) + " NOT IN LIST")
				self.box.selection_set(availableList.index(i))
			
	def update(self):
	   
		self.returnedList = []

		for i in self.availableList:
			self.returnedList += [i]

		#print("\n[ACTIVATED]")
		#print("IN : " + str(self.__class__.__name__))
		#print("availableList:", self.availableList,len(self.availableList))
		#print("before:",self.returnedList,len(self.returnedList))

		for i in self.availableList:
			#print("<PARSING : " + str(i) + ">")
			if (self.availableList.index(i) in self.box.curselection()):
				self.returnedList.remove(i)

		self.refresh()
#		if (isinstance(self, 

	def pack(self, **options):
		
		sideOption = options.get("side", tk.TOP)
		anchorOption = options.get("anchor", tk.N)

		self.spot.pack(side = sideOption, anchor = anchorOption) 
		self.title.pack(anchor = tk.W)
	   
		self.location.pack(side = sideOption, anchor = anchorOption)
		
		self.scroll.pack(side = tk.RIGHT, fill = tk.Y)
		self.box.config(yscrollcommand = self.scroll.set)
		self.scroll.config(command = self.box.yview)
		
		self.box.pack()

class KeyOptions(EntityChecker):
	
	"""
	User is able to choose which keys they would like to play

	This includes whether they wish to play keys starting on a sharp/flat
	"""
	def __init__(self, master, **options):
		
		keyOption = options.get("key", False)

		self.returnedList = []

		self.spot = tk.Frame(master)
		self.title = tk.Label(self.spot, text = "Keys:")

		self.location = tk.Frame(self.spot, bd = 0, relief = tk.SUNKEN)
		self.boxKeys = tk.Listbox(self.location, 
			selectmode = "multiple", 
			bd = 1, 
			relief = tk.SUNKEN, 
			height = len(keysAvailable), 
			exportselection = False)
		#self.boxKeys.config()

		self.boxSharpFlat = tk.Listbox(self.location, 
			selectmode = "multiple", 
			bd = 1, 
			relief = tk.SUNKEN, 
			height = len(sharpFlatAvailable), 
			exportselection = False)

		self.boxKeys.bind("<<ListboxSelect>>", (lambda event: self.update()))
		self.boxSharpFlat.bind("<<ListboxSelect>>", (lambda event: self.update()))

		for entity in keysAvailable:
			self.boxKeys.insert(tk.END, str(entity))
		for i in keysAvailable:
			if not (i in keysSelected):
				self.boxKeys.selection_set(keysAvailable.index(i))

		for entity in sharpFlatAvailable:
			if (entity == ""):
				entity = "natural"
			self.boxSharpFlat.insert(tk.END, str(entity))
		for i in sharpFlatAvailable:
			if not (i in sharpFlatSelected):
				self.boxSharpFlat.selection_set(sharpFlatAvailable.index(i))

	def update(self):

		self.returnedKeyList = []
		self.returnedSharpFlatList = []

		for i in keysAvailable:
			self.returnedKeyList += [i]

		for i in sharpFlatAvailable:
			self.returnedSharpFlatList += [i]

		#print("\n[ACTIVATED]")
#		print("IN : " + str(self.__class__.__name__))
#		print("availableList:", self.availableList,len(self.availableList))
		#print("before:")
		#print(self.returnedKeyList,len(self.returnedKeyList))
		#print(self.returnedSharpFlatList,len(self.returnedSharpFlatList))

		for i in keysAvailable:
			#print("<PARSING : " + str(i) + ">")
			if (keysAvailable.index(i) in self.boxKeys.curselection()):
				self.returnedKeyList.remove(i)

		for i in sharpFlatAvailable:
			#print("<PARSING : " + str(i) + ">")
			if (i == "natural") and (sharpFlatAvailable.index(i) in self.boxSharpFlat.curselection()):
				self.returnedSharpFlatList.remove("")
			elif (sharpFlatAvailable.index(i) in self.boxSharpFlat.curselection()):
				self.returnedSharpFlatList.remove(i)
		
		#print("after:", self.returnedKeyList,":",len(self.returnedKeyList))

		self.refresh()
		
	def refresh(self):
		
		global keysSelected
		global sharpFlatSelected

		keysSelected = []
		sharpFlatSelected = []

		for i in self.returnedKeyList:
			keysSelected += [i]
		for i in self.returnedSharpFlatList:
			sharpFlatSelected += [i]

		#print("Keys:", keysSelected, len(keysSelected), len(keysAvailable))
		#print("Sharps and Flats:", sharpFlatSelected,len(sharpFlatSelected))

	def pack(self, **options):

		sideOption = options.get("side",tk.TOP)
		anchorOption = options.get("anchor",tk.N)

		self.spot.pack(side = sideOption, anchor = anchorOption)
		self.title.pack(anchor = tk.W)

		self.location.pack(side = sideOption, anchor = anchorOption)

		self.boxKeys.pack()
		self.boxSharpFlat.pack()

class ScaleOptions(EntityChecker):
	"""
	User is able to choose which scales, if any, they would like to play
	"""
	def refresh(self):

		global scalesSelected
		scalesSelected = []

		for i in self.returnedList:
			scalesSelected += [i]

		#print("after:", self.returnedList,":",len(self.returnedList))
		#print("Scales:", scalesSelected, len(scalesSelected), len(scalesAvailable))

class ChordOptions(EntityChecker):
	"""
	User is able to choose which chords, if any, they would like to play
	"""
	def __init__(self, master, **options):
		
		keyOption = options.get("key", False)

		self.returnedList = []

		self.spot = tk.Frame(master)
		self.title = tk.Label(self.spot, text = "Chords:")

		self.overalllocation = tk.Frame(self.spot, bd = 0, relief = tk.SUNKEN)
		self.chordsLocation = tk.Frame(self.overalllocation,bd =0)
		self.scroll = tk.Scrollbar(self.chordsLocation)
		self.boxChords = tk.Listbox(
			self.chordsLocation, 
			selectmode = "multiple", 
			bd = 1, 
			relief = tk.SUNKEN, 
			height = 7, 
			exportselection = False)
		#self.boxKeys.config()
		self.boxStyles = tk.Listbox(
			self.overalllocation, 
			selectmode = "multiple", 
			bd = 1, relief = tk.SUNKEN, 
			height = len(chordStylesAvaliable), 
			exportselection = False)

		self.boxChords.bind("<<ListboxSelect>>", (lambda event: self.update()))
		self.boxStyles.bind("<<ListboxSelect>>", (lambda event: self.update()))

		for entity in chordsAvailable:
			self.boxChords.insert(tk.END, str(entity))
		for i in chordsAvailable:
			if not (i in chordsSelected):
				self.boxChords.selection_set(chordsAvailable.index(i))

		for entity in chordStylesAvaliable:
			self.boxStyles.insert(tk.END, str(entity))
		for i in chordStylesAvaliable:
			if not (i in chordStylesSelected):
				self.boxStyles.selection_set(chordStylesAvaliable.index(i))

	def update(self):

		self.returnedChordsList = []
		self.returnedStyleList = []

		for i in chordsAvailable:
			self.returnedChordsList += [i]

		for i in chordStylesAvaliable:
			self.returnedStyleList += [i]

		#print("\n[ACTIVATED]")
#		print("IN : " + str(self.__class__.__name__))
#		print("availableList:", self.availableList,len(self.availableList))
		#print("before:")
		#print(self.returnedKeyList,len(self.returnedKeyList))
		#print(self.returnedSharpFlatList,len(self.returnedSharpFlatList))

		for i in chordsAvailable:
			#print("<PARSING : " + str(i) + ">")
			if (chordsAvailable.index(i) in self.boxChords.curselection()):
				self.returnedChordsList.remove(i)

		for i in chordStylesAvaliable:
			#print("<PARSING : " + str(i) + ">")
			if (chordStylesAvaliable.index(i) in self.boxStyles.curselection()):
				self.returnedStyleList.remove(i)

		#print(self.returnedStyleList)
		
		#print("after:", self.returnedKeyList,":",len(self.returnedKeyList))

		self.refresh()
		
	def refresh(self):
		
		global chordsSelected
		global chordStylesSelected

		chordsSelected = []
		chordStylesSelected = []

		for i in self.returnedChordsList:
			chordsSelected += [i]
		for i in self.returnedStyleList:
			chordStylesSelected += [i]

		#print("Keys:", keysSelected, len(keysSelected), len(keysAvailable))
		#print("Sharps and Flats:", sharpFlatSelected,len(sharpFlatSelected))

	def pack(self, **options):

		sideOption = options.get("side",tk.TOP)
		anchorOption = options.get("anchor",tk.N)

		self.spot.pack(side = sideOption, anchor = anchorOption)
		self.title.pack(anchor = tk.W)

		self.overalllocation.pack(side = sideOption, anchor = anchorOption)
		self.chordsLocation.pack()

		self.scroll.pack(side = tk.RIGHT, fill = tk.Y)
		self.boxChords.config(yscrollcommand = self.scroll.set)
		self.scroll.config(command = self.boxChords.yview)

		self.boxChords.pack()
		self.boxStyles.pack(fill = tk.X)

root = tk.Tk()

root.title(title)
root.minsize(900,50)

whiteSpace1 = CleanUp(root)
whiteSpace2 = CleanUp(root)

text = Print(root)

bottomButtonSpot = tk.Frame(root)

fileReader = FileReader()

generateButton = GenerateButton(root,text)
findFileButton = FileReaderButton(root, fileReader)
optionsButton = OptionsButton(root)
aboutButton = AboutButton(root)

whiteSpace1.pack()
text.pack()
generateButton.pack()
whiteSpace2.pack()

findFileButton.pack(side = tk.LEFT)
optionsButton.pack(side = tk.LEFT)
aboutButton.pack(side = tk.LEFT)

for i in chordsAvailable:
	chordsSelected += [i]

for i in scalesAvailable:
	scalesSelected += [i]

root.mainloop()