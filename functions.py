def name(*n):
    print("My Name is " + n[1])

name("Lakshan", "Dinesh", "Kumara", "Liayanarachchi")


#################33333333return values
def area(a, b):
    return a*b

print(area(3, 5))


##################################Recurrtions
"""def rec(k):
    if (k > 0):
        result = k * rec(k - 1)
        print(result)
rec(5)"""

"""def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)"""


###############################
x = lambda a : a + 10# adiing constant to the method
print(x(10))

def lambdafuction(b):
  return lambda a : a * b


y = lambdafuction(3)
print(y(5))

