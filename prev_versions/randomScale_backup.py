"""
ScaleBot, a little bot who ust wants to help you practice

This program supports all sorts of scales: classical, jazz or custom scales.

Created by request of Zane Sereda
Created by Ethan Sengs
Contact me on Twitter! @potatoPetiole
"""

#!/usr/bin/python2

import Tkinter as tk
from tkFileDialog import askopenfilename
import random

keysAvaliable = ["A","B","C","D","E","F","G"]
keysSelected = []

keysSelected += keysAvaliable

sharpFlatAvaliable = ["","b","#"]
sharpFlatSelected = []

sharpFlatSelected += sharpFlatAvaliable

scalesEnabled = True
scalesAvaliable = []
scalesSelected = []

chordsEnabled = True
chordsAvaliable = []
chordsSelected = []
chordStylesAvaliable = ["solid", "broken", "arpeggiated"]
chordStylesSelected = []
chordStylesSelected += chordStylesAvaliable

filepath = str(raw_input("Enter file path: "))

title = "ScaleBot ^_^"

class FileReaderButton:
    
    """
    The button which says "Load Technique"

    This allows a user to upload files into ScaleBot
    """

    def __init__(self,master,reader):
        
        self.spot = tk.Frame(master)
        self.button = tk.Button(self.spot, text = "Load Technique", command = reader.findFile(filepath))

    def pack(self, **options):
        sideOption = options.get('side',tk.TOP)

        self.spot.pack(side = sideOption)
        self.button.pack()

class FileReader:
    """
    The object which actually reads the file that has been uploaded

    This class will categorize the contents of the file as "scales" or "chords"
    """
    
    def __init__(self,filepath):

        self.findFile(filepath)

    def findFile(self,filepath):
###TODO custom file reading
        self.openedFile = open(filepath,"r")
#        filepath = str(askopenfilename())
        self.parseFile()
    
    def pack(self, **options):
        sideOption = options.get('side',tk.TOP)

        self.spot.pack(side = sideOption)
        self.button.pack()

    def parseFile(self):
        
        self.content = []
        self.chords = []
        self.scales = []
        
        for i in self.openedFile:
            self.content += [i]

        #print("content", self.content)

    def giveChords(self):

        for i in range(0,self.content.index("scales:{\n") - 1):
            self.chords += [self.content[i].translate(None,'\n')]
        #print("chords",self.chords)

        self.chords.pop(self.chords.index("chords:{"))
        self.chords.pop(self.chords.index("}"))

        return self.chords

    def giveScales(self):

        for i in range(self.content.index("scales:{\n"),len(self.content)):
            self.scales += [self.content[i].translate(None, '\n')]
        #print("scales",self.scales)
        
        self.scales.pop(self.scales.index("scales:{"))
        self.scales.pop(self.scales.index("}"))

        return self.scales

    def pack(self, **options):
        sideOption = options.get('side',tk.TOP)

        self.spot.pack(side = sideOption)
        self.button.pack()

class Print:

    """
    Not to be confused with the actual print function within Python

    This class is the actual text that is present on the app.
    Within it, it randomizes the scale or chord to play, along with the key to play it in.
    """

    def __init__(self, master):
        
        self.master = master

        self.spot = tk.Frame(master)

        self.printScaleLabel = tk.Label(self.spot, text = title, font = ("Courier", 32))
        
        self.subWindow = None

    def newScale(self):
        
        printMe = "Ranomizing..."
        
        key = str(keysSelected[random.randint(0,len(keysSelected) - 1)] + sharpFlatSelected[random.randint(0,len(sharpFlatSelected) - 1)])
        scale = str(scalesSelected[random.randint(0,len(scalesSelected) - 1)])
        
        ###TODO Fix this boi
        if (len(sharpFlatSelected) == 3):
            if (key == "Fb"):
                key = "E"
#                print("Would've been Fb!")
            if (key == "E#"):
                key = "F"
#                print("Would've been E#!")
            if (key == "Cb"):
                key = "B"
#                print("Would've been Cb!")
            if (key == "B#"):
                key = "C"
#                print("Would've been B#!")

        printMe = str(key + " " + scale + " scale")
        self.printScaleLabel.config(text = printMe)

 #       print(printMe) #TESTING

    def newChord(self):
        
        printMe = "Ranomizing..."
        
        key = str(keysSelected[random.randint(0,len(keysSelected) - 1)] + sharpFlatSelected[random.randint(0,len(sharpFlatSelected) - 1)])
        chord = str(chordsSelected[random.randint(0,len(chordsSelected) - 1)])
        style = str(chordStylesSelected[random.randint(0,len(chordStylesSelected) - 1)])
        
        if (len(sharpFlatSelected) == 3):
            if (key == "Fb"):
                key = "E"
#                print("Would've been Fb!")
            if (key == "E#"):
                key = "F"
#                print("Would've been E#!")
            if (key == "Cb"):
                key = "B"
#                print("Would've been Cb!")
            if (key == "B#"):
                key = "C"
#                print("Would've been B#!")

        printMe = str(key + " " + chord + " chord, " + style)
        self.printScaleLabel.config(text = printMe)

#        print(printMe) #TESTING
    
    def error(self):

        errorMessage = "\nEnable at least one from the following categories:\n"

        if (len(sharpFlatSelected) < 1):
            errorMessage += "Sharps, Flats or Naturals\n"

        if (len(keysSelected) < 1):
            errorMessage += "Key\n"

        if (len(scalesSelected) < 1) and (len(chordsSelected) < 1):
            errorMessage += "Chord or Scale\n"

        if (len(chordStylesSelected) < 1) and (len(chordsSelected) >= 1):
            errorMessage += "Chord Sequence (Broken, Solid, Arpeggiated)\n"

        self.printScaleLabel.config(text = "Whoops!")

        self.CreateWindow(errorMessage)

    def CreateWindow(self,message):

        if (self.subWindow == None) or (tk.Toplevel.winfo_exists(self.subWindow) == 0):
            self.subWindow = tk.Toplevel(self.master)
            self.subWindow.title("Error!")
#           self.window = OptionsMenu(root,ScalesPrintObject)
#           self.window.pack()
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
    This class does two things: adds whitespace and ensures the dimensions of the window are maintained.
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

    #       print(str(event))
            
            GeneratePress()
                
        ScalesPrintObject = ScalesPrinter
        
        self.spot = tk.Frame(master)

        self.generate = tk.Button(self.spot, text = "Generate New Scale", command = GeneratePress)

        master.bind("<space>", KeyGeneratePress)

    def pack(self,**options):
        
        sideOptions = options.get("side", tk.TOP)

        self.spot.pack(side = sideOptions)
        self.generate.pack()

class CreditsButton:
    
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
        self.credits = tk.Button(self.spot, text = "Credits", command = LaunchWindow)

    def CreateWindow(self):

        if (self.subWindow == None) or (tk.Toplevel.winfo_exists(self.subWindow) == 0):
            self.subWindow = tk.Toplevel(self.master)
            self.subWindow.title("Credits")
            self.content = tk.Label(self.subWindow, text = "\nCreated by Ethan Sengsavang\n\nCommissioned by Zane Sereda\n")
            self.content.pack()
        else:
            self.subWindow.lift(self.master)

    def pack(self,**options):

        sideOptions = options.get("side",None)

        self.spot.pack(side = sideOptions)
        self.credits.pack()

class OptionsButton:

    """
    This button is the button to open up the options menu,where a user would be able to specify which things to practice.
    """

    def __init__(self,master,ScalesPrintObject):

        self.subWindow = None
        self.master = master
        self.ScalesPrintObject = ScalesPrintObject

        def LaunchWindow():

            self.CreateWindow()
            
        self.spot = tk.Frame(self.master)
        self.options = tk.Button(self.spot, text = "Options", command = LaunchWindow)

    def CreateWindow(self):

        if (self.subWindow == None) or (tk.Toplevel.winfo_exists(self.subWindow) == 0):
            self.subWindow = tk.Toplevel(self.master)
            self.subWindow.title("Options")
#           self.window = OptionsMenu(root,ScalesPrintObject)
#           self.window.pack()
            self.PopulateWindow()
        else:
            self.subWindow.lift(self.master)

    def PopulateWindow(self):

        self.content = OptionsMenu(self.subWindow,self.ScalesPrintObject)
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

    def __init__(self,master,ScalesPrintObject):
        
        self.keyOptions = KeyOptions(master)
        self.scaleOptions = ScaleOptions(master)
        self.chordOptions = ChordOptions(master)
        
        keysSelected = self.keyOptions.keyPopulate.returnedList
        sharpFlatSelected = self.keyOptions.sharpFlatPopulate.returnedList 
        scalesSelected = self.scaleOptions.scalePopulate.returnedList
        chordsSelected = self.chordOptions.chordPopulate.returnedList

    def pack(self):

        self.keyOptions.pack(side = tk.LEFT, anchor = tk.N)
        self.scaleOptions.pack(side = tk.LEFT, anchor = tk.N)
        self.chordOptions.pack(side = tk.LEFT, anchor = tk.N)

class KeyOptions:
    
    """
    User is able to choose which keys they would like to play

    This includes whether they wish to play keys starting on a sharp/flat
    """
    def __init__(self, master):

        self.spot = tk.Frame(master)
        self.title = tk.Label(self.spot, text = "Keys:")
        self.keyPopulate = EntityChecker(self.spot, keysAvaliable, keysSelected)
        self.sharpFlatPopulate = EntityChecker(self.spot, sharpFlatAvaliable, sharpFlatSelected)
        
    def pack(self, **options):

        sideOption = options.get("side",tk.TOP)
        anchorOption = options.get("anchor",tk.N)

        self.spot.pack(side = sideOption, anchor = anchorOption)
        self.title.pack(anchor = tk.W)
        self.keyPopulate.pack(anchor = tk.W, key = True)
        self.sharpFlatPopulate.pack(anchor = tk.W)

class ScaleOptions:
    """
    User is able to choose which scales, if any, they would like to play
    """
    def __init__(self, master):

        self.spot = tk.Frame(master)
        self.title = tk.Label(self.spot, text = "Scales:")
        #self.box = tk.Listbox(self.spot, bd = 0)
        #self.scroll = tk.Scrollbar(self.spot)
        self.scalePopulate = EntityChecker(self.spot, scalesAvaliable, scalesSelected)

    def pack(self,**options):
        
        sideOption = options.get("side", tk.TOP)
        anchorOption = options.get("anchor", tk.N)

        self.spot.pack(side = sideOption, anchor = anchorOption) 
        self.title.pack(anchor = tk.W)
        self.scalePopulate.pack(anchor = tk.W)

class ChordOptions:
    """
    User is able to choose which chords, if any, they would like to play
    """
    def __init__(self, master):

        self.spot = tk.Frame(master)
        self.title = tk.Label(self.spot, text = "Chords:")
        #self.box = tk.Listbox(self.spot, bd = 0)
        self.chordPopulate = EntityChecker(self.spot, chordsAvaliable, chordsSelected)

    def pack(self,**options):
        
        sideOption = options.get("side", tk.TOP)
        anchorOption = options.get("anchor", tk.N)

        self.spot.pack(side = sideOption, anchor = anchorOption)
        self.title.pack(anchor = tk.W)
        #self.box.pack(anchor = tk.W)
        self.chordPopulate.pack(anchor = tk.W)

class EntityChecker:
    """
    Creates a checkbox for every option avaliable in any "Avaliable" list given (done in __init__)
    It will then add or remove entities from the "Selected" list according to a choice (done in update)
    """
    def __init__(self, master, avaliableList, selectedList):

        self.totalEntities = {}
        self.entityVariable = {}
        self.returnedList = []

        for entity in avaliableList:
            self.entityVariable[entity] = (tk.IntVar())
            self.totalEntities[entity] = (tk.Checkbutton(master, text = entity, variable = self.entityVariable[entity], command = (lambda: self.update(selectedList)), onvalue = 1, offvalue = 0))

        for entity in avaliableList:
            if (entity in selectedList):
                self.entityVariable[entity].set(1)
            else:
                self.entityVariable[entity].set(0)

    def update(self, selectedList):
    
        print("\n[Activated]")
        print("before:",selectedList,":",len(selectedList))

        for entity in self.entityVariable:
            print("parsing: " + str(entity), "self.entityVariable[" + entity + "].get == " + str(self.entityVariable[entity].get()))
            if (self.entityVariable[entity].get() == 0) and (entity in selectedList):
                selectedList.remove(entity)
                print("popped:", entity)
            elif (self.entityVariable[entity].get() == 1) and (entity not in selectedList):
                selectedList += [entity]
                print("putted:", entity)
   
        print("after:",selectedList,":",len(selectedList))

        self.returnedList = selectedList #Basically, in the object which would contain the checkbuttons, then equate that list to the returned value.

    def pack(self, **options):

        sideOptions = options.get("anchor",tk.N)
        keyOption = options.get("key", False)
    
        if (keyOption == True):
            self.totalEntities['A'].pack(anchor = sideOptions)
            self.totalEntities['B'].pack(anchor = sideOptions)
            self.totalEntities['C'].pack(anchor = sideOptions)
            self.totalEntities['D'].pack(anchor = sideOptions)
            self.totalEntities['E'].pack(anchor = sideOptions)
            self.totalEntities['F'].pack(anchor = sideOptions)
            self.totalEntities['G'].pack(anchor = sideOptions)
        else:
            for i in self.totalEntities:
                self.totalEntities[i].pack(anchor = sideOptions)


root = tk.Tk()

root.title(title)
root.minsize(900,50)

whiteSpace1 = CleanUp(root)
whiteSpace2 = CleanUp(root)

text = Print(root)

bottomButtonSpot = tk.Frame(root)

fileReader = FileReader(filepath)

generateButton = GenerateButton(root,text)
findFileButton = FileReaderButton(root, fileReader)
optionsButton = OptionsButton(root,text)
creditsButton = CreditsButton(root)

whiteSpace1.pack()
text.pack()
generateButton.pack()
whiteSpace2.pack()

findFileButton.pack(side = tk.LEFT)
optionsButton.pack(side = tk.LEFT)
creditsButton.pack(side = tk.LEFT)

chordsAvaliable = fileReader.giveChords()
scalesAvaliable = fileReader.giveScales()

chordsSelected = chordsAvaliable
scalesSelected = scalesAvaliable

#print("chords", chordsAvaliable)
#print("scales", scalesAvaliable)

#text.newScale()

root.mainloop()
