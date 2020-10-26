##############################################################################
a="Hello World"

print(a[6]) # print second element of the word and array length is word length
# space also count as the element

print(a[2:7])   #get a range of word
print(a[-7:-2]) #get rreverse

print(len(a))   #get length of word

print(a.strip())    #return a

print(a.lower())       #get in lower case

print(a.upper())    #get in upper case

print(a.replace("H", "J"))  #replace charactor

print(a.split("l")) #split words


##############################################################################
b="lakshan dinesh liyanarachchi"
x="l" in b #can use "in" and not "in"
print(x)#boolen method


##############################################################################
p=1
q=2
r=3
x="one {}, tow {} and three {}"

print(x.format(p,q,r))# use format() method to add strings and numbers


##############################################################################
txt="My name is \"lakshan\""    # Use escape mark to insert double qoutes