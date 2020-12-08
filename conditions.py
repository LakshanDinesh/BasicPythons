#if-else
m=70
if m>75:
    print("A")
elif m>65:
    print("B")


#########################
i=0
while i<6:
    i+=1
    if i==3:# 3 is missing there, with continue key word can stop the itteration.
        continue
    print(i)


###########################
#For loop

name=["Lakshan", "Dinesh", "kumara", "Liyanaachchi"]

for x in name:
    if x == "Dinesh":
        break
    print(x)


####################################
for x in range(2, 30, 3):# 3 is the increment vallue

    print(x)


############################
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


###################
