import pyhk, pyperclip

"""

Script set to run on startup. Runs particular commands based on shortcuts set here.


"""

class Format(object):
	""" Format script """
	
	def __init__(self):
		self.text = ""
		self.text_clean = ""
		self.newtext = []
		self.formatted = ""
	
	def clear(self):
		self.text = ""
		self.text_clean = ""
		self.newtext = []
		self.formatted = ""
	
	def fromclipboard(self):
		self.clear()
		self.text = pyperclip.paste()
		self.text_clean = self.text.split("\n")
		self.newtext = []
		
		for i in self.text_clean:
			self.newtext.append(i.title())
	
	def toclipboard(self):
		pyperclip.copy(self.formatted)

	def address(self):
		self.fromclipboard()
		
		for index, item in enumerate(self.newtext):
			if index != len(self.newtext)-1:
				newline = item + "\n"
				self.formatted += newline
			else:
				self.formatted += item.upper()
		
		self.toclipboard()

	def name(self):
		self.fromclipboard()
		
		for index, item in enumerate(self.newtext):
			if index != len(self.newtext)-1:
				self.formatted = self.formatted + item + " "
			else:
				self.formatted += item
		
		self.toclipboard()

	def copy(self):
		self.fromclipboard()
		
		for index, item in enumerate(self.newtext):
			if index != len(self.newtext)-1:
				self.formatted = self.formatted + item.lower() + " "
			else:
				self.formatted += item.lower()
		
		self.toclipboard()


format = Format()
hot = pyhk.pyhk()

hot.addHotkey(['Lcontrol' , 'Lwin' , 'F1'], format.name)
hot.addHotkey(['Lcontrol' , 'Lwin' , 'F2'], format.address)
hot.addHotkey(['Lcontrol' , 'Lwin' , 'F3'], format.copy)

if __name__ == "__main__":
	hot.start()