user_number = int(input("Choose a number and I'll return the prime numbers: \n"))
list = []
for i in range(1,user_number+1):
	if user_number%i==0:
		list.append(i)
if list[1]==user_number:
	print user_number, "is a prime number"
else:
	print user_number,"'s prime factorials are:"
	for i in list:
		print i,