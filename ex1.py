# exercise 1

multiples = [0]

for i in range(1,1000):
	if (i%3==0):
		multiples.append(i)
	elif (i%5==0):
		multiples.append(i)

print(sum(multiples))
