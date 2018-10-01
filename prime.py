def primeyn(number):
#
# This function is intended to evaluate wheter  
# "number" is prime or not
#
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False

	return True



