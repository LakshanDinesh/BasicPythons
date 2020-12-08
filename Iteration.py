x = ["A", "B", "C"]
#x = "Lakshan"
y = iter(x)# Assign iterable values

print(next(y))#next() use to get assigned value
print(next(y))
print(next(y))


class myno:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x

		else:
			raise StopIteration

final = myno()
finaliter = iter(final)

for x in finaliter:
	print(x)