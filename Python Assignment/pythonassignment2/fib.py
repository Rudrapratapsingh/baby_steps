
n = int(raw_input("Enter number till pattern is to be printed: "))

t1 = 1
t2 = 0
t = 0

for i in range(1,n):
	t = t1 + t2
	print t1 ,
	t2 = t1
	t1 = t

