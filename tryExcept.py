"""try:
	print(x)

except:
	print("The exception is occurs")
else:
	pass
finally:
	print("error checking is finished")"""

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 



################################
y = 1

if not type(y) is float:
	raise TypeError("please enter the word")