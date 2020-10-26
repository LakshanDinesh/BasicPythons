print(10>9) # print true when true and print false when false statements


########################################################################
print(bool("Hello"))    # bool() function help to identify the values
print(bool())


########################################################################
class myclass():
    def __len__(self):
        return 0

myjob=myclass()
print(bool(myjob))
#can use class and function to return booleans


########################################################################
x=2
print(isinstance(x, int)) # weather check x is integer
#isinstance() function use to check

