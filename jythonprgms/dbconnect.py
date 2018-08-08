from com.ziclix.python.sql import zxJDBC

import os
import sys
from java.util import Properties
sys.path.append('/root/Desktop/mysql-connector-java-5.1.42.jar')

import com.mysql.jdbc.Driver as Driver

props = Properties()
props.put ('user','root')
props.put('password','')

mysqlconn = zxJDBC.connect(Driver().connect('jdbc:mysql://localhost/Appin',props))
mysqlconn = mysqlconn.cursor()
mysqlconn.execute('SELECT * FROM emp2')

for a in mysqlconn.fetchall():
	print a


