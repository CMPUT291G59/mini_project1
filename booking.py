import random

def bookingView(conString,connection,curs, email):
    query = """select tickets.name, tickets.paid_price, bookings.* from
        bookings, tickets where
        tickets.tno = bookings.tno and
        tickets.email = '{0}'""".format(email)
        database.cursor.execute(query)

def addBooking(conString,connection,curs, tno, email, flightno, fare, dep_date, price):
    a = str(random.randint(0, 99))
    b = random.choice("ABCDEF")
    seatNum = a+b			
    query = """insert into bookings
        values({0}, '{1}', '{2}', to_date('{3}', 'YYYY-MM-DD'), '{4}')""".format(tno, flightno, fare, dep_date, seatNum)
    curs.execute(query)
    connnection.commit()
    return tno

def cancelBooking(conString,connection,curs, tno):
    query = """delete from
    bookings where bookings = {}""".format(tno)
    curs.execute(query)
    connection.commit()


