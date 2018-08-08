n1 = input("First Number: ")
n2 = input("Second Number : ")
n3 = input("Third Number : ")
import math
if( n1<10 and n2<10 and n3<10): 
	if (n1<n2 and n1<n3):
		print "Square root of the smallest number is: ", math.sqrt(n1)
	elif(n2<n1 and n2<n3):
		print "Square root of the smallest number is: ",math.sqrt(n2)
	else:
		print "Square root of the smallest number is: ",math.sqrt(n3)
	
else: 
	print "One of the number is of two digits"
