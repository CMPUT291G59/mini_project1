import random
import sys
import interface
def bookingView(conString,connection,curs, email):     #view all passengers infor from same login email account
    query = """select tickets.name, tickets.paid_price, bookings.* from
    bookings, tickets where
    tickets.tno = bookings.tno and
    tickets.email = '{0}'""".format(email)
    curs.execute(query)
    bv=curs.fetchall()
    print("Index".ljust(13)+"Ticket_no".ljust(13)+"passenger".ljust(13)+"dep_time".ljust(13)+"price")
    for i, a in enumerate(bv):
        print(str(i + 1).ljust(13) +str(a[2]).ljust(13)+ str(a[0].strip()).ljust(13)+(a[5].strftime('%d/%m/%y')).ljust(13)+str(a[1]))
        
        
def addBooking(conString,connection,curs, email, name, con, tno, pay, flightno, fare, dep_date):   # add Booking into the system if the passenger name appear with the same ticket name it will block the booking
    s = checkStatus(conString,connection,curs,email,name)
    if s == False:
        a = str(random.randint(0, 99))
        b = random.choice("ABCDEF")
        seatNum = a+b
    
        query =""" insert into passengers values('{0}','{1}','{3}')""".format(email, name, fare, con)
        curs.execute(query)
        connection.commit()
        query =""" insert into tickets values('{0}','{1}','{2}','{3}')""".format(tno, name, email, pay)
        curs.execute(query)
        connection.commit()
			
        query = """insert into bookings
            values({0}, '{1}', '{2}', to_date('{3}', 'DD/MM/YYYY'), '{4}')""".format(tno, flightno, fare, dep_date, seatNum)
        curs.execute(query)
        connection.commit()
        print("Your booking is successful! Your booking number is "+str(tno))
        return tno
    else:
        print("your booking exists")
        return tno



def cancelBooking(conString,connection,curs, tno, name):          # cancel a booking 
    query = """delete from
    bookings where bookings.tno = '{0}'""".format(tno)
    curs.execute(query)
    connection.commit()
    
    query = """delete from
    tickets where tickets.tno = '{0}'""".format(tno)
    curs.execute(query)
    connection.commit()        
    
    query = """delete from
    passengers where passengers.name = '{0}'""".format(name)
    curs.execute(query)
    connection.commit()  
    print("You flight is canceled!")

def checkStatus(conString,connection,curs,email,name):    # check if the passenger name exist in the DB
    query = """select passengers.name 
    from passengers, tickets, bookings
    where tickets.tno = bookings.tno
    and passengers.name = tickets.name
    and passengers.email = '{0}'
    and passengers.name = '{1}'""".format(email,name)
    curs.execute(query)
    b = curs.fetchall()
    if not b:
        return False
    else:
        return True



