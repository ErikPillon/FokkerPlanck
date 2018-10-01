# Exercise 7

def primeyn(number):
#
# This function is intended to evaluate wheter  
# "number" is prime or not
#
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False

	return True

n = 0
i = 2
while n<=10000:
	if primeyn(i):
		n = n+1
	i=i+1

print(i)
print(n)






