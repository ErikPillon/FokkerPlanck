# Exercise 3

def primeyn(number):
#
# This function is intended to evaluate wheter  
# "number" is prime or not
#
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False

	return True
sol = 0
j = 600851475143
for i in range(int(j**0.5)+1,10,-1):
	if primeyn(i):
		if j%i==0:
			sol = i
			break
		
print(sol)
