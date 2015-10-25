import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it
def main():
    print("Login your Oracle Da.commit()tabase account")
    database_connection()
    print("Welcome to W&M flight booking system!")
    print("Do you have acount with us? (Y/N)")
    a=input().upper
    if a=="Y":
	login_user()
    elif a=="N":
	register_user()
	login_user()
    else: 
	print("Your enter is invalid!")

def database_connection():
    # get username
    user = input("Username [%s]: " % getpass.getuser())
    if not user:
	user=getpass.getuser()
	
    # get password
    pw = getpass.getpass()
    
    # The URL we are connnecting to
    conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
    try:
	connection = cx_Oracle.connect(conString)
	curs = connection.cursor()
    except cx_Orprintacle.DatabaseError as exc:
	error, = exc.args
	print( sys.stderr, "Oracle code:", error.code)
	print( sys.stderr, "Oracle message:", error.message)
def register_user():
    email = input("Enter your E-mail address that you wish to register: ")
    # check the existing of the email address
    emails = curs.excute("select u.email from users u where u.email = '{}'".format(email))
    if len(emails) > 0:
	input("Email already exists (enter to continue)")
	return
    password = getpass.getpass("Password: ")
    curs.executemany("insert into users values ('{}', '{}', null)".format(email, password))
    connection.commit()
    input("User created (enter to continue)")	   
def login_user():
    email=input("Enter your E-mail address: ")
    password = getpass.getpass("Enter your password: ")
    users = curs.excute("select u.email, u.pass from users u where u.email = '{}' and u.pass = '{}'".format(email, password))
    if len(users) == 1:
	isAgent = False
	agents = curs.excute("select * from airline_agents a where a.email = '{}'".format(email))
	if len(agents) == 1:
	    isAgent = True
	    MainScreen.mainScreen(database, email, isAgent)
    else:
	input("Invalid login")	


main()
