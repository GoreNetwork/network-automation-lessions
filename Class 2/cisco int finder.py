#Import the library
from ciscoconfparse import CiscoConfParse

#set a varable to the file name, 
#you might want to change it later
#this way you only have to change it in 1 place
filename = "running_config.txt"

#Make a function, in this example we are handing it the running config and 
#the string "nterface"
def find_child_text (file, text):
	#"all" will end up holding all the info we are looking for being returned
	all = []
	#Give the file to CiscoConfParse to look at
	parse = CiscoConfParse(file)
	#Here we are finding all the lines with "nterface" in them
	for obj in parse.find_objects(text):
		#Make a list that will contain the parent and the children
		each_obj = []
		#Add the parent to the list as a string
		each_obj.append(obj.text)
		#For all the parent's children
		for each in obj.all_children:
			#Add the child to the list as a string
			each_obj.append(each.text)
		#Add the device/config to a list of devices and configs
		all.append(each_obj)
	#Once all the interfaces have gone through this the 
	#function hands the list of all interfaces to the main program
	#At this point all is a list of lists, each sub list is the interface
	#And all the config for each interface
	return all

interfaces = (find_child_text (filename, "nterface" ))

lines_I_care_about=["shutdown"]

#Look at each interface
for interface_config in interfaces:
	#Look at each line of the config
	for interface_line in interface_config:
		if "shut" in interface_line:
			print (interface_config[0])