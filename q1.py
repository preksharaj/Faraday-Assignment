import json
list = {}

class itemlist(object):

	def __init__(self,ilist):
		global list
		list = ilist
		if isinstance(ilist, dict):
			self.ilist = ilist
		else:	
			#list = {x:str(ilist.count(x)) for x in ilist}	
			#self.ilist = list
			self.dictify(ilist)
			
			#print "Please populate class with valid dictionary of items and their frequency"
		self.display()

	def dictify(self,mlist):
		nlist = {x:str(mlist.count(x)) for x in mlist}
		self.ilist = nlist

####DISPLAY UNIQUE ITEMS IN LIST ########
        def display_items(self):
		print "UNIQUE ITEMS IN LIST:"
		for k,v in self.ilist.items():
			print k

####DISPLAY UNIQUE ITEMS AND THEIR FREQUENCY IN LIST ########
	def display(self):
		print "ITEM   FREQUENCY"
		for k,v in self.ilist.items():
			print k+"  "+v

###DISPLAY A PARTICULAR AND ITS FREQUENCY######
 	def get_item(self,item):
		if item in self.ilist:
			print "Item "+item+" Found in list has frequency "+self.ilist[item] 
		else:
			print "Item not present in List"

###UPDATE THE LIST WITH NEW ITEMS######
	def update(self,item):
		global list
		list.append(item)
		self.dictify(list)

      
if __name__ == "__main__":

	#newpack = {"apple":"10","orange":"20","grape":"3"}
	newpack = ["apple","apple","orange","apple","grape","apple","grape","orange"]
	#dict = json.loads(newpack)
	newlist = itemlist(newpack)
	#newlist.display()

	newlist.get_item("orange")
	newlist.update("peer")
    	newlist.display_items()
    	newlist.display()
	newlist.update("peer")
    	newlist.display()
	
