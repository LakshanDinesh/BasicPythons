import re# import from Regular Expressions pakcage

txt = "My Name is Lakshan Dinesh Liyanarachchi"

x = re.search("^The.*Lakshan$", txt)
if x:
	print("Yes the word is found")
else: 
	print("No")	

########################################
x = re.findall("an", txt)
print(x)
#print(x.span())



###################
x = re.split("\s", txt)
print(x)

y = re.split("\s", txt, 2)
print(y)


##############################
x = re.sub("\s", "0", txt)
print(x)

y = re.split("\s", "0", 2)
print(y)
