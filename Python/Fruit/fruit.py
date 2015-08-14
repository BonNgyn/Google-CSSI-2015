class Fruit:
	name = ''
	poisonous = False

	def __init__(self, nameOfFruit, willDie):
		self.name = nameOfFruit
		self.poisonous = willDie

	def describe(self):
		if self.poisonous == False:
			print "It's okay to eat the " + self.name
		else:
			print "It's not okay to eat the " + self.name


f1 = Fruit('Apple', True)
f2 = Fruit('Banana', False)

f1.describe()
f2.describe()