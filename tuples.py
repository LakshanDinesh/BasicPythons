######################
#tupels are unchangebale
x=("a", "b", "c", "d")

y=list(x)#need convert tuple in to a list to change
y[1]="e"
x=tuple(y)
print(x)


######################
(f, *g, h) = x#unpacking tuples
print(f)
print(g)
print(h)

######################
#tuples can multify
######################
######################