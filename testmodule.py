import mymodule as m# import key word is use to access to created module

m.welcome("Lakshan")



import platform#built-in module

x = platform.system()
print(x)

y =dir(platform)#list all the functions or variables in the module
print(y)


import datetime#get date and time in the python
z = datetime.datetime.now()
print(z)
print(z.strftime("%B"))