import os
import sys
import search
import booking
import random
def main(conString,connection,curs,email, isAgent):          #create the user interface manu and ask users for input
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
            booking.bookingView(conString,connection,curs, email)
            a=input("Do you want cancel flight above?(Y/N) ")
            a=a.upper()
            if a=="Y":
                tno=input("Enter your ticket_no ")
                name=input("Enter your name ")
                booking.cancelBooking(conString,connection,curs, tno, name)
        elif user_input == "3":
            if isAgent==True:
                flight_num = input("please enter the filght number that you want to update ")
                dep_date = input("please enter the depart date of your flight(dd/mm/yyyy) ")
                dep_time = input("please enter the actual depart time of your flight(hh:mm) ")
                record_dep(conString,connection,curs, flight_num, dep_date, dep_time)
        elif user_input == "4" and isAgent==True:
            flight_num = input("please enter the filght number that you want to update ")
            arv_date = input("please enter the arrival date of your flight(dd/mm/yyyy) ")
            arv_time = input("please enter the actual arrival time of your flight(hh:mm) ")
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

    
def search_flight(conString,connection,curs,email):                        # this is the search engine interface
    src=input("Enter your departure airport: ")
    src=search.find_acode(conString,connection,curs,src)
    print(src)
    dst=input("Enter your arrival airport: ")
    dst=search.find_acode(conString,connection,curs,dst)
    print(dst)
    roundtrip=input("Do you want to book round trip? (Y/N) ")
    roundtrip=roundtrip.upper()
    if roundtrip=="Y":
        dep_date=input("Enter your departure date (dd/mm/yyyy)")
        return_date=input("Enter your returen date (dd/mm/yyyy)")
    if roundtrip=="N":
        dep_date=input("Enter your departure date (dd/mm/yyyy)")
    print("How many stop you want? (Maximum 2 stop) ")
    c="You enter is greater than maxmum number of stops.\nPlease try entera number less than 3"
    a=input("")
    a=check_int(a,3,c)
    if a==0 and roundtrip=="N":
        print("Departure on "+dep_date+"\n")
        alist=search.find_direct_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass         
    if a==0 and roundtrip=="Y":
        print("Departure on "+dep_date+"\n")
        alist=search.find_direct_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass                 
        src1=src
        dst1=dst
        src=dst1
        dst=src1
        print("\n"+"Return on "+return_date+"\n")
        alist=search.find_direct_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass         
        
    if a==1 and roundtrip=="N":
        print("Departure on "+dep_date+"\n")
        alist=search.find_regular_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass                
    if a==1 and roundtrip=="Y":
        print("Departure on "+dep_date+"\n")
        alist=search.find_regular_flight(conString,connection,curs,email,src,dst,return_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass                 
        src1=src
        dst1=dst
        src=dst1
        dst=src1
        print("\n"+"Return on "+return_date+"\n")
        alist=search.find_regular_flight(conString,connection,curs,email,src,dst,return_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass         
        
    if a==2 and roundtrip=="N":
        print("Departure on "+dep_date+"\n")
        alist=search.find_2stop_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print(1)
        elif check=="N":
            pass        
    if a==2 and roundtrip=="Y":
        print("Departure on "+dep_date+"\n")
        alist=search.find_2stop_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass                 
        src1=src
        dst1=dst
        src=dst1
        dst=src1
        print("\n"+"Return on "+return_date+"\n")
        alist=search.find_2stop_flight(conString,connection,curs,email,src,dst,dep_date)
        check=input("Do you want to book any flight above? (Y/N) ")
        check=check_str(check)
        if check=="Y":
            print("Enter the index of flight you want to choose ")
            choose=input("")
            choose=check_int(choose,len(alist)+1,"Invalid enter!")
            passenger_detail(conString,connection,curs, email,alist,choose,dep_date)
        elif check=="N":
            pass         

def record_dep(conString,connection,curs, flightno, dep_date, time):             # function for agent to record the dep_time
    query = """UPDATE sch_flights
        SET act_dep_time = TO_DATE('{0}', 'HH24:MI')
        WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'DD/MM/YYYY')""".format(time, flightno, dep_date)	
    curs.execute(query)
    connection.commit()
    query1="""select flightno, 
    act_dep_time 
    from sch_flights
    WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'DD/MM/YYYY')""".format(time, flightno, dep_date)
    curs.execute(query1)
    a=curs.fetchall()
    print("Your update "+a[0][0]+"actual depart time to "+(a[0][1].strftime('%H:%M:%S')))

def record_arv(conString,connection,curs, flightno,arv_date,time):              # function for agent to record the arr_date
    query = """UPDATE sch_flights
        SET act_arr_time = TO_DATE('{0}', 'HH24:MI')
        WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'DD/MM/YYYY')""".format(time, flightno, arv_date)	
    curs.execute(query)
    connection.commit()
    query2="""select flightno, 
    act_arr_time 
    from sch_flights
    WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'DD/MM/YYYY')""".format(time, flightno, arv_date)
    curs.execute(query2)
    a=curs.fetchall()
    print("Your update "+a[0][0]+"actual arrival time to "+(a[0][1].strftime('%H:%M:%S')))



def check_int(a,b,c):          # check input type
    check=False
    while check==False:
        try:
            a=int(a)
            if a>b or isinstance(a,int)==False:
                check=False
                print(c)
                a=int(input(""))
            else:
                return a
        except: 
            ValueError
            a=input("Enter a number! ")
            check=False
def check_str(a):         # check the input type 
    check=False
    a=a.upper()
    while check==False:
        if a!="Y" and a!="N" or isinstance(a,str)==False:
            check=False
            print("You enter is invalid! Please try again!")
            a=input("")
            a=a.upper()
        else:
            return a
def passenger_detail(conString,connection,curs, email,a,b,dep_date):       #fetch the passengers information from database
    chek=False
    print(len(a[0]))
    print(a)
    print("")
    print(a[0])
    name=input("Enter passenger name ")
    con=input("Enter your country ")
    #book when there is no connection flights
    if len(a[b-1])==9: 
        c=a[b-1]
        flightno=c[0]
        fare=c[7]
        pay=c[6]
        tno=random.randint(0, 9999)
        booking.addBooking(conString,connection,curs, email, name, con, tno, pay, flightno, fare, dep_date)
    #book when there is 1 connection flights
    elif len(a[0])==14:
        c=a[b-1]
        flightno1=c[0]
        flightno2=c[1]
        fare1=c[10]
        fare2=c[12]
        pay=c[8]
        tno=random.randint(0, 9999)
        booking.addBooking(conString,connection,curs, email, name, con, tno, pay, flightno1, fare1, dep_date)
        tno=random.randint(0, 9999)
        query =""" insert into tickets values('{0}','{1}','{2}','{3}')""".format(tno, name, email, pay)
        curs.execute(query)
        connection.commit()
        query = """delete from
        bookings where bookings.tno = '{0}'""".format(tno)
        curs.execute(query)
        connection.commit()

    #book when there is 2 connection flights
    elif len(a[0])==16:
        c=a[b-1]
        flightno1=c[0]
        flightno2=c[1]
        flightno3=c[2]
        fare1=c[10]
        fare2=c[12]
        fare3=c[14]
        pay=c[8]
        tno=random.randint(0, 9999)
        booking.addBooking(conString,connection,curs, email, name, con, tno, pay, flightno1, fare1, dep_date)
        tno=random.randint(0, 9999)
        query =""" insert into tickets values('{0}','{1}','{2}','{3}')""".format(tno, name, email, pay)
        curs.execute(query)
        connection.commit()
        query = """delete from
        bookings where bookings.tno = '{0}'""".format(tno)
        curs.execute(query)
        connection.commit() 
        tno=random.randint(0, 9999)
        query =""" insert into tickets values('{0}','{1}','{2}','{3}')""".format(tno, name, email, pay)
        curs.execute(query)
        connection.commit()
        query = """delete from
        bookings where bookings.tno = '{0}'""".format(tno)
        curs.execute(query)
        connection.commit()
        