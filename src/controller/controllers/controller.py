#pip install mysql-connector
import mysql.connector as sql

##########################
#       Db Info          #
##########################
#Host: 127.0.0.1
#Port: 3306 
#User: root
#Pass: 
db = sql.connect(host='127.0.0.1',
                user='root',
                password='pass',
                database='testDb')

myCursor = db.cursor()



##########################
#    Table creation      #
##########################

#Only needs to be ran once for creation of the DB
# myCursor.execute('CREATE DATABASE testDb')
# myCursor.execute("CREATE TABLE User (PID int PRIMARY KEY AUTO_INCREMENT, user_name varchar(50), password varchar(50))")

############################        Example model
# PID |  USER  |  PASS     #        PID must be a unqiue value in the table
# -------------------------#        
# 0  |  test1  |  pass     #        All attributes within the table are non-nullable
# 1  |  test2  |  pass     #
############################



##########################
#    Logic Handeling     #
##########################

# myCursor.execute("SET PASSWORD FOR 'root'@'localhost' = 'pass'")
# mycursor.execute("insert into User (PID, user_name, password) values (1, 'riley', 'pass')")
# myCursor.execute("select * from User where PID = '1'")
print(myCursor.execute('DESCRIBE user'))

