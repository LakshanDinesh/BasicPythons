set1 = {"apple", "banana", "cherry"}
print(set1)

set2 = {"a", "b", "c"}

set1.update(set2)
print(set1)
#use update() and add() to add elements

##############
#join sets
set1.intersection(set2)
print(set1)

x = set1.symmetric_difference(set2)
print(x)