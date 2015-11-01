import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it
import interface

def main():
    print("Login your Oracle Database account")
    database_connection()
    print("Welcome to W&M flight booking system!")
    user_input = ""
    while True:
        print("Do you have acount with us? (Y/N)")
        a=input()
        if a.upper()=="Y":
            user_input = login_user()
            if user_input == "q":
                break
        elif a.upper()=="N":
            register_user()
            user_input = login_user()
           
        else: 
	        print("Your enter is invalid! press enter and try again")

def database_connection():   # connecting to the database
    # get username
    user = input("Username [%s]: " % getpass.getuser())
    if not user:
	    user=getpass.getuser()
	
    # get password
    pw = getpass.getpass()
    
    # The URL we are connnecting to
    global conString
    conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
    #conString=''+'xinchao'+'/' + 'Wang0408' +'@gwynne.cs.ualberta.ca:1521/CRS'
    try:
	    global connection 
	    global curs
	    connection = cx_Oracle.connect(conString)
	    curs = connection.cursor()
    except cx_Orprintacle.DatabaseError as exc:
    #except Exception as exc:
	    #pass
	    error, = exc.args
	    print( sys.stderr, "Oracle code:", error.code)
	    print( sys.stderr, "Oracle message:", error.message)


def register_user():                      # try to register the user, ask for email and password
    email = input("Enter your E-mail address that you wish to register: ")
    # check the existing of the email address
    curs.execute("select u.email from users u where u.email = '{}'".format(email))
    emails=curs.fetchall()
    if len(emails) > 0:
	    input("E-mail already exists (Press <ENTER> to continue)")
	    return
    password = getpass.getpass("Password: ")
    curs.execute("insert into users values ('{}', '{}', null)".format(email, password))
    connection.commit()
    input("User created Successfully (Press <ENTER> to continue)")	   
def login_user():                        # ask users to input the login username and password in order to login
    email=input("Enter your E-mail address: ")
    password = getpass.getpass("Enter your password: ")
    curs.execute("select u.email, u.pass from users u where u.email = '{0}' and u.pass = '{1}'".format(email, password))
    users=curs.fetchall()

    curs.execute("select u.email, u.last_login from users u where u.email = '{0}' and u.pass = '{1}'".format(email, password))
    getLog = curs.fetchall()
    print("your last login is " + getLog[0][1].strftime('%d/%m/%y'))
    print("\n")
    if len(users) == 1:
	    isAgent = False
	    curs.execute("select * from airline_agents a where a.email = '{}'".format(email))
	    agents=curs.fetchall()
	    if len(agents) == 1:
		    isAgent = True
	    user_input = interface.main(conString,connection,curs,email, isAgent)
	    return user_input
    else:
	    input("Invalid login")
    
main()	
