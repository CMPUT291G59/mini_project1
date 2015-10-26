import os
import sys
import search
def main(conString,connection,curs,email, isAgent):
    while True:
        print("1.Search Flight?")
        print("2.List exiting bookings?")
        if isAgent==True:
            print("3.Rcord flight departure?")
            print("4.Rcord flight arrival?")
            print("Enter Q to logout your account")
        else:
            print("Enter Q to logout your account")
        user_input = input("Please enter the opertion number to continue, or to logout: ")
        quit = "q"
        if user_input == "1":
            search_flight(conString,connection,curs,email)
        elif user_input == "2":
            medical_test()
        elif user_input == "3":
            if isAgent==True:
                record_dep()
        elif user_input == "4" and isAgent==True:
            search_engine()
        elif user_input.lower() == 'q':
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
    return user_input

    
def search_flight(conString,connection,curs,email):
    src=input("Enter your departure airport: ")
    src=src.upper()
    dst=input("Enter your arrival airport: ")
    dst=dst.upper()
    roundtrip=input("Do you want to book round trip? (Y/N) ")
    roundtrip=roundtrip.upper()
    if roundtrip=="Y":
        dep_date=input("Enter your departure date (dd/mm/yyyy)")
        reture_date=input("Enter your returen date (dd/mm/yyyy)")
    if roundtrip=="N":
        dep_date=input("Enter your departure date (dd/mm/yyyy)")
    a=input("Do you want connecting flights? (Y/N) ")
    a=a.upper()
    if a=="N" and roundtrip=="N":
        search.find_direct_flight(conString,connection,curs,email,src,dst,dep_date)
        
        
