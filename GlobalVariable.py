x="lakshan"

def myfunc():
    x="tipa"# can use local and global varibles as a same name
    print("my name is "+x)
    global y#global key word is use to make global variables
    y = 1
    
myfunc()
print("my name is "+x)
print(y)
print(type(y))#print the type of variable

print(float(y))#make constructive variables


