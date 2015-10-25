import os

def main(conString,connection,curs,email, isAgent):
    while True:
        print("1.Search Flight?")
        print("2.List exiting bookings?")
        if isAgent==True:
            print("3.Rcord flight departure?")
            print("4.Rcord flight arrival?")
            print("5.Log out?")
        else:
            print("3.Log out?")
        user_input = input ("Please enter the opertion number to continue, or to log_out: ")	    
        if user_input == "1":
            Search.search_flight()
        elif user_input == "2":
            medical_test()
        elif user_input == "3":
            if isAgent==True:
                record_dep()
            else:
                curs.execute("update users set last_login = sysdate where users.email = '{}'".format(email))
                connection.commit()
                break
        elif user_input == "4" and isAgent==True:
            search_engine()
        elif user_input.lower() == '5' and isAgent==True:
            curs.execute("update users set last_login = sysdate where users.email = '{}'".format(email))
            connection.commit()
            break
        else:
            print("Invalid opertion number.")
            print()
        print()
    print()
    print("Thanks for using W&M flight booking System.")
    print("Your conveniency has always been our first priority.")
    print("We hope you have a nice day.")        
