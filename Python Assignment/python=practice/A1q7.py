h = input("Enter height of the person in centimeter: ")
w1 = 18.5*h**2
w3 = w1/10000
w2 = 24.9*h**2
w4 = w2/10000

if (h>161 and h<189):
	print "Ideal weight for the person is in range(Kg): ",(w3,w4)

else: 
	print "Height entered is out of range" 


