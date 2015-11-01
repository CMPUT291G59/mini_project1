import sys
import os
#using the Assigngment2 solution provide by instructor and Chris Wang's solution as well
def search_view(conString,connection,curs):           # view all the existing bookings
    curs.execute("Select view_name from all_views where lower(view_name) = 'available_flights'")
    a_flights=curs.fetchall()
    if len(a_flights)!=0:
        curs.execute("""drop view available_flights""")
        connection.commit()
    availableFlights="""
    create view available_flights(flightno,dep_date, src,dst,dep_time,arr_time,fare,seats,price) as(
    select 
    f.flightno, 
    sf.dep_date, 
    f.src, f.dst, 
    f.dep_time+(trunc(sf.dep_date)-trunc(f.dep_time)),
    f.dep_time+(trunc(sf.dep_date)-trunc(f.dep_time))+(f.est_dur/60+a2.tzone-a1.tzone)/24, 
    fa.fare, 
    fa.limit-count(tno) seats, 
    fa.price
    
    from flights f, 
    flight_fares fa, 
    sch_flights sf, 
    bookings b, 
    airports a1, 
    airports a2
    
    where f.flightno=sf.flightno and 
    f.flightno=fa.flightno and 
    f.src=a1.acode and
    f.dst=a2.acode and 
    fa.flightno=b.flightno(+) and 
    fa.fare=b.fare(+) and
    sf.dep_date=b.dep_date(+)
    
    group by f.flightno, 
    sf.dep_date, 
    f.src, 
    f.dst, 
    f.dep_time, 
    f.est_dur,
    a2.tzone,
    a1.tzone, 
    fa.fare, 
    fa.limit, 
    fa.price
    having fa.limit-count(tno) > 0)"""
    
    curs.execute(availableFlights)
    
    
    curs.execute("Select view_name from all_views where lower(view_name) = 'good_connections'")
    c_flights=curs.fetchall()
    if len(c_flights)!=0:
        curs.execute("""drop view good_connections""")
        connection.commit()    
    good_connections="""
    create view good_connections (flightno1,flightno2,src,dst,dep_date,dep_time,arr_time,layover,price,seat1,seat2,fare1,fare2) as
    select a1.flightno, 
    a2.flightno,  
    a1.src, 
    a2.dst, 
    a1.dep_date,
    a1.dep_time,
    a2.arr_time,
    a2.dep_time-a1.arr_time,
    min(a1.price+a2.price) price,
    a1.seats,
    a2.seats,
    a1.fare,
    a2.fare
    
    from available_flights a1, 
    available_flights a2
    where a1.dst=a2.src and 
    a1.arr_time +1.5/24 <=a2.dep_time and 
    a1.arr_time +5/24 >=a2.dep_time
    group by a1.src, 
    a2.dst, 
    a1.dep_date, 
    a1.flightno, 
    a2.flightno, 
    a1.dep_time, 
    a2.arr_time,
    a2.dep_time,
    a1.arr_time,
    a1.seats,
    a2.seats,
    a1.fare,
    a2.fare
    """
    curs.execute(good_connections)
    
    curs.execute("Select view_name from all_views where lower(view_name) = 'good2_connections'")
    c2_flights=curs.fetchall()
    if len(c2_flights)!=0:
        curs.execute("""drop view good2_connections""")
        connection.commit()    
    good2_connections="""
    create view good2_connections (flightno1,flightno2,flightno3,src,dst,dep_date,dep_time,arr_time,layover,price,seat1,seat2,seat3,fare1,fare2,fare3) as
    select a1.flightno, 
    a2.flightno,  
    a3.flightno,
    a1.src,
    a3.dst,
    a1.dep_date,
    a1.dep_time,
    a3.arr_time,
    (a2.dep_time-a1.arr_time)+(a3.dep_time-a2.arr_time),
    min(a1.price+a2.price+a3.price) price,
    a1.seats,
    a2.seats,
    a3.seats,
    a1.fare,
    a2.fare,
    a3.fare
    from available_flights a1, 
    available_flights a2,
    available_flights a3
    where a1.dst=a2.src and 
    a2.dst=a3.src and
    a1.arr_time +1.5/24 <=a2.dep_time and 
    a1.arr_time +5/24 >=a2.dep_time and 
    a2.arr_time +1.5/24 <=a3.dep_time and 
    a2.arr_time +5/24 >=a3.dep_time
    group by a1.src, 
    a3.dst,
    a1.dep_date, 
    a1.flightno, 
    a2.flightno,
    a3.flightno,
    a1.dep_time, 
    a3.arr_time,
    a2.dep_time,
    a1.arr_time,
    a2.arr_time,
    a3.dep_time,
    a1.seats,
    a2.seats,
    a3.seats,
    a1.fare,
    a2.fare,
    a3.fare
    """
    curs.execute(good2_connections)
    
    #3 connections
    #curs.execute("Select view_name from all_views where lower(view_name) = 'good2_connections'")
    #c2_flights=curs.fetchall()
    #if len(c2_flights)!=0:
        #curs.execute("""drop view good2_connections""")
        #connection.commit()    
    #good2_connections="""
    #create view good2_connections (flightno1,flightno2,flightno3,src,dst,dep_date,dep_time,arr_time,layover,price,seat1,seat2,seat3,fare1,fare2,fare3) as
    #select a1.flightno, 
    #a2.flightno,  
    #a3.flightno,
    #a1.src,
    #a3.dst,
    #a1.dep_date,
    #a1.dep_time,
    #a3.arr_time,
    #(a2.dep_time-a1.arr_time)+(a3.dep_time-a2.arr_time),
    #min(a1.price+a2.price+a3.price) price,
    #a1.seats,
    #a2.seats,
    #a3.seats,
    #a1.fare,
    #a2.fare,
    #a3.fare
    #from available_flights a1, 
    #available_flights a2,
    #available_flights a3
    #where a1.dst=a2.src and 
    #a2.dst=a3.src and
    #a1.arr_time +1.5/24 <=a2.dep_time and 
    #a1.arr_time +5/24 >=a2.dep_time and 
    #a2.arr_time +1.5/24 <=a3.dep_time and 
    #a2.arr_time +5/24 >=a3.dep_time
    #group by a1.src, 
    #a3.dst,
    #a1.dep_date, 
    #a1.flightno, 
    #a2.flightno,
    #a3.flightno,
    #a1.dep_time, 
    #a3.arr_time,
    #a2.dep_time,
    #a1.arr_time,
    #a2.arr_time,
    #a3.dep_time,
    #a1.seats,
    #a2.seats,
    #a3.seats,
    #a1.fare,
    #a2.fare,
    #a3.fare
    #"""
    #curs.execute(good2_connections)    
    connection.commit()    
