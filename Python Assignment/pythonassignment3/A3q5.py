string = raw_input("Enter any string: ")
list = []
for i in string:
	if(i.islower()):
		a = i.upper();
		list.append(a);
	elif(i.isupper()):
		b = i.lower();
		list.append(b);
	elif(i == ' '):
		c = ' '
		list.append(c);
s = ''.join(list);
print s
