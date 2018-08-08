i = raw_input("Enter item name: ") #item name
q = int(raw_input("Enter quantity of item: ")) #quantity
r = input("Enter rate per item: ") #rate per item
t = q*r #total amount
if(t<1000):
	discount = 2
elif(t>1000 and t<10000):
	discount = 5
elif(t>9999 and t<15001):
	discount = 9
else:
	discount = 10

dis = discount*t/100

print "Name of item is: ",i
print "Quantity of item is: ",q
print "Rate per item is: ",r
print "total amount is: ",t
print "Availed discount is:", dis


