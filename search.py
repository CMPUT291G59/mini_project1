import sys
import os 
import create_view
def find_direct_flight(conString,connection,curs,email,src,dst,dep_date):
    print(11111)
    create_view.search_view(conString,connection,curs)
    print(22222)
    print(src,dst,dep_date)
    query ="""select * 
    from available_flights a
    where a.src='YEG' and
    a.dst='YVR' and
    a.dep_date=to_date('15/10/2015','dd/mm/yyyy')"""
    curs.execute(query.format(src, dst, dep_date))
    flight=curs.fetchall()
    print(flight)