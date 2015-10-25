def search_flight(conString,connection,curs,email):
    dep_airport=input("Enter your departure airport: ")
    arr_airport=input("Enter your arrival airport: ")
    a=input("Do you want to book round trip? (Y/N) ")
    if a.upper()=="Y":
        