import sys
import os 
import create_view
def find_direct_flight(conString,connection,curs,email,src,dst,dep_date):
    create_view.search_view(conString,connection,curs)
    query ="""select 
    flightno, 
    dep_date, 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    fare, 
    seats, 
    price 
    from available_flights a
    where a.src='{0}' and
    a.dst='{1}' and
    a.dep_date=to_date('{2}','dd/mm/yyyy')"""
    curs.execute(query.format(src, dst, dep_date))
    flight=curs.fetchall()
    print("Index"+5*" "+"Flightno"+2*" "+"src"+7*" "+"dst"+7*" "+"Dep_time"+2*" "+"Arr_time"+2*" "+"fare"+6*" "+"seats"+5*" "+"price")
    for i, a in enumerate(flight):
		    print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[2]) + (10-len(str(a[2])))*' ' + str(a[3]) + (10-len(str(a[3])))*' '+ str(a[4]) + (10-len(str(a[4])))*' '+ str(a[5]) + (10-len(str(a[5])))*' '+ str(a[6]) +(10-len(str(a[6])))*' '+ str(a[7]) + (10-len(str(a[7])))*' '+ str(a[8]))
    