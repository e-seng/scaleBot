import Tkinter as tk

keysAvailable = range(7)
keysSelected = []

sharpFlatAvailable = range(3)
sharpFlatSelected = []

scalesAvailable = range(42)
scalesSelected = []

chordsAvailable = range(49)
chordsSelected = []

class OptionsMenu:

    """
    This class open up the window for a user to the options menu

    Here, they can enable or disable specific technique they would or would not want to practice.
    """

    def __init__(self,master):
        
        self.keyOptions = KeyOptions(master)
        self.scaleOptions = ScaleOptions(master, scalesAvailable, scalesSelected, "Scales:")
        self.chordOptions = ChordOptions(master, chordsAvailable, chordsSelected, "Chords")
        
        print(scalesSelected, scalesAvailable)

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

        self.spot = tk.Frame(master)
        self.title = tk.Label(self.spot, text = title)

        self.returnedList = []
        self.availableList = availableList
        
        self.location = tk.Frame(self.spot, bd = 2,relief = tk.RIDGE)
        self.scroll = tk.Scrollbar(self.location)
        self.box = tk.Listbox(self.location,selectmode = "multiple",bd = 0, exportselection = False, height = 10)

        for i in availableList:
            if (i in selectedList):
                self.box.activate(availableList.index(i))

        self.box.bind("<<ListboxSelect>>", (lambda(event): self.update()))

        for entity in availableList:
            if (entity == ""):
                entity = "natural"
            self.box.insert(tk.END, str(entity))
            
    def update(self):
       
        self.returnedList = []

        for i in self.availableList:
            self.returnedList += [i]

        print("\n[ACTIVATED]")
        print("IN : " + str(self.__class__.__name__))
        print("availableList:", self.availableList,len(self.availableList))
        print("before:",self.returnedList,len(self.returnedList))

        for i in self.availableList:
            print("<PARSING : " + str(i) + ">")
            if (self.availableList.index(i) in self.box.curselection()):
                self.returnedList.remove(i)

        self.refresh()
#        if (isinstance(self, 

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

        self.location = tk.Frame(self.spot, bd = 0, relief = tk.RIDGE)
        self.boxKeys = tk.Listbox(self.location, selectmode = "multiple", bd = 0.5, height = len(keysAvailable), exportselection = False)
        #self.boxKeys.config()

        self.boxSharpFlat = tk.Listbox(self.location, selectmode = "multiple", bd = 0.5, height = len(sharpFlatAvailable), exportselection = False)

        for i in keysAvailable:
            if (i in keysSelected):
                self.boxKeys.activate(keysAvailable.index(i))

        self.boxKeys.bind("<<ListboxSelect>>", (lambda(event): self.update()))
        self.boxSharpFlat.bind("<<ListboxSelect>>", (lambda(event): self.update()))

        for entity in keysAvailable:
            self.boxKeys.insert(tk.END, str(entity))

        for entity in sharpFlatAvailable:
            if (entity == ""):
                entity = "natural"
            self.boxSharpFlat.insert(tk.END, str(entity))

    def update(self):

        self.returnedKeyList = []
        self.returnedSharpFlatList = []

        for i in keysAvailable:
            self.returnedKeyList += [i]

        for i in sharpFlatAvailable:
            self.returnedSharpFlatList += [i]

        print("\n[ACTIVATED]")
#        print("IN : " + str(self.__class__.__name__))
#        print("availableList:", self.availableList,len(self.availableList))
        print("before:")
        print(self.returnedKeyList,len(self.returnedKeyList))
        print(self.returnedSharpFlatList,len(self.returnedSharpFlatList))

        for i in keysAvailable:
            print("<PARSING : " + str(i) + ">")
            if (keysAvailable.index(i) in self.boxKeys.curselection()):
                self.returnedKeyList.remove(i)

        for i in sharpFlatAvailable:
            print("<PARSING : " + str(i) + ">")
            if (i == "natural") and (sharpFlatAvailable.index(i) in self.boxSharpFlat.curselection()):
                self.returnedSharpFlatList.remove("")
            elif (sharpFlatAvailable.index(i) in self.boxSharpFlat.curselection()):
                self.returnedSharpFlatList.remove(i)
        
        print("after:", self.returnedKeyList,":",len(self.returnedKeyList))

        self.refresh()
        
    def refresh(self):
        
        keysSelected = []
        sharpFlatSelected = []

        for i in self.returnedKeyList:
            keysSelected += [i]
        for i in self.returnedSharpFlatList:
            sharpFlatSelected += [i]

        print("Keys:", keysSelected, len(keysSelected), len(keysAvailable))
        print("Sharps and Flats:", sharpFlatSelected,len(sharpFlatSelected))

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

        scalesSelected = []

        for i in self.returnedList:
            scalesSelected += [i]

        print("after:", self.returnedList,":",len(self.returnedList))
        print("Scales:", scalesSelected, len(scalesSelected), len(scalesAvailable))

class ChordOptions(EntityChecker):
    """
    User is able to choose which chords, if any, they would like to play
    """

    def refresh(self):

        chordsSelected = []

        for i in self.returnedList:
            chordsSelected += [i]

#    def pack(self, **options):
#        
#        keyOption = options.get("key", False)
#        sideOption = options.get("side", tk.TOP)
#        anchorOption = options.get("anchor", tk.N)
#       
#        self.location.pack(side = sideOption, anchor = anchorOption)
#        
#        if (keyOption == False):
#            self.scroll.pack(side = tk.RIGHT, fill = tk.Y)
#            self.box.config(yscrollcommand = self.scroll.set)
#            self.scroll.config(command = self.box.yview)
#        
#        self.box.pack()

root = tk.Tk()

optionsMenu = OptionsMenu(root)
optionsMenu.pack()

tk.mainloop()
