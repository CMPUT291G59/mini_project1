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
                flight_num = input("please enter the filght number that you want to update")
                dep_date = input("please enter the depart date of your flight")
                dep_time = input("please enter the actual depart time of your flight")
                record_dep(conString,connection,curs, flight_num, dep_date, dep_time)
        elif user_input == "4" and isAgent==True:
            flight_num = input("please enter the filght number that you want to update")
            arv_date = input("please enter the arrival date of your flight")
            arv_time = input("please enter the actual arrival time of your flight")
            record_arv(conString,connection,curs,flight_num, arv_date, arv_time)
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
        return_date=input("Enter your returen date (dd/mm/yyyy)")
    if roundtrip=="N":
        dep_date=input("Enter your departure date (dd/mm/yyyy)")
    a=input("Do you want 2 stop numbers? (Y/N) ")
    a=a.upper()
    if a=="N" and roundtrip=="N":
<<<<<<< HEAD
        print("Departure on "+dep_date+"\n")
        search.find_regular_flight(conString,connection,curs,email,src,dst,dep_date)
    if a=="N" and roundtrip=="Y":
        print("Departure on "+dep_date+"\n")
        search.find_regular_flight(conString,connection,curs,email,src,dst,dep_date)
        src1=src
        dst1=dst
        src=dst1
        dst=src1
        print("\n"+"Return on "+return_date+"\n")
        search.find_regular_flight(conString,connection,curs,email,src,dst,return_date)
    if a=="Y" and roundtrip=="N":
        print("Departure on "+dep_date+"\n")
        search.find_2stop_flight(conString,connection,curs,email,src,dst,dep_date)
    if a=="Y" and roundtrip=="Y":
        print("Departure on "+dep_date+"\n")
        search.find_2stop_flight(conString,connection,curs,email,src,dst,dep_date)
        src1=src
        dst1=dst
        src=dst1
        dst=src1
        print("\n"+"Return on "+return_date+"\n")
        search.find_2stop_flight(conString,connection,curs,email,src,dst,dep_date)
=======
        search.find_direct_flight(conString,connection,curs,email,src,dst,dep_date)


def record_dep(conString,connection,curs, flightno, dep_date, time):
    query = """UPDATE sch_flights
        SET act_dep_time = TO_DATE('{0}', 'HH24:MI')
        WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'DD/MM/YYYY')""".format(time, flightno, dep_date)	
    curs.execute(query)
    connection.commit()

def record_arv(conString,connection,curs, flightno,arv_date,time):
    query = """UPDATE sch_flights
        SET act_arr_time = TO_DATE('{0}', 'HH24:MI')
        WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'DD/MM/YYYY')""".format(time, flightno, arv_date)	
    curs.execute(query)
    connection.commit()

        
        
>>>>>>> 9a230ca0107cf4225104daaf6af44d2fa04d03f2
