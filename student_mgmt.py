import os
import mysql.connector as mariadb
db = mariadb.connect(host='localhost', database='student_mgmt', user='root',password='')
cursor = db.cursor()
os.system("clear");
def addfns(sname,sbranch,syear,phy,math,bio,eng): #add
	sql = "INSERT INTO student(sname,sbranch,syear,phy,math,bio,eng) VALUES ('%s','%s',%d,%d,%d,%d,%d)"%(sname,sbranch,syear,phy,math,bio,eng)
	cursor.execute(sql)
	print "added!"
	db.commit()
	sql1 = "select * from student"
	cursor.execute(sql1)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)	
	db.commit()
	db.close()
def editfns(sid): #edit
	field_old = int(raw_input("Enter the field you want to edit from name(1), branch(2), year(3), phy(4), math(5), bio(6), eng(7):\n"))
	field_new = raw_input("Enter the value you want to add into field")
	if field_old == 1:
		sql = "UPDATE student SET sname = '%s' WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)		
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)	
		db.commit()
		db.close()				
	elif field_old == 2:
		sql = "UPDATE student SET sbranch = '%s' WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)	
		db.commit()
		db.close()		
	elif field_old == 3:
		int(field_new)
		sql = "UPDATE student SET syear = %d WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)	
		db.commit()
		db.close()		
	elif field_old == 4:
		int(field_new)
		sql = "UPDATE student SET phy = '%s' WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)	
		db.commit()
		db.close()		
	elif field_old == 5:
		int(field_new)		
		sql = "UPDATE student SET math = '%s' WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)	
		db.commit()
		db.close()		
	elif field_old == 6:
		int(field_new)
		sql = "UPDATE student SET bio = '%s' WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)		
		db.commit()
		db.close()		
	elif field_old == 7:
		int(field_new)
		sql = "UPDATE student SET eng = '%s' WHERE sid =%d"%(field_new,sid)
		cursor.execute(sql)
		print "updated!"
		sql1 = "select * from student"
		cursor.execute(sql1)
		results = cursor.fetchall()
		widths = []
		columns = []
		tavnit = '|'
		separator = '+' 
		for cd in cursor.description:
		    widths.append(max(cd[2], len(cd[0])))
		    columns.append(cd[0])
		for w in widths:
		    tavnit += " %-"+"%ss |" % (w,)
		    separator += '-'*w + '--+'
		print(separator)
		print(tavnit % tuple(columns))
		print(separator)
		for row in results:
		    print(tavnit % row)
		print(separator)		
		db.commit()
		db.close()		
	else:
		print "Wrong entry!"
def removefns(sid): #remove
	sql = "delete from student where sid = %d"%(sid)
	cursor.execute(sql)
	print "removed!"
	sql1 = "select * from student"
	cursor.execute(sql1)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)	
	db.commit()
	db.close()
def updatefns(sid,sname,sbranch,syear,phy,math,bio,eng): #update
	sql = "UPDATE student SET sname = '%s', sbranch = '%s', syear = %d, phy = %d, math = %d, bio = %d, eng = %d WHERE sid = %d"%(sname,sbranch,syear,phy,math,bio,eng,sid)
	cursor.execute(sql)
	sql1 = "select * from student"
	cursor.execute(sql1)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)	
	db.commit()
	db.close()
def searchfns(sname): #search
	sql = "SELECT * from student WHERE sname='%s'"%sname
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)			
	db.commit()
	db.close()
def addmarksfns(sid):  #addmarks
	sql = "SELECT phy,math,bio,eng FROM student WHERE sid=%d"%(sid)
	cursor.execute(sql)
	results = cursor.fetchall()
	for a in results:
		phy0=a[0]
		math0=a[1]
		bio0=a[2]
		eng0=a[3]
		sum = phy0 + math0 + bio0 + eng0
		print "Sum of marks: ",sum,"/400"
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)	
	db.commit()
	db.close()
def aggrfns(sid): # aggr
	sql =  "SELECT phy,math,bio,eng FROM student WHERE sid=%d"%(sid)
	cursor.execute(sql)
	results = cursor.fetchall()
	for a in results:
		phy0=a[0]
		math0=a[1]
		bio0=a[2]
		eng0=a[3]
		s = phy0 + math0 + bio0 + eng0
		aggregate = s/4
		print "Aggreagte: ",aggregate
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)
	db.commit()
	db.close()
def vbranchfns(sbranch): # vbranch
	sql = "SELECT * FROM student WHERE sbranch = '%s'"%sbranch
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)			
	db.commit()
	db.close()
def physics(phy):
	sql = "SELECT * from student where phy = %d"%phy
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)	
def maths(math):
	sql = "SELECT * from student where math = %d"%math
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)
def biology(bio):
	sql = "SELECT * from student where bio = %d"%bio
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)
def english(eng):
	sql = "SELECT * from student where english = %d"%eng
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)
def vyearfns(syear): #vbyyear
	sql = "SELECT * FROM student where syear = %d"%syear
	cursor.execute(sql)
	results = cursor.fetchall()
	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 
	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])
	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'
	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)
	db.commit()
	db.close()
print '#'*75,
print "STUDENT MANAGEMENT SYSTEM",
print '#'*75
n = int(raw_input( 'Enter number corresponding to the operation:\n 1. Add new Student \n2. edit student data  \n3. Remove student  \n4. update student  \n5. Search student  \n6. Add marks \n7. Calculate Aggregate \n8. View By Branch \n9. View By Marks  \n10. View By year\n'))
if n==1:#done
	sname = raw_input("What is student's name? ")
	phy = int(raw_input("Enter marks in physics: "))
	math = int(raw_input("Enter marks in maths: "))
	bio = int(raw_input("Enter marks in biology: "))
	eng = int(raw_input("Enter marks in english: "))
	sbranch = raw_input("Enter student's Branch: ")
	syear = int(raw_input("Enter student's year: "))
	addfns(sname,sbranch,syear,phy,math,bio,eng)
elif n==2:#done
	sid = int(raw_input("Enter the student's id to edit student's data"))
	editfns(sid)
elif n==3: #done
	sid = int(raw_input("Enter student's id to remove the corresponding data"))
	removefns(sid)
	print "Removed!"
elif n==4:#done
	sid = int(raw_input("Enter the student's id to Update student's data"))
	sname = raw_input("Enter New student's name:")
	phy = int(raw_input("Enter marks in physics: "))
	math = int(raw_input("Enter marks in maths: "))
	bio = int(raw_input("Enter marks in biology: "))
	eng = int(raw_input("Enter marks in english: "))
	sbranch = raw_input("Enter student's Branch: ")
	syear = int(raw_input("Enter student's year: "))
	updatefns(sid,sname,sbranch,syear,phy,math,bio,eng)
elif n==5:#done
	sname = raw_input("What is student's name you are searching for? ")
	searchfns(sname)
	#call search student fns by name
elif n==6: #done
	sid = int(raw_input("Enter the id of student to add marks"))
	addmarksfns(sid)
	#add marks fns call
elif n==7:#done
	print "Calculate Total aggregate"
	sid = int(raw_input("Enter the student's id to Calculate student's Aggregate"))
	aggrfns(sid)
	#calculate aggregate fns
elif n==8:#done
	print "View by branch"
	sbranch = raw_input("Enter the student(s)' branch")
	vbranchfns(sbranch)
elif n==9:   #done
	print "View by marks"
	name = raw_input("Enter subject from phy, math, bio, eng to view by marks")
	if name == 'phy':
		phy = int(raw_input("Enter marks in physics: \n"))
		physics(phy)
	elif name == 'math':
		math = int(raw_input("Enter marks in maths: \n"))
		maths(math)
	elif name == 'bio':
		bio = int(raw_input("Enter marks in biology: \n"))
		biology(bio)
	elif name == 'eng':
		eng = int(raw_input("Enter marks in english: \n"))
		english(eng)
	else:
		print "Wrong entry!"
	
elif n==10: #done
	print "View by year"
	syear = int(raw_input("Enter the student(s)' year to view data"))
	vyearfns(syear)
else:
	print 'Invalid Entry!'
