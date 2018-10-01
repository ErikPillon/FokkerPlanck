def primeyn(number):
#
# This function is intended to evaluate wheter  
# "number" is prime or not
#
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False

	return True

sum = 0
i = 2
for i in range(2,2000000):
	if primeyn(i):
		sum = sum+i
print(sum)
		
