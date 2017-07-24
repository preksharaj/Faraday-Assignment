import sys
from easygui import *
import json
from pprint import pprint

with open('ca.json') as data_file:
    data = json.load(data_file)

choices = []
dict = {}
#pprint(data)
#print data[0]["state_name"]
for i in data:
	choices.append(i["name"].encode('ascii','ignore'))
	dict[i["name"].encode('ascii','ignore')] = i
#print dict



	# make sure that none of the fields was left blank
while 1:
	msg ="Select your city?"
	title = "City Information"
	choice = choicebox(msg, title, choices)
	print choice
	msg = ""
	title = "City Information"
	fieldNames = ["City","County","Latitude","Longitude"]
	fieldValues = [choice,dict[choice]['full_county_name'],dict[choice]['primary_latitude'],dict[choice]['primary_longitude']]  # we start with blanks for the values
	multenterbox(msg,title, fieldNames,fieldValues)
	msg = "Do you want to continue?"
	title = "Please Confirm"
	if ccbox(msg, title):     # show a Continue/Cancel dialog
     		pass  # user chose Continue
 	else:
     		sys.exit(0)           # user chose Cancel
