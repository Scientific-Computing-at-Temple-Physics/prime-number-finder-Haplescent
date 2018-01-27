# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)

# These functions will ask you for your number ranges, and assign them to 'x1' and 'x2'
x1 = int(raw_input('smallest number to check: '))
x2 = int(raw_input('largest number to check: '))

# This line will print your two numbers out
print "This function uses a while-loop, so if you are using large"
print "numbers, use CTRL-C to quit the function if you wish to"
print "do so"


""" Text enclosed in triple quotes is also a comment.
This code should find and output all prime numbers between (and including) the numbers entered initially.
If no prime numbers are found in that range, it should print a statement to the user.
Now we end the comment with triple quotes."""

# The rest is up to you!

#defining the lists
start = range(x1,x2+1)
primes = []
not_primes = []
not_relevent = []



"""
This loop function goes through each number between the largest
and smallest number inputted by user.  Each number (x) is divided by
every number between x and 1 until a remainer is found.  If no
remainer is found, the number is considered to be prime.  Negative
numbers are not considered prime"
""" 

for x in start:
	if abs(x) != x:
		not_relevent.append(x)
	elif x == 0:
		not_relevent.append(x)
	elif x == 1:
		not_primes.append(x)
	else: 
		n = x - 1
		while n != 0:
			if n == 1:
				primes.append(x)
				n = 0
			elif x % n == 0:
				n = 0
				not_primes.append(x)
			elif x % n >= 0:
				n = n - 1

print "Here is a list of all of the primes"
print primes

		
		

