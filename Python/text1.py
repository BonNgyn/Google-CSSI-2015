#This is a comment 

# if 6 < 7:
# 	print "hello"
# 	print "goodbye"
# if 7 < 8:
# 	if 8 < 9:
# 		print "everything"

# a = True
# b = True

# if a and b:
# 	print '1'
# elif a or b:
# 	print '2'
# else:
# 	print '3'

# def sales_tax(subtotal, tax_rate):
# 	return subtotal*tax_rate

# print sales_tax(100, 0.10)


# def fizzBuzz(num):
# 	a = num%3
# 	b = num%5

# 	if(a == 0 and b == 0):
# 		return "FizzBuzz"
# 	elif(a == 0):
# 		return "Fizz"
# 	elif(b == 0):
# 		return "Buzz"

# print fizzBuzz(35039) 

# def fizzBuzz(num):	
# 	a = num%3
# 	b = num%5
# 	c = num%15

# 	if(c==0):
# 		if(a==0):
# 			return "Fizz"
# 		if(b==0):	
# 			return "Buzz"

# print fizzBuzz(30)

# def FizzBuzz(num):
# 	if num%15 == 0:
# 		return "FizzBuzz"
# 	elif num%5 == 0:
# 		return "Buzz"
# 	elif num%3 == 0:
# 		return "Fizz"
# 	else:
# 		return ""

# print FizzBuzz(33)



# def FizzBuzz2(num):
# 	s = ""
# 	if num%3 == 0:
# 		s = s + "Fizz"
# 	if num%5 == 0:
# 		s = s + "Buzz"
# 	return s

# print FizzBuzz2(45)

# for i in ['a', 'b', 'c']:
# 	print i


# i = 0
# while i < 10:
# 	print i
# 	i += 1 


# myList = [1, True, 'hello']

# for x in myList: 
# 	print x

# print 'done'

#-----------------------------------------------------------

import random

# count = 0
# roll1 = 0
# roll2 = 0
# total = 0
# prop = 0
# rang = 100

# for x in range(rang):

# 	while not(roll2 == 6 and roll1 ==6):
# 		count += 1
# 		roll1 = random.randint(1,6)
# 		roll2 = random.randint(1,6)

# 		print 'Rolled: ', roll1, roll2

# 		if(roll1 == 6 and roll2 == 6):
# 			print 'Got double sixes!'	
# 		elif(roll1 == 1 and roll2 == 1):
# 			print 'Got snake eyes!'

# 	roll1 = 0
# 	roll2 = 0
# 	total += count
# 	print "Rolled the dice " + str(count) + " times"
# 	count = 0


# prop = total/rang
# print prop


# times = 0
# done = False

# while not done:
# 	times += 1
# 	roll1 = random.randint(1,6)
# 	roll2 = random.randint(1,6)
# 	print 'I rolled', roll1, 'and', roll2
# 	if roll1 == 1 and roll2 ==1:
# 		print 'both ones!'
# 	if roll1 == 6 and roll2 ==6:
# 		print 'both sixes!'
# 		done = True
# print 'Rolled the dice', times, 'times'




# [] this is a list and {} is a dictionary 
#there is no order in the dictionary

# d = {'98052':'Redmond', '98007':'Bellevue'}

# for i in d:
# 	print i, 'is mapped to', d[i]

#raw_input() ~ evaluates to the stirng 
#'from' in d ~ ask if a key is in the dictionary 
#d['from'] = 'to to' ~ to change it

#Last lab of the day 4, using raw_input and dictionary 
# Write a program that asks the user for a word. 
# Say whether the word has been seen before. 
# If so, say how many times it's been seen.
# Then keep asking.

# Maybe let users exit?

# done = False
# count = 0
# word = raw_input('Please enter a word: ')

# while not done:
# 	my_dictionary = {}

# 	if word not in my_dictionary:
# 		print 'Sorry, we can not find this word.'
# 		word = raw_input('Please enter another word: ')
# 		my_dictionary[word] = 0
# 	if word in my_dictionary:
# 		count = my_dictionary[word]
#		my_dictionary[word] = (count+1)
# 	if word == 'exit':
# 		done = True

# print my_dictionary



# done = False 
# words = {}

# while not done:
# 	word =raw_input('Please enter a word:')
# 	if word == '':
# 		break
# 	if word in words:
# 		words[word] += 1
# 		print 'Seen that', words[word], 'times'
# 	else:
# 		words[word] = 1
# 		print "That's a new one"

###################################################################### Day 2 of Python ######################################################################

########## Morning review: Party ###################

# def get_guest(): 
# 	guests = []

# 	while True:
# 		name = raw_input("Who's coming? ")
# 		if name == '':
# 			break
# 		guests.append(name)
# 	return guests

# def say(what, guests):
# 	for x in guests:
# 		# print 'hi, {0}'.format(x)
# 		print  what, ',', x

# def inflate_balloons():
# 	print 'The ballons are inflated.'

# def start_music():
# 	print '*I want it that way* is playing.'

# def cheer(num):
# 	for x in range(num):
# 		print 'Woop de doo!'

# def party():
# 	guests = get_guest()
# 	say('Hello', guests)
# 	inflate_balloons()
# 	start_music()
# 	cheer(8)
# 	say('Good-bye',guests)


# party()

################# ##########################






















































































































