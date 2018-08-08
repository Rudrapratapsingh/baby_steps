#run in python3.6

import random

pnamelist = ['rudra','utkarsh']
pclasslist = ['a','b']
preglist = ['0','1']
ploginnamelist = ['rudra','utkarsh']
ppasslist = ['rudra','utkarsh']
preportlist = ['']
scoredict = {''}


qlist = ['Which of these provides a Stream processing system used in Hadoop ecosystem?','The main role of the secondary namenode is to?','For a HDFS directory the replication factor(RF) is?','The hadfs command put is used to?','Sultan Azlan Shah Cup is related to which among the following Sports?','Sachin Tendulkar hit his 100th international century against which among the following team? ','THE WORLD BENEATH HIS FEET is a Biography of? ','Which among the following country is the host of 2018 Commonwealth Games? ','Tansen sangeet samaroh is organised at which place of Madhya Pradesh? ','Which place in Madhya Pradesh is known for Festival of Dances? ','Which of the following countries are separated by the Strait of Gibraltar? ','Which among the following is the driest desert in Earth? ','After Brazil, which among the following is the second largest country in South America? ','Which among the following is the most populous country of Africa?']

alist = ['Solr','Copy the filesystem metadata from primary namenode.','same as the RF of the files in that directory.','Copy files from local file system to HDFS.','Badminton','Sri Lanka ','Pulela Gopichand ','Canada ','Gwalior  ','Orchha  ','Portugal and Morocco ','Kalahari ','Columbia ','Nigeria ']

blist = ['Tez','Copy the filesystem metadata from NFS stored by primary namenode.','Zero','Copy files or directories from local file system to HDFS.','Hockey ','Bangladesh ','Nawab Pataudi ','England ','Bhopal ','Khajuraho  ','Algeria and Spain ','Atacama ','Argentina ','Egypt ']

clist = ['Spark','Monitor if the primary namenode is up and running.','3','Copy files from from HDFS to local filesystem.','Table Tennis ','Pakistan','Ajit Wadekar ','Australia ','Ujjain ','Bhopal ','Morroco and Spain ','Mojave Desert ','Peru ','Algeria ']

dlist = ['Hive','Periodically merge the namespace image with the edit log.','Does not apply.','Copy files or directories from HDFS to local filesystem.','Golf ','South Africa ','Sachin Tendulkar ','India ','Chhatarpur ','Chanderi ','Algeria and Portugal ','Tabernas Desert ','Chile ','Ghana ']

anslist = ['c','d','d','b','b','b','a','c','a','b','c','b','b','a']

print('='*45),
print('Quiz Login'),
print('='*50)

print ('Choose 1 for Admin')
print ('Choose 2 for Player')
print ('Choose 3 for Exit')

n1 = 'root'
username_admin = ['rudra','raj']
password_admin = ['rudra','raj']

opt=int(input("Enter any value:"))

if opt==1:
	print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++ Admin Window ++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
	count = 0
	while count<3:		
		print ("Admin login")
		for at in range(2,-1,-1):
			username_admin = input('Please Enter username for admin:')
			password_admin = input('Please Enter password for admin:')	
			for i in range(0, len(useradmin)):
				if  username_admin == useradmin[i]  and password_admin == passadmin[i] :

					print ('='*50),
					print ("Welcome root admin!"),
					print ('='*50)

					print ('Select 1 to add Player')
					print ('Select 2 to update Player')
					print ('Select 3 to delete player')
					print ('Select 4 to Update Admin profile')
					print ('Select 5 to Add Question')
					print ('Select 6 to Update Question')
					print ('Select 7 to Delete Question')
					print ('Select 8 to know Player Report')
					print ('Select 9 to search Player Report')
					print ('Select 10 to Log Out')
			
					select = int(input("Enter the value: "))

				if select == 1:
					pName = input("Name of the player: ")
					pClass = input ("Class of the player:")
					pReg = int(input("Regisration number of the player:"))
					pLogin = input("Login name:")
					pPass = input("password:")

					pnamelist.append(pName);
					pclasslist.append(pClass);
					preglist.append(pReg);
					ploginnamelist.append(pLogin);
					ppasslist.append(pPass);
					print('Player added successfully! ')

				elif select == 2:
					regno = int(input('Enter registration number/index to update player:')

					del pnamelist[regno]
					del pclasslist[regno]
					del preglist[regno]
					del ploginnamelist[regno]
					del ppasslist[regno]
				
					pName = input("Name of the player: ")
					pClass = input ("Class of the player:")
					pReg = input("Regisration number of the player:")
					pLogin = input("Login name:")
					pPass = input("password:")

					pnamelist.insert(regno, pName);
					pclassist.insert(regno, pClass);
					preglist.insert(regno, pReg);
					ploginnamelist.insert(regno, pLogin);
					ppasslist.insert(regno, pPass);
						 

				elif select == 3:
					regno = int(input('Enter registration number/index to delete player: '))
					del pnamelist[regno]				
					del pclasslist[regno]
					del preglist[regno]
					del ploginnamelist[regno]
					del ppasslist[regno]
					print ('Player Removed! ')

				
				elif select == 4:
					print ('='*50),
					print ('Update Admin profile'),
					print ('='*50)
				
					useradmin[i] =raw_input("Update Profile\n Enter new username :	")
					passadmin[i]=raw_input(" Enter new password :	")
					print("Update Successfull")

				elif select == 5: 
					print('Add Question')
					q = input('Enter new question: ')
					qlist.append(q);
					optA = input('Enter Option (a) ')
					alist.append(optA);
					optB = input('Enter Option (b) ')
					alist.append(optB);
					optC = input('Enter Option (c) ')
					alist.append(optC);
					optD = input('Enter Option (d) ')
					alist.append(optD);
					ans = input('Enter answer character:')
					anslist.append(ans);
					print (qlist) #print the new list?
 
				elif select == 6:
					up = int(input('Print Index of Question you want to update'))
					if up<len(qlist):
						del qlist[up]				
						del alist[up]
						del blist[up]
						del clist[up]
						del dlist[up]
						del anslist[up]
				
						upq = input('Question: ')
						upa = input('Option a: ')
						upb = input('Option b: ')
						upc = input('Option c: ')
						upd = input('Option d: ')
						upans = input('Answer Option: ')

						qlist.insert(up,upq);
						alist.insert(up,upa);
						blist.insert(up,upb);
						clist.insert(up,upc);
						dlist.insert(up,upd);
				
						print ('Updated Successfully!')
					else:
						print ('Value out of data!')

				elif select == 7:
					i1 = int(input('Index of Question number you want to remove: '))
					if i1<len(qlist):
						del qlist[i1]				
						del alist[i1]
						del blist[i1]
						del clist[i1]
						del dlist[i1]
						del anslist[i1]
					else:
						print ('Value out of data!')

				elif select == 8:
					pName = input('Enter player name to know report: ')
					k = scoredict.has_key(pName);

					if k == true:
						sc = scoredict.get(pName);
						print (sc)
					else:
						print('This player does not exist')

				elif select == 9:
					num = len(pnamelist);
					print ('Number of players are:',num)

				elif select == 10:
					print('Logout')
					exit()
			else :
				print ("Entry Mismatch! Forgot credentials? Try again")
			count += 1			#try again program
elif opt==2:	
	sum = 0
	print ("++++++++++++++++++++++++++++++++++++++++++++++++++++ Player Window +++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	pName = input("Name of the player: ")
	pClass = input ("Class of the player:")
	pReg = input("Regisration number of the player:")
	pLogin = input("Login name:")
	pPass = input("password:")

	pnamelist.append(pName);
	pclasslist.append(pClass);
	preglist.append(pReg);
	ploginnamelist.append(pLogin);
	ppasslist.append(pPass);

	print ('='*50),
	print ("Welcome",pName),
	print ('='*50)

	print ('....... Your quiz starts here ..........')
	for i in qlist:
		q1 = random.choice(qlist);
		ind = qlist.index(q1);
		print (qlist[ind])
		print (alist[ind])
		print (blist[ind])
		print (clist[ind])
		print (dlist[ind])
		answer = input('Enter your one choice out of a,b,c and d: ')
		if answer == anslist[ind]:
			print ('Correct answer!')
			sum = sum + 1
		else:
			print('Wrong Answer!')
	print('Total marks: ',sum)
	d['pName'] = 'sum'
	sc = scoredict.get(pName);
	print (sc)

		
elif opt==3:
	print ("Exiting...")
	exit()
else :
	print ("Invalid Entry, Try again")

