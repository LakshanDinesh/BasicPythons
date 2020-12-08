class People:
	def __init__(self, name, age, address):#self parameter use to accsess variables that related class
		self.name = name
		self.age = age
		self.address = address

p1 = People("Lakshan", 24, "Wandu")
print(p1.name)
print(p1.age)
print(p1.address)




###############################
#inheritance
class person:#parent class
	def __init__(self, fname, lname, age):
		self.firstname=fname
		self.lastname=lname
		self.age = age

	def printname(self):
		print(self.firstname, self.lastname, self.age)

x = person("Lakshan", "Dinesh", 10)
x.printname()


class student(person):#child class
	#pass use to pass without adding any methods

	def __init__(self, fname, lname, age, town):
		super().__init__(fname, lname, age)
		self.town= town

	def printname(self):
		print(self.firstname, self.lastname, self.age, self.town)


		

y = student("Thanuri", "Navindi", 24, "Galle")
y.printname()